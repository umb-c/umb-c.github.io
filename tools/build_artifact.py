#!/usr/bin/env python3
"""Genera la versione a file singolo (foto incorporata) per l'anteprima come Artifact.

Uso:  python3 tools/build_artifact.py [percorso_output]
Legge ../index.html e ../assets/head-art.png. Non modifica nessun file del sito.
"""
import base64, io, re, sys
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parent.parent
out_path = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "umberto-portfolio.artifact.html"

s = (root / "index.html").read_text(encoding="utf-8")

buf = io.BytesIO()
Image.open(root / "assets" / "head-art.png").convert("L").save(buf, "PNG", optimize=True)
uri = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
assert "art: 'assets/head-art.png'," in s, "CONFIG.art non trovato"
s = s.replace("art: 'assets/head-art.png',", "art: '" + uri + "',")

title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
links = "\n".join(re.findall(r"<link[^>]+fonts[^>]+>", s))
css = re.search(r"<style>(.*?)</style>", s, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", s, re.S).group(1)

out = (f"<title>{title}</title>\n"
       '<meta name="claude:viewport-fit-sides" content="cover">\n'
       f"{links}\n<style>{css}</style>\n{body}")
out_path.write_text(out, encoding="utf-8")
print(f"scritto {out_path} ({len(out)//1024} KB)")
