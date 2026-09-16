#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

PAGES = [
    Path("index.html"),
    Path("profile/index.html"),
    Path("career/index.html"),
    Path("activities/index.html"),
    Path("projects/index.html"),
    Path("media/index.html"),
    Path("contact/index.html"),
]

EXPECTED_LABELS = ["About", "Work", "Projects", "Career", "Contact"]

EXPECTED_HREFS_HOME = {
    "About": "#about",
    "Work": "#work",
    "Projects": "projects/",
    "Career": "career/",
    "Contact": "contact/",
}

EXPECTED_HREFS_SUBPAGE = {
    "About": "../#about",
    "Work": "../#work",
    "Projects": "../projects/",
    "Career": "../career/",
    "Contact": "../contact/",
}

CURRENT_PAGE_LABEL = {
    Path("projects/index.html"): "Projects",
    Path("career/index.html"): "Career",
    Path("contact/index.html"): "Contact",
}


def extract_main_nav(text: str) -> str:
    match = re.search(r'<nav\s+class="nav"[^>]*>(.*?)</nav>', text, re.S | re.I)
    return match.group(1) if match else ""


def extract_links(nav: str) -> list[tuple[str, str, str]]:
    links: list[tuple[str, str, str]] = []
    for match in re.finditer(r'<a\s+([^>]*)>(.*?)</a>', nav, re.S | re.I):
        attrs = match.group(1)
        label = re.sub(r"<[^>]+>", "", match.group(2)).strip()
        href_match = re.search(r'href="([^"]*)"', attrs, re.I)
        href = href_match.group(1) if href_match else ""
        links.append((label, href, attrs))
    return links


def audit(root: Path) -> list[tuple[str, list[str]]]:
    problems: list[tuple[str, list[str]]] = []
    for rel in PAGES:
        path = root / rel
        issues: list[str] = []
        if not path.exists():
            issues.append("FILE_MISSING")
            problems.append((str(rel), issues))
            continue

        nav = extract_main_nav(path.read_text(encoding="utf-8"))
        if not nav:
            issues.append("MAIN_NAV_MISSING")
            problems.append((str(rel), issues))
            continue

        links = extract_links(nav)
        labels = [label for label, _, _ in links]
        if labels != EXPECTED_LABELS:
            issues.append("ORDER_OR_LABELS")

        expected_hrefs = EXPECTED_HREFS_HOME if rel == Path("index.html") else EXPECTED_HREFS_SUBPAGE
        current_label = CURRENT_PAGE_LABEL.get(rel)

        for label, href, attrs in links:
            expected = "./" if label == current_label else expected_hrefs.get(label)
            if expected is None:
                continue
            if href != expected:
                issues.append(f"HREF:{label}")
            has_current = 'aria-current="page"' in attrs
            if label == current_label and not has_current:
                issues.append(f"CURRENT_MISSING:{label}")
            if label != current_label and has_current:
                issues.append(f"CURRENT_UNEXPECTED:{label}")
            if label == "Contact" and 'class="nav-cta"' not in attrs:
                issues.append("CONTACT_CTA_CLASS")

        if issues:
            problems.append((str(rel), sorted(set(issues))))
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Furusho Official FURUSHO-NAV-2 global navigation drift")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    problems = audit(args.root)
    if not problems:
        print("NAVIGATION AUDIT: PASS (FURUSHO-NAV-2)")
        return 0

    print("NAVIGATION AUDIT: DRIFT DETECTED")
    for page, issues in problems:
        print(f"- {page}: {', '.join(issues)}")
    print(f"drift_pages={len(problems)}")
    return 1 if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
