#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

PAGES = {
    Path("index.html"): None,
    Path("profile/index.html"): None,
    Path("career/index.html"): "Career",
    Path("activities/index.html"): None,
    Path("projects/index.html"): "Projects",
    Path("media/index.html"): None,
    Path("contact/index.html"): "Contact",
}

ITEMS = [
    ("About", "#about", "../#about"),
    ("Work", "#work", "../#work"),
    ("Projects", "projects/", "../projects/"),
    ("Career", "career/", "../career/"),
    ("Contact", "contact/", "../contact/"),
]


def render_nav(is_home: bool, current: str | None) -> str:
    lines = ['    <nav class="nav" aria-label="メインナビゲーション">']
    for label, home_href, sub_href in ITEMS:
        target = home_href if is_home else sub_href
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
        replacement = render_nav(path == Path("index.html"), current)
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
