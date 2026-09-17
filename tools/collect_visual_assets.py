#!/usr/bin/env python3
"""Collect visual asset candidates referenced by the public website.

Conservative by design:
- Never downloads or copies external images.
- Registers YouTube thumbnails as external platform previews.
- Resolves this site's absolute canonical image URLs back to repository-local assets.
- Honors owner-authorized remote image sources from approved_remote_image_sources.json.
- Marks other remote/OG images REVIEW_REQUIRED.
- Indexes local repository images without inferring ownership/rights.
- Preserves generated_at when registry content is unchanged.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import parse_qs, unquote, urljoin, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "assets" / "data" / "media-assets.json"
APPROVED_REMOTE_SOURCES = ROOT / "tools" / "approved_remote_image_sources.json"
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".avif"}
SKIP_DIRS = {".git", ".github", "__pycache__"}
YOUTUBE_HOSTS = {"youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be"}
YOUTUBE_IMAGE_HOSTS = {"img.youtube.com", "i.ytimg.com"}
SITE_HOST = "noritap.github.io"
SITE_PATH_PREFIX = "/furusho-official/"
MAX_FETCH_BYTES = 512_000

class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(); self.links=[]; self.images=[]; self.og_images=[]
    def handle_starttag(self, tag, attrs):
        data={k.lower():(v or "") for k,v in attrs}; tag=tag.lower()
        if tag=="a" and data.get("href"): self.links.append(data["href"].strip())
        elif tag=="img" and data.get("src"): self.images.append(data["src"].strip())
        elif tag=="meta":
            prop=(data.get("property") or data.get("name") or "").lower()
            if prop=="og:image" and data.get("content"): self.og_images.append(data["content"].strip())

def iter_html_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.html"):
        if not any(part in SKIP_DIRS for part in path.parts): yield path

def parse_html(text):
    parser=PageParser(); parser.feed(text); return parser

def normalize_host(url): return urlparse(url).netloc.lower().split(":")[0]

def youtube_id(url):
    parsed=urlparse(url); host=normalize_host(url)
    if host not in YOUTUBE_HOSTS: return None
    if host=="youtu.be": return parsed.path.strip("/").split("/")[0] or None
    if parsed.path=="/watch": return (parse_qs(parsed.query).get("v") or [None])[0]
    match=re.match(r"^/(?:embed|shorts|live)/([^/?#]+)", parsed.path); return match.group(1) if match else None

def youtube_image_id(url):
    if normalize_host(url) not in YOUTUBE_IMAGE_HOSTS: return None
    match=re.search(r"/vi(?:_webp)?/([^/?#]+)/", urlparse(url).path); return match.group(1) if match else None

def page_relative(page): return page.relative_to(ROOT).as_posix()

def add_entry(entries,key,entry,found_in):
    if key not in entries: entry["found_in"]=[found_in]; entries[key]=entry
    elif found_in not in entries[key]["found_in"]: entries[key]["found_in"].append(found_in)

def repository_path_from_absolute(url):
    parsed=urlparse(url)
    if normalize_host(url)!=SITE_HOST or not parsed.path.startswith(SITE_PATH_PREFIX): return None
    relative=unquote(parsed.path[len(SITE_PATH_PREFIX):]).lstrip("/")
    if not relative: return None
    candidate=(ROOT/relative).resolve()
    try: candidate.relative_to(ROOT)
    except ValueError: return None
    return candidate

def repository_image_entry(candidate):
    try: rel=candidate.relative_to(ROOT)
    except ValueError: return None
    if rel.suffix.lower() not in IMAGE_SUFFIXES: return None
    key=f"local:{rel.as_posix()}"
    return key,{"type":"repository_image","source_url":None,"image_url":rel.as_posix(),"local_path":rel.as_posix(),"usage_status":"EXISTING_PUBLIC_ASSET" if candidate.exists() else "MISSING_LOCAL_FILE","rights_status":"RIGHTS_NOT_INFERRED","auto_publish":candidate.exists()}

def local_image_entry(src,page):
    parsed=urlparse(src)
    if parsed.scheme in {"http","https"} or src.startswith("//"): return None
    if not parsed.path: return None
    return repository_image_entry((page.parent/parsed.path).resolve())

def load_approved_remote_sources():
    try: data=json.loads(APPROVED_REMOTE_SOURCES.read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError): return []
    return data.get("sources",[])

APPROVED_SOURCES = load_approved_remote_sources()

def approved_remote_source(url):
    parsed=urlparse(url); host=normalize_host(url)
    for source in APPROVED_SOURCES:
        if host==source.get("host","").lower() and parsed.path.startswith(source.get("path_prefix","/")):
            return source
    return None

def remote_image_entry(url):
    approved=approved_remote_source(url)
    if approved:
        return f"remote:{url}",{"type":"remote_image","source_url":url,"image_url":url,"local_path":None,"usage_status":approved.get("usage_status","OWNER_AUTHORIZED_CROSS_SITE"),"rights_status":approved.get("rights_status","OWNER_AUTHORIZED_REUSE"),"authorization":approved.get("authorization"),"auto_publish":True}
    return f"remote:{url}",{"type":"remote_image","source_url":url,"image_url":url,"local_path":None,"usage_status":"REVIEW_REQUIRED","rights_status":"UNVERIFIED","auto_publish":False}

def youtube_entry(video_id,source_url=None):
    return f"youtube:{video_id}",{"type":"youtube_thumbnail","source_url":source_url or f"https://www.youtube.com/watch?v={video_id}","image_url":f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg","local_path":None,"usage_status":"AUTO_EXTERNAL_PREVIEW","rights_status":"PLATFORM_PREVIEW_REFERENCE","auto_publish":True}

def classify_image(src,page):
    parsed=urlparse(src)
    if parsed.scheme not in {"http","https"} and not src.startswith("//"): return local_image_entry(src,page)
    video_id=youtube_image_id(src)
    if video_id: return youtube_entry(video_id)
    same_site=repository_path_from_absolute(src)
    if same_site: return repository_image_entry(same_site)
    return remote_image_entry(src)

def fetch_og_image(url):
    request=Request(url,headers={"User-Agent":"furusho-official-visual-asset-collector/1.2"})
    with urlopen(request,timeout=8) as response:
        if "text/html" not in response.headers.get("Content-Type",""): return None
        data=response.read(MAX_FETCH_BYTES)
    parser=parse_html(data.decode("utf-8",errors="ignore")); return urljoin(url,parser.og_images[0]) if parser.og_images else None

def collect(fetch_og=False):
    entries={}; external_links={}
    for page in sorted(iter_html_files(ROOT)):
        rel_page=page_relative(page); parser=parse_html(page.read_text(encoding="utf-8",errors="ignore"))
        for src in parser.images+parser.og_images:
            classified=classify_image(src,page)
            if classified: key,entry=classified; add_entry(entries,key,entry,rel_page)
        for href in parser.links:
            vid=youtube_id(href)
            if vid: key,entry=youtube_entry(vid,href); add_entry(entries,key,entry,rel_page); continue
            parsed=urlparse(href)
            if fetch_og and parsed.scheme in {"http","https"} and normalize_host(href) not in YOUTUBE_HOSTS: external_links.setdefault(href,set()).add(rel_page)
    if fetch_og:
        for url,pages in sorted(external_links.items()):
            try: image=fetch_og_image(url)
            except Exception: image=None
            if not image: continue
            classified=classify_image(image,ROOT/"index.html")
            if classified and classified[1]["usage_status"]!="REVIEW_REQUIRED":
                key,entry=classified
                for found_in in sorted(pages): add_entry(entries,key,entry.copy(),found_in)
                continue
            entries[f"og:{url}"]={"type":"og_image_candidate","source_url":url,"image_url":image,"local_path":None,"usage_status":"REVIEW_REQUIRED","rights_status":"UNVERIFIED","auto_publish":False,"found_in":sorted(pages)}
    ordered=[dict({"id":key},**entries[key]) for key in sorted(entries)]; counts={}
    for item in ordered: counts[item["usage_status"]]=counts.get(item["usage_status"],0)+1
    return {"schema_version":1,"generated_at":datetime.now(timezone.utc).isoformat(timespec="seconds"),"generator":"tools/collect_visual_assets.py","policy":{"external_images_downloaded":False,"youtube_thumbnails":"AUTO_EXTERNAL_PREVIEW","same_site_absolute_images":"RESOLVE_TO_REPOSITORY_ASSET","approved_remote_images":"OWNER_AUTHORIZED_CROSS_SITE","remote_or_og_images":"REVIEW_REQUIRED","repository_images":"RIGHTS_NOT_INFERRED"},"summary":{"total":len(ordered),"by_usage_status":counts},"assets":ordered}

def without_generated_at(data): clone=dict(data); clone.pop("generated_at",None); return clone

def stabilize_generated_at(data,output):
    if not output.exists(): return data
    try: previous=json.loads(output.read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError): return data
    if without_generated_at(previous)==without_generated_at(data): data["generated_at"]=previous.get("generated_at",data["generated_at"])
    return data

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--fetch-og",action="store_true"); parser.add_argument("--output",type=Path,default=DEFAULT_OUTPUT); parser.add_argument("--stdout",action="store_true"); args=parser.parse_args()
    output=args.output if args.output.is_absolute() else ROOT/args.output; data=stabilize_generated_at(collect(args.fetch_og),output); payload=json.dumps(data,ensure_ascii=False,indent=2)+"\n"
    if args.stdout: print(payload,end=""); return 0
    output.parent.mkdir(parents=True,exist_ok=True); output.write_text(payload,encoding="utf-8"); print(f"Wrote {data['summary']['total']} assets to {output.relative_to(ROOT)}"); return 0

if __name__=="__main__": raise SystemExit(main())
