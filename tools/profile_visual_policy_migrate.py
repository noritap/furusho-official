#!/usr/bin/env python3
from pathlib import Path

path = Path("profile/index.html")
text = path.read_text(encoding="utf-8")

replacements = {
'''            <img src="https://p1-598f4ae0.imageflux.jp/c!/w=1200,h=630,a=2,ir=auto/5a264227c8f22c4ecd0010c5/ogp/15f156b233266ca1861f.png" alt="Rhythm Speaker 公式サイトのビジュアル" width="1200" height="630" loading="lazy" decoding="async">''': '''            <span class="current-project-visual-type" aria-hidden="true">RS</span>''',
'''            <img src="https://noritap.github.io/tapdance-cardgame/images/tapdance.jpg" alt="Tap Dance Card Game のメインビジュアル" width="1200" height="800" loading="lazy" decoding="async">''': '''            <span class="current-project-visual-type" aria-hidden="true">TAP</span>''',
'''    .current-project-card:hover img{transform:scale(1.025);filter:saturate(.78) contrast(1.08) brightness(.76)}''': '''    .current-project-visual-type{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:Georgia,"Yu Mincho","Hiragino Mincho ProN",serif;font-size:clamp(4rem,10vw,8rem);letter-spacing:-.06em;color:#777;background:linear-gradient(135deg,#171717,#2d2d2d);transition:transform .3s ease,color .3s ease}\n    .current-project-card:hover .current-project-visual-type{transform:scale(1.025);color:#929292}'''
}

for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f"expected migration target not found: {old[:80]}")
    text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")
print("profile visual policy migration complete")
