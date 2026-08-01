"""Roda o avaliador contra o gabarito de todos os capítulos.

Uso:  python ferramentas/testar_tudo.py
Serve para garantir que mudanças no avaliador.py não quebraram nenhum capítulo.
"""
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

capitulos = sorted(
    d for d in os.listdir(RAIZ)
    if d.startswith("capitulo-") and os.path.isdir(os.path.join(RAIZ, d))
)

falhas = 0
for cap in capitulos:
    pasta = os.path.join(RAIZ, cap)
    if not os.path.exists(os.path.join(pasta, "gabarito.py")):
        continue
    r = subprocess.run(
        [sys.executable, "teste.py", "gabarito.py"],
        cwd=pasta, capture_output=True, text=True,
    )
    status = "✅" if r.returncode == 0 else "❌"
    print(f"{status} {cap} (exit={r.returncode})")
    if r.returncode != 0:
        falhas += 1
        print(r.stdout)
        print(r.stderr)

print()
print("TUDO PASSANDO 🎉" if falhas == 0 else f"{falhas} capítulo(s) com problema")
sys.exit(1 if falhas else 0)
