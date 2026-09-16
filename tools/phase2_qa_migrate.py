from pathlib import Path

PAGES = [
    Path('profile/index.html'),
    Path('career/index.html'),
    Path('activities/index.html'),
    Path('projects/index.html'),
    Path('media/index.html'),
    Path('contact/index.html'),
]

for path in PAGES:
    text = path.read_text(encoding='utf-8')
    if 'class="skip-link"' not in text:
        text = text.replace('<body>', '<body>\n  <a class="skip-link" href="#main">本文へ移動</a>', 1)
    if '<main id="main">' not in text:
        text = text.replace('<main>', '<main id="main">', 1)
    path.write_text(text, encoding='utf-8')

# Projects did not yet carry the same OGP metadata baseline as other primary pages.
projects = Path('projects/index.html')
text = projects.read_text(encoding='utf-8')
if '<meta property="og:type"' not in text:
    marker = '  <link rel="stylesheet" href="../assets/css/style.css">'
    og = '''  <meta property="og:type" content="website">\n  <meta property="og:locale" content="ja_JP">\n  <meta property="og:title" content="Projects / Activities | 古庄里好 Noritaka Furusho">\n  <meta property="og:description" content="古庄里好が運営・制作・参加する公開プロジェクト、教育、メディア、サービスへの公式ディレクトリ。">\n  <meta property="og:url" content="https://noritap.github.io/furusho-official/projects/">\n  <meta property="og:image" content="https://noritap.github.io/furusho-official/assets/images/furusho-profile-main.jpg">\n  <meta property="og:image:alt" content="古庄里好 Official Website">\n  <meta name="twitter:card" content="summary_large_image">\n'''
    text = text.replace(marker, og + marker, 1)
projects.write_text(text, encoding='utf-8')
