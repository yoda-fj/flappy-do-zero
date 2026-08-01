import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from avaliador import Avaliador

CAMINHO = sys.argv[1] if len(sys.argv) > 1 else "jogo.py"

av = Avaliador("Capítulo 8 — Pontuação", capitulo=8)
jogo = av.carregar(CAMINHO)

# grade de pontos na área do placar (topo da tela)
def foto_placar():
    return [av.pixel(x, y) for x in range(140, 261, 15) for y in range(15, 86, 10)]

if av.checar("a variável pontos existe e começa em 0",
             lambda: getattr(jogo, "pontos", None) == 0,
             dica="Crie lá em cima: pontos = 0"):
    jogo.cano.x = -49  # cano quase saindo da tela
    av.rodar_frames(10)
    if av.checar("passar do cano soma 1 ponto",
                 lambda: jogo.pontos >= 1,
                 dica="No update, dentro do if que faz o cano voltar, some:\n"
                      "    pontos = pontos + 1\n"
                      "(e adicione pontos no global do update!)"):
        jogo.pontos = 0
        if av.desenhar():
            foto_0 = foto_placar()
            jogo.pontos = 5
            av.desenhar()
            foto_5 = foto_placar()
            av.checar("o placar aparece no topo da tela e muda com os pontos",
                      lambda: foto_0 != foto_5,
                      dica="No draw, por último, use:\n"
                           '    screen.draw.text(str(pontos), (180, 30), fontsize=60, color="white")\n'
                           "Não esqueça do str() em volta de pontos!")

    # regressão: o pulo continua funcionando
    jogo.morreu = False
    av.apertar_espaco()
    y_antes = jogo.bird.y
    av.rodar_frames(6)
    av.checar("o pulo continua funcionando (cap. 4 não quebrou)",
              lambda: jogo.bird.y < y_antes,
              dica="Confira se o on_key_down continua igual ao capítulo 7.")

av.relatorio()
