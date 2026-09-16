#!/usr/bin/env python3
from pathlib import Path

VIDEO_URL = "https://www.youtube.com/watch?v=RCHe13BrkUo"
THUMB_URL = "https://img.youtube.com/vi/RCHe13BrkUo/hqdefault.jpg"

# 1) Career: add verified video link to the existing Yanawaraba item.
career_path = Path("career/index.html")
career = career_path.read_text(encoding="utf-8")
old_career = '<article><span>MUSIC</span><h3>やなわらばー</h3><p>「いちごいちえ」振付・出演</p></article>'
new_career = f'<article><span>MUSIC</span><h3>やなわらばー</h3><p>「いちごいちえ」振付・出演</p><a class="career-link" href="{VIDEO_URL}" target="_blank" rel="noopener noreferrer" aria-label="やなわらばー いちごいちえの関連動画をYouTubeで見る">WATCH VIDEO →</a></article>'
if old_career not in career:
    raise SystemExit("career target not found")
career_path.write_text(career.replace(old_career, new_career, 1), encoding="utf-8")

# Shared visual-work card for Profile.
profile_path = Path("profile/index.html")
profile = profile_path.read_text(encoding="utf-8")
profile_anchor = '''          <a class="visual-work-card" href="https://www.youtube.com/watch?v=15566qQHhlw" target="_blank" rel="noopener noreferrer" aria-label="スキマスイッチ 虹のレシピの関連動画をYouTubeで見る">
            <img src="https://i.ytimg.com/vi/15566qQHhlw/hqdefault.jpg" alt="スキマスイッチ 虹のレシピ 関連動画サムネイル" width="480" height="360" loading="lazy" decoding="async">
            <span class="work-type">MUSIC</span><strong>スキマスイッチ</strong><em>WATCH</em>
          </a>'''
profile_card = f'''{profile_anchor}
          <a class="visual-work-card" href="{VIDEO_URL}" target="_blank" rel="noopener noreferrer" aria-label="やなわらばー いちごいちえの関連動画をYouTubeで見る">
            <img src="{THUMB_URL}" alt="やなわらばー いちごいちえ 関連動画サムネイル" width="480" height="360" loading="lazy" decoding="async">
            <span class="work-type">MUSIC</span><strong>やなわらばー「いちごいちえ」</strong><em>WATCH</em>
          </a>'''
if profile_anchor not in profile:
    raise SystemExit("profile target not found")
profile_path.write_text(profile.replace(profile_anchor, profile_card, 1), encoding="utf-8")

# 3) Media: add to Selected Video after Sukima Switch.
media_path = Path("media/index.html")
media = media_path.read_text(encoding="utf-8")
media_anchor = '''          <a class="visual-card" href="https://www.youtube.com/watch?v=15566qQHhlw" target="_blank" rel="noopener noreferrer"><div class="visual-card-media"><img src="https://img.youtube.com/vi/15566qQHhlw/hqdefault.jpg" alt="スキマスイッチ 虹のレシピ 関連動画サムネイル" width="480" height="360" loading="lazy" decoding="async"><span class="visual-card-badge">MUSIC</span></div><div class="visual-card-body"><span class="visual-card-kicker">CHOREOGRAPHY / PERFORMANCE</span><h3>スキマスイッチ</h3><span class="visual-card-cta">WATCH VIDEO →</span></div></a>'''
media_card = f'''{media_anchor}
          <a class="visual-card" href="{VIDEO_URL}" target="_blank" rel="noopener noreferrer"><div class="visual-card-media"><img src="{THUMB_URL}" alt="やなわらばー いちごいちえ 関連動画サムネイル" width="480" height="360" loading="lazy" decoding="async"><span class="visual-card-badge">MUSIC</span></div><div class="visual-card-body"><span class="visual-card-kicker">CHOREOGRAPHY / PERFORMANCE</span><h3>やなわらばー「いちごいちえ」</h3><span class="visual-card-cta">WATCH VIDEO →</span></div></a>'''
if media_anchor not in media:
    raise SystemExit("media target not found")
media_path.write_text(media.replace(media_anchor, media_card, 1), encoding="utf-8")

print("Yanawaraba / Ichigo Ichie video added to career, profile, and media.")
