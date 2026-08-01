import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from avaliador import Avaliador

CAMINHO = sys.argv[1] if len(sys.argv) > 1 else "jogo.py"

av = Avaliador("Capítulo 7 — Colisão", capitulo=7)
jogo = av.carregar(CAMINHO)

if av.checar("a variável morreu existe e começa como False",
             lambda: getattr(jogo, "morreu", None) is False,
             dica="Crie lá em cima: morreu = False"):
    av.rodar_frames(15)  # jogo rolando, cano longe do pássaro
    if av.checar("sem encostar no cano, o jogo continua (morreu fica False)",
                 lambda: jogo.morreu is False,
                 dica="A variável morreu só pode virar True quando houver colisão.\n"
                      "Confira se o if está certo: if bird.colliderect(cano):"):
        # força a colisão: joga o cano em cima do pássaro
        jogo.cano.x = jogo.bird.x
        av.rodar_frames(3)
        if av.checar("encostar no cano mata o pássaro (morreu vira True)",
                     lambda: jogo.morreu is True,
                     dica="Dentro do update, use:\n"
                          "    if bird.colliderect(cano):\n"
                          "        morreu = True\n"
                          "(e não esqueça de adicionar morreu no global!)"):
            y_parado = jogo.bird.y
            x_parado = jogo.cano.x
            av.rodar_frames(30)
            av.checar("depois de morrer, o jogo congela",
                      lambda: jogo.bird.y == y_parado and jogo.cano.x == x_parado,
                      dica="Todo o miolo do update precisa ficar dentro de:\n"
                           "    if not morreu:\n"
                           "Assim, quando morreu é True, nada mais se move.")

av.relatorio()
