import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from avaliador import Avaliador

CAMINHO = sys.argv[1] if len(sys.argv) > 1 else "jogo.py"

av = Avaliador("Capítulo 1 — Acendendo a tela", capitulo=1)
jogo = av.carregar(CAMINHO)

if av.checar("a largura da janela (WIDTH) está definida",
             lambda: isinstance(getattr(jogo, "WIDTH", None), (int, float))
             and jogo.WIDTH > 0,
             dica="Escreva lá em cima do arquivo: WIDTH = 400"):
    if av.checar("a altura da janela (HEIGHT) está definida",
                 lambda: isinstance(getattr(jogo, "HEIGHT", None), (int, float))
                 and jogo.HEIGHT > 0,
                 dica="Escreva lá em cima do arquivo: HEIGHT = 600"):
        if av.checar("a função draw() existe",
                     lambda: callable(getattr(jogo, "draw", None)),
                     dica="Crie a função escrevendo: def draw():"):
            if av.desenhar():
                av.checar("o fundo da tela foi pintado (não está preto)",
                          lambda: av.pixel(10, 10) != (0, 0, 0),
                          dica="Dentro do draw(), use screen.fill((135, 206, 235))\n"
                               "Lembre dos 4 espaços no começo da linha!")

av.relatorio()
