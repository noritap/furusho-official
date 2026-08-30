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

REQUIRED_LABELS = ["Profile", "Career", "Activities", "Projects", "Media", "Contact"]


def extract_main_nav(text: str) -> str:
    match = re.search(r'<nav\s+class="nav"[^>]*>(.*?)</nav>', text, re.S | re.I)
    return match.group(1) if match else ""


def audit(root: Path) -> list[tuple[str, list[str]]]:
    problems: list[tuple[str, list[str]]] = []
    for rel in PAGES:
        path = root / rel
        missing: list[str] = []
        if not path.exists():
            missing.append("FILE_MISSING")
        else:
            nav = extract_main_nav(path.read_text(encoding="utf-8"))
            if not nav:
                missing.append("MAIN_NAV_MISSING")
            else:
                for label in REQUIRED_LABELS:
                    if f">{label}<" not in nav:
                        missing.append(label)
        if missing:
            problems.append((str(rel), missing))
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Furusho Official global navigation drift")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    problems = audit(args.root)
    if not problems:
        print("NAVIGATION AUDIT: PASS")
        return 0

    print("NAVIGATION AUDIT: DRIFT DETECTED")
    for page, missing in problems:
        print(f"- {page}: missing {', '.join(missing)}")
    print(f"drift_pages={len(problems)}")
    return 1 if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
