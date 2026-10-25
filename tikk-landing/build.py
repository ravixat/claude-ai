"""Inline fonts and poster images into src.html -> index.html (single self-contained file)."""
import base64, pathlib
d = pathlib.Path(__file__).parent
b64 = lambda p: base64.b64encode((d / 'assets' / p).read_bytes()).decode()
s = (d / 'src.html').read_text()
for k, f in {'FONT_LATIN': 'archivo-latin.woff2', 'FONT_LATIN_EXT': 'archivo-latin-ext.woff2',
             'IMG_TATVA': 'tatva.jpg', 'IMG_NAGRI': 'nagri.jpg', 'IMG_MANDLI': 'mandli.jpg'}.items():
    s = s.replace('{{%s}}' % k, b64(f))
(d / 'fragment.html').write_text(s)  # what gets published (the host adds the document skeleton)
head = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
(d / 'index.html').write_text(head + s + '</html>')
print(len(s) // 1024, 'KB')
