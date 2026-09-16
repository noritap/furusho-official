from pathlib import Path
import re

pages = [
    Path('index.html'),
    Path('profile/index.html'),
    Path('career/index.html'),
    Path('activities/index.html'),
    Path('projects/index.html'),
    Path('media/index.html'),
    Path('contact/index.html'),
]

for path in pages:
    text = path.read_text(encoding='utf-8')
    root = path == Path('index.html')
    prefix = '' if root else '../'

    if 'nf-tap-icon.png' not in text:
        marker = '  <meta name="theme-color" content="#111111">'
        insert = (
            marker + '\n'
            f'  <link rel="icon" type="image/png" href="{prefix}assets/icons/nf-tap-icon.png">\n'
            f'  <link rel="apple-touch-icon" href="{prefix}assets/icons/nf-tap-icon.png">\n'
            f'  <link rel="manifest" href="{prefix}site.webmanifest">\n'
            '  <meta name="apple-mobile-web-app-title" content="NF TAP">'
        )
        text = text.replace(marker, insert, 1)

    pattern = re.compile(
        r'(<a class="brand"[^>]*>)\s*'
        r'<span class="brand-ja">古庄里好</span>\s*'
        r'<span class="brand-en">Noritaka Furusho</span>\s*'
        r'</a>'
    )
    replacement = (
        r'\1\n'
        f'      <img class="brand-mark" src="{prefix}assets/icons/nf-tap-icon.png" alt="" width="38" height="38" aria-hidden="true">\n'
        '      <span class="brand-copy"><span class="brand-ja">古庄里好</span><span class="brand-en">Noritaka Furusho</span></span>\n'
        '    </a>'
    )
    text = pattern.sub(replacement, text, count=1)
    path.write_text(text, encoding='utf-8')

css_path = Path('assets/css/style.css')
css = css_path.read_text(encoding='utf-8')
marker = '/* NF TAP brand mark */'
if marker not in css:
    css += '''\n\n/* NF TAP brand mark */\n.brand {\n  flex-direction: row;\n  align-items: center;\n  gap: 10px;\n}\n.brand-mark {\n  width: 38px;\n  height: 38px;\n  display: block;\n  flex: 0 0 38px;\n  object-fit: cover;\n  border-radius: 2px;\n}\n.brand-copy {\n  display: flex;\n  flex-direction: column;\n  line-height: 1.1;\n}\n@media (max-width: 720px) {\n  .brand { gap: 8px; }\n  .brand-mark { width: 32px; height: 32px; flex-basis: 32px; }\n}\n'''
css_path.write_text(css, encoding='utf-8')
