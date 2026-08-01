import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from avaliador import Avaliador, Actor

CAMINHO = sys.argv[1] if len(sys.argv) > 1 else "jogo.py"

av = Avaliador("Capítulo 5 — O primeiro cano", capitulo=5)
jogo = av.carregar(CAMINHO)

if av.checar("a variável cano existe",
             lambda: hasattr(jogo, "cano"),
             dica='Crie lá em cima: cano = Actor("pipe", (350, 300))'):
    if av.checar("cano é um Actor com a imagem do cano",
                 lambda: isinstance(jogo.cano, Actor),
                 dica='Use a palavra Actor: cano = Actor("pipe", (350, 300))'):
        if av.checar("o cano está à direita do pássaro",
                     lambda: jogo.cano.x > jogo.bird.x,
                     dica="O x do cano precisa ser maior que o x do pássaro (100).\n"
                          "Ex.: (350, 300)."):
            if av.desenhar():
                cor_fundo = av.pixel(5, 5)
                av.checar("o cano aparece desenhado na tela",
                          lambda: av.pixel(jogo.cano.x, jogo.cano.y) != cor_fundo,
                          dica="Dentro do draw(), chame cano.draw() DEPOIS do\n"
                               "screen.fill() e ANTES do bird.draw().")
                av.checar("o pássaro continua aparecendo (cap. 2 não quebrou)",
                          lambda: av.pixel(jogo.bird.x, jogo.bird.y) != cor_fundo,
                          dica="Não apague o bird.draw()! Ele continua no draw(),\n"
                               "depois do cano.draw().")

av.relatorio()
