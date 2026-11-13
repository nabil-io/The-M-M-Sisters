"""Build a single-file, fully portable version of the site.

Usage:  python build-standalone.py
Output: standalone.html (all photos and icons embedded as data URIs)
"""
import base64
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "index.html")
ASSETS = os.path.join(ROOT, "assets")
OUT = os.path.join(ROOT, "standalone.html")

MIME = {
    ".webp": "image/webp",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
}

html = open(SRC, encoding="utf-8").read()

# References that cannot work inside a single shared file.
html = html.replace('<link rel="manifest" href="site.webmanifest">\n', "")

inlined = 0
for name in sorted(os.listdir(ASSETS)):
    if name == "og-cover.jpg":
        continue  # keep the social preview as a normal path
    rel = "assets/" + name
    if rel not in html:
        continue
    with open(os.path.join(ASSETS, name), "rb") as fh:
        data = base64.b64encode(fh.read()).decode("ascii")
    ext = os.path.splitext(name)[1].lower()
    html = html.replace(rel, "data:%s;base64,%s" % (MIME.get(ext, "application/octet-stream"), data))
    inlined += 1

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(html)

print("wrote %s (%.0f KB, %d assets inlined)" % (OUT, os.path.getsize(OUT) / 1024, inlined))
