#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

PAGES = {
    Path("index.html"): None,
    Path("profile/index.html"): "Profile",
    Path("career/index.html"): "Career",
    Path("activities/index.html"): "Activities",
    Path("projects/index.html"): "Projects",
    Path("media/index.html"): "Media",
    Path("contact/index.html"): "Contact",
}

ITEMS = [
    ("Profile", "profile/"),
    ("Career", "career/"),
    ("Activities", "activities/"),
    ("Projects", "projects/"),
    ("Media", "media/"),
    ("Contact", "contact/"),
]


def render_nav(prefix: str, current: str | None) -> str:
    lines = ['    <nav class="nav" aria-label="メインナビゲーション">']
    for label, href in ITEMS:
        target = href if not prefix else prefix + href
        attrs = []
        if label == "Contact":
            attrs.append('class="nav-cta"')
        if current == label:
            attrs.append('aria-current="page"')
            target = "./"
        attr_text = (" " + " ".join(attrs)) if attrs else ""
        lines.append(f'      <a{attr_text} href="{target}">{label}</a>')
    lines.append("    </nav>")
    return "\n".join(lines)


def main() -> int:
    changed = 0
    for path, current in PAGES.items():
        text = path.read_text(encoding="utf-8")
        prefix = "" if path == Path("index.html") else "../"
        replacement = render_nav(prefix, current)
        updated, count = re.subn(
            r'    <nav\s+class="nav"[^>]*>.*?</nav>',
            replacement,
            text,
            count=1,
            flags=re.S | re.I,
        )
        if count != 1:
            raise SystemExit(f"navigation block not found exactly once: {path}")
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            print(f"UPDATED {path}")
            changed += 1
        else:
            print(f"OK {path}")
    print(f"changed_pages={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
