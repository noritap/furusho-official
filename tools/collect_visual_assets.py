#!/usr/bin/env python3
"""Collect visual asset candidates referenced by the public website.

Conservative by design:
- Never downloads or copies external images.
- Registers YouTube thumbnails as external platform previews.
- Marks other remote/OG images REVIEW_REQUIRED.
- Indexes local repository images without inferring ownership/rights.

Usage:
    python3 tools/collect_visual_assets.py
    python3 tools/collect_visual_assets.py --fetch-og
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import parse_qs, urljoin, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "assets" / "data" / "media-assets.json"
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".avif"}
SKIP_DIRS = {".git", ".github", "__pycache__"}
YOUTUBE_HOSTS = {"youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be"}
MAX_FETCH_BYTES = 512_000


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.images: list[str] = []
        self.og_images: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {k.lower(): (v or "") for k, v in attrs}
        tag = tag.lower()
        if tag == "a" and data.get("href"):
            self.links.append(data["href"].strip())
        elif tag == "img" and data.get("src"):
            self.images.append(data["src"].strip())
        elif tag == "meta":
            prop = (data.get("property") or data.get("name") or "").lower()
            if prop == "og:image" and data.get("content"):
                self.og_images.append(data["content"].strip())


def iter_html_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.html"):
        if not any(part in SKIP_DIRS for part in path.parts):
            yield path


def parse_html(text: str) -> PageParser:
    parser = PageParser()
    parser.feed(text)
    return parser


def normalize_host(url: str) -> str:
    return urlparse(url).netloc.lower().split(":")[0]


def youtube_id(url: str) -> str | None:
    parsed = urlparse(url)
    host = normalize_host(url)
    if host not in YOUTUBE_HOSTS:
        return None
    if host == "youtu.be":
        candidate = parsed.path.strip("/").split("/")[0]
        return candidate or None
    if parsed.path == "/watch":
        return (parse_qs(parsed.query).get("v") or [None])[0]
    match = re.match(r"^/(?:embed|shorts|live)/([^/?#]+)", parsed.path)
    return match.group(1) if match else None


def page_relative(page: Path) -> str:
    return page.relative_to(ROOT).as_posix()


def add_entry(entries: dict[str, dict], key: str, entry: dict, found_in: str) -> None:
    if key not in entries:
        entry["found_in"] = [found_in]
        entries[key] = entry
    elif found_in not in entries[key]["found_in"]:
        entries[key]["found_in"].append(found_in)


def local_image_entry(src: str, page: Path) -> tuple[str, dict] | None:
    parsed = urlparse(src)
    if parsed.scheme in {"http", "https"} or src.startswith("//"):
        return None
    clean = parsed.path
    if not clean:
        return None
    candidate = (page.parent / clean).resolve()
    try:
        rel = candidate.relative_to(ROOT)
    except ValueError:
        return None
    if rel.suffix.lower() not in IMAGE_SUFFIXES:
        return None
    key = f"local:{rel.as_posix()}"
    return key, {
        "type": "repository_image",
        "source_url": None,
        "image_url": rel.as_posix(),
        "local_path": rel.as_posix(),
        "usage_status": "EXISTING_PUBLIC_ASSET" if candidate.exists() else "MISSING_LOCAL_FILE",
        "rights_status": "RIGHTS_NOT_INFERRED",
        "auto_publish": candidate.exists(),
    }


def remote_image_entry(url: str) -> tuple[str, dict]:
    return f"remote:{url}", {
        "type": "remote_image",
        "source_url": url,
        "image_url": url,
        "local_path": None,
        "usage_status": "REVIEW_REQUIRED",
        "rights_status": "UNVERIFIED",
        "auto_publish": False,
    }


def youtube_entry(video_id: str, source_url: str) -> tuple[str, dict]:
    return f"youtube:{video_id}", {
        "type": "youtube_thumbnail",
        "source_url": source_url,
        "image_url": f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
        "local_path": None,
        "usage_status": "AUTO_EXTERNAL_PREVIEW",
        "rights_status": "PLATFORM_PREVIEW_REFERENCE",
        "auto_publish": True,
    }


def fetch_og_image(url: str) -> str | None:
    request = Request(url, headers={"User-Agent": "furusho-official-visual-asset-collector/1.0"})
    with urlopen(request, timeout=8) as response:
        content_type = response.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            return None
        data = response.read(MAX_FETCH_BYTES)
    parser = parse_html(data.decode("utf-8", errors="ignore"))
    return urljoin(url, parser.og_images[0]) if parser.og_images else None


def collect(fetch_og: bool = False) -> dict:
    entries: dict[str, dict] = {}
    external_links: dict[str, set[str]] = {}

    for page in sorted(iter_html_files(ROOT)):
        rel_page = page_relative(page)
        parser = parse_html(page.read_text(encoding="utf-8", errors="ignore"))

        for src in parser.images + parser.og_images:
            parsed = urlparse(src)
            if parsed.scheme in {"http", "https"}:
                key, entry = remote_image_entry(src)
                add_entry(entries, key, entry, rel_page)
            else:
                local = local_image_entry(src, page)
                if local:
                    key, entry = local
                    add_entry(entries, key, entry, rel_page)

        for href in parser.links:
            vid = youtube_id(href)
            if vid:
                key, entry = youtube_entry(vid, href)
                add_entry(entries, key, entry, rel_page)
                continue

            parsed = urlparse(href)
            if fetch_og and parsed.scheme in {"http", "https"}:
                host = normalize_host(href)
                if host not in YOUTUBE_HOSTS:
                    external_links.setdefault(href, set()).add(rel_page)

    if fetch_og:
        for url, pages in sorted(external_links.items()):
            try:
                image = fetch_og_image(url)
            except Exception:
                image = None
            if image:
                entries[f"og:{url}"] = {
                    "type": "og_image_candidate",
                    "source_url": url,
                    "image_url": image,
                    "local_path": None,
                    "usage_status": "REVIEW_REQUIRED",
                    "rights_status": "UNVERIFIED",
                    "auto_publish": False,
                    "found_in": sorted(pages),
                }

    ordered = [dict({"id": key}, **entries[key]) for key in sorted(entries)]
    counts: dict[str, int] = {}
    for item in ordered:
        counts[item["usage_status"]] = counts.get(item["usage_status"], 0) + 1

    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "generator": "tools/collect_visual_assets.py",
        "policy": {
            "external_images_downloaded": False,
            "youtube_thumbnails": "AUTO_EXTERNAL_PREVIEW",
            "remote_or_og_images": "REVIEW_REQUIRED",
            "repository_images": "RIGHTS_NOT_INFERRED",
        },
        "summary": {"total": len(ordered), "by_usage_status": counts},
        "assets": ordered,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch-og", action="store_true", help="Fetch external pages and register og:image candidates.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--stdout", action="store_true", help="Print JSON instead of writing the registry.")
    args = parser.parse_args()

    data = collect(fetch_og=args.fetch_og)
    payload = json.dumps(data, ensure_ascii=False, indent=2) + "\n"

    if args.stdout:
        print(payload, end="")
        return 0

    output = args.output if args.output.is_absolute() else ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(payload, encoding="utf-8")
    print(f"Wrote {data['summary']['total']} assets to {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
