import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from avaliador import Avaliador

CAMINHO = sys.argv[1] if len(sys.argv) > 1 else "jogo.py"

av = Avaliador("Capítulo 6 — Canos em movimento", capitulo=6)
jogo = av.carregar(CAMINHO)

if av.checar("a função update() existe e o cano existe",
             lambda: callable(getattr(jogo, "update", None)) and hasattr(jogo, "cano"),
             dica="O cano do capítulo 5 e o update do capítulo 4 precisam\ncontinuar no arquivo!"):
    x_inicial = jogo.cano.x
    av.rodar_frames(30)  # meio segundo
    if av.checar("o cano anda para a esquerda",
                 lambda: jogo.cano.x < x_inicial,
                 dica="Dentro do update: cano.x = cano.x - 3\n"
                      "(subtrair no x = andar para a esquerda)"):
        jogo.cano.x = -49  # cano quase saindo da tela
        av.rodar_frames(10)
        av.checar("o cano volta para a direita depois de sair da tela",
                  lambda: jogo.cano.x > 300,
                  dica="Ainda no update, use:\n"
                       "    if cano.x < -50:\n"
                       "        cano.x = 450\n"
                       "(com o if DENTRO do update, com recuo)")

    # regressão: a gravidade do capítulo 4 continua funcionando
    y_antes = jogo.bird.y
    av.rodar_frames(20)
    av.checar("o pássaro continua caindo (cap. 4 não quebrou)",
              lambda: jogo.bird.y > y_antes,
              dica="Não apague as linhas da gravidade no update!\n"
                   "As linhas novas do cano entram DEPOIS delas.")

av.relatorio()
