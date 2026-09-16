from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')
start = text.index('    <section id="career" class="section dark-section">')
end = text.index('    <section id="activities" class="section-shell section">')

section = '''    <section id="career" class="section dark-section">
      <div class="section-shell">
        <p class="section-label">SELECTED CAREER</p>
        <h2>Performance / Choreography</h2>
        <div class="career-grid">
          <article class="home-career-card">
            <a class="home-career-preview" href="https://www.youtube.com/watch?v=op0b7AyaQn0" target="_blank" rel="noopener noreferrer" aria-label="座頭市の関連動画をYouTubeで見る"><img src="https://img.youtube.com/vi/op0b7AyaQn0/hqdefault.jpg" alt="座頭市 関連動画サムネイル" width="480" height="360" loading="lazy" decoding="async"><span class="home-career-preview-label">WATCH VIDEO</span></a>
            <span>FILM</span><h3>「座頭市」</h3><p>出演</p><a class="career-link" href="https://www.youtube.com/watch?v=op0b7AyaQn0" target="_blank" rel="noopener noreferrer">WATCH VIDEO →</a>
          </article>
          <article class="home-career-card">
            <a class="home-career-preview" href="https://www.youtube.com/watch?v=NXozUa1IzRM" target="_blank" rel="noopener noreferrer" aria-label="TAP THE LAST SHOWの関連動画をYouTubeで見る"><img src="https://img.youtube.com/vi/NXozUa1IzRM/hqdefault.jpg" alt="TAP THE LAST SHOW 関連動画サムネイル" width="480" height="360" loading="lazy" decoding="async"><span class="home-career-preview-label">WATCH VIDEO</span></a>
            <span>FILM</span><h3>「TAP THE LAST SHOW」</h3><p>出演</p><a class="career-link" href="https://www.youtube.com/watch?v=NXozUa1IzRM" target="_blank" rel="noopener noreferrer">WATCH VIDEO →</a>
          </article>
          <article class="home-career-card">
            <a class="home-career-preview" href="https://www.youtube.com/watch?v=KNPQqgpgqPQ" target="_blank" rel="noopener noreferrer" aria-label="CITIZEN デュラテクトの関連動画をYouTubeで見る"><img src="https://img.youtube.com/vi/KNPQqgpgqPQ/hqdefault.jpg" alt="CITIZEN デュラテクト 関連動画サムネイル" width="480" height="360" loading="lazy" decoding="async"><span class="home-career-preview-label">WATCH VIDEO</span></a>
            <span>CM</span><h3>CITIZEN デュラテクト</h3><p>振付・出演</p><a class="career-link" href="https://www.youtube.com/watch?v=KNPQqgpgqPQ" target="_blank" rel="noopener noreferrer">WATCH VIDEO →</a>
          </article>
          <article class="home-career-card">
            <a class="home-career-preview" href="https://www.youtube.com/watch?v=3HW_v_vA63w" target="_blank" rel="noopener noreferrer" aria-label="DREAMS COME TRUE 連れてって 連れてっての関連動画をYouTubeで見る"><img src="https://img.youtube.com/vi/3HW_v_vA63w/hqdefault.jpg" alt="DREAMS COME TRUE 連れてって 連れてって 関連動画サムネイル" width="480" height="360" loading="lazy" decoding="async"><span class="home-career-preview-label">WATCH VIDEO</span></a>
            <span>MUSIC</span><h3>DREAMS COME TRUE</h3><p>「連れてって 連れてって」振付・出演</p><a class="career-link" href="https://www.youtube.com/watch?v=3HW_v_vA63w" target="_blank" rel="noopener noreferrer">WATCH VIDEO →</a>
          </article>
          <article class="home-career-card">
            <a class="home-career-preview" href="https://www.youtube.com/watch?v=15566qQHhlw" target="_blank" rel="noopener noreferrer" aria-label="スキマスイッチ 虹のレシピの関連動画をYouTubeで見る"><img src="https://img.youtube.com/vi/15566qQHhlw/hqdefault.jpg" alt="スキマスイッチ 虹のレシピ 関連動画サムネイル" width="480" height="360" loading="lazy" decoding="async"><span class="home-career-preview-label">WATCH VIDEO</span></a>
            <span>MUSIC</span><h3>スキマスイッチ</h3><p>「虹のレシピ」振付・出演</p><a class="career-link" href="https://www.youtube.com/watch?v=15566qQHhlw" target="_blank" rel="noopener noreferrer">WATCH VIDEO →</a>
          </article>
          <article class="home-career-card">
            <a class="home-career-preview" href="https://www.youtube.com/watch?v=RCHe13BrkUo" target="_blank" rel="noopener noreferrer" aria-label="やなわらばー いちごいちえの関連動画をYouTubeで見る"><img src="https://img.youtube.com/vi/RCHe13BrkUo/hqdefault.jpg" alt="やなわらばー いちごいちえ 関連動画サムネイル" width="480" height="360" loading="lazy" decoding="async"><span class="home-career-preview-label">WATCH VIDEO</span></a>
            <span>MUSIC</span><h3>やなわらばー</h3><p>「いちごいちえ」振付・出演</p><a class="career-link" href="https://www.youtube.com/watch?v=RCHe13BrkUo" target="_blank" rel="noopener noreferrer">WATCH VIDEO →</a>
          </article>
          <article class="home-career-card">
            <a class="home-career-preview" href="https://www.facebook.com/photo.php?fbid=1236768718491027&set=pb.100064737308832.-2207520000&type=3" target="_blank" rel="noopener noreferrer" aria-label="Chicago Human Rhythm Projectの関連アーカイブ写真を見る"><img src="assets/images/career/chicago-human-rhythm-project.jpg" alt="Chicago Human Rhythm Project『Rhythm World』公演写真" width="720" height="576" loading="lazy" decoding="async"><span class="home-career-preview-label">VIEW ARCHIVE</span></a>
            <span>OVERSEAS</span><h3>Chicago Human Rhythm Project</h3><p>「Rhythm World」招聘・出演</p><div class="career-links"><a class="career-link" href="https://www.facebook.com/photo.php?fbid=1236768718491027&set=pb.100064737308832.-2207520000&type=3" target="_blank" rel="noopener noreferrer">VIEW ARCHIVE 01 →</a><a class="career-link" href="https://www.facebook.com/photo/?fbid=1236768715157694&set=pb.100064737308832.-2207520000" target="_blank" rel="noopener noreferrer">VIEW ARCHIVE 02 →</a></div>
          </article>
          <article class="home-career-card">
            <div class="home-career-preview home-career-type" aria-hidden="true"><strong>LIVE</strong><small>TOKYO STOMP</small></div>
            <span>LIVE</span><h3>RIP SLYME</h3><p>日本武道館「TOKYO STOMP」出演</p>
          </article>
        </div>
        <div class="hero-actions"><a class="button light" href="career/">Careerを詳しく見る →</a></div>
      </div>
    </section>

'''

text = text[:start] + section + text[end:]
path.write_text(text, encoding='utf-8')
