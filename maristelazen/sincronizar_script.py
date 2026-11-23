"""Copia o <script id="msz-script"> de uma página para as outras, preservando o BLOCK_ID de cada uma.

Uso (na pasta maristelazen):
    python3 sincronizar_script.py areas.html

Edite o script em UMA página (a "origem") e rode este comando para replicar nas demais.
"""
import re
import sys
from pathlib import Path

PAGES = ['home.html', 'sobre.html', 'areas.html', 'procedimentos.html']
SCRIPT = re.compile(r'<script id="msz-script">.*?</script>', re.S)
BLOCK = re.compile(r"var BLOCK_ID = '([^']*)';")

here = Path(__file__).resolve().parent
origem = sys.argv[1] if len(sys.argv) > 1 else 'areas.html'
src = SCRIPT.search((here / origem).read_text(encoding='utf-8')).group(0)

for name in PAGES:
    if name == origem:
        continue
    f = here / name
    txt = f.read_text(encoding='utf-8')
    block_id = BLOCK.search(txt).group(1)
    new = BLOCK.sub("var BLOCK_ID = '%s';" % block_id, src, count=1)
    txt, n = SCRIPT.subn(lambda m: new, txt, count=1)
    assert n == 1, name
    f.write_text(txt, encoding='utf-8')
    print('atualizado:', name, '(BLOCK_ID=%r)' % block_id)
