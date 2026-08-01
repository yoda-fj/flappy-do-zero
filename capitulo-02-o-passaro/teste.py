import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from avaliador import Avaliador, Actor

CAMINHO = sys.argv[1] if len(sys.argv) > 1 else "jogo.py"

av = Avaliador("Capítulo 2 — O pássaro aparece", capitulo=2)
jogo = av.carregar(CAMINHO)

if av.checar("a variável bird existe",
             lambda: hasattr(jogo, "bird"),
             dica='Crie lá em cima: bird = Actor("bird", (100, 300))'):
    if av.checar("bird é um personagem (Actor) com imagem",
                 lambda: isinstance(jogo.bird, Actor),
                 dica='Use a palavra Actor: bird = Actor("bird", (100, 300))'):
        if av.checar("o pássaro começa dentro da tela",
                     lambda: 0 < jogo.bird.x < getattr(jogo, "WIDTH", 800)
                     and 0 < jogo.bird.y < getattr(jogo, "HEIGHT", 600),
                     dica="A posição (x, y) precisa ser menor que WIDTH e HEIGHT.\n"
                          "Ex.: (100, 300) fica bem no meio da tela."):
            if av.desenhar():
                cor_fundo = av.pixel(5, 5)
                av.checar("o pássaro aparece desenhado na tela",
                          lambda: av.pixel(jogo.bird.x, jogo.bird.y) != cor_fundo,
                          dica="Dentro do draw(), chame bird.draw() DEPOIS do\n"
                               "screen.fill(). A ordem importa: primeiro o fundo,\n"
                               "depois o pássaro!")

av.relatorio()
