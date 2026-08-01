import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from avaliador import Avaliador

CAMINHO = sys.argv[1] if len(sys.argv) > 1 else "jogo.py"

av = Avaliador("Capítulo 3 — A gravidade", capitulo=3)
jogo = av.carregar(CAMINHO)

# O capítulo 2 precisa continuar funcionando
if hasattr(jogo, "bird") and callable(getattr(jogo, "draw", None)) and av.desenhar():
    cor_fundo = av.pixel(5, 5)
    av.checar("o pássaro ainda aparece na tela (cap. 2 não quebrou)",
              lambda: av.pixel(jogo.bird.x, jogo.bird.y) != cor_fundo,
              dica="Não apague o código do capítulo anterior!\n"
                   "O draw() precisa continuar com screen.fill() e bird.draw().")

if av.checar("a função update() existe",
             lambda: callable(getattr(jogo, "update", None)),
             dica="Crie lá embaixo: def update():"):
    y_inicial = jogo.bird.y
    av.rodar_frames(60)  # 1 segundo de jogo
    if av.checar("o pássaro cai sozinho depois de 1 segundo",
                 lambda: jogo.bird.y > y_inicial + 3,
                 dica="Dentro do update, escreva: bird.y = bird.y + 3\n"
                      "(com 4 espaços no começo da linha!)"):
        y_agora = jogo.bird.y
        av.rodar_frames(60)  # mais 1 segundo
        av.checar("o pássaro continua caindo (não caiu uma vez só)",
                  lambda: jogo.bird.y > y_agora,
                  dica="A linha bird.y = bird.y + 3 precisa estar DENTRO da função\n"
                       "update, com recuo de 4 espaços. Se ela estiver fora, roda\n"
                       "uma vez só quando o jogo abre — e o pássaro fica parado.")
else:
    pass

av.relatorio()
