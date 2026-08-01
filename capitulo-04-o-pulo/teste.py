import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from avaliador import Avaliador

CAMINHO = sys.argv[1] if len(sys.argv) > 1 else "jogo.py"

av = Avaliador("Capítulo 4 — O pulo", capitulo=4)
jogo = av.carregar(CAMINHO)

if av.checar("a função update() existe",
             lambda: callable(getattr(jogo, "update", None)),
             dica="Crie: def update():"):
    y_inicial = jogo.bird.y
    av.rodar_frames(30)  # meio segundo de queda
    if av.checar("a gravidade derruba o pássaro",
                 lambda: jogo.bird.y > y_inicial,
                 dica="No update, a velocidade precisa aumentar com a gravidade\n"
                      "e depois somar na posição: bird.y = bird.y + velocidade"):
        if av.checar("a função on_key_down() existe",
                     lambda: callable(getattr(jogo, "on_key_down", None)),
                     dica="Crie: def on_key_down(key):"):
            av.apertar_espaco()
            y_antes_do_pulo = jogo.bird.y
            av.rodar_frames(6)
            if av.checar("apertar ESPAÇO faz o pássaro subir",
                         lambda: jogo.bird.y < y_antes_do_pulo,
                         dica="Dentro de on_key_down, use:\n"
                              "    if key == keys.SPACE:\n"
                              "        velocidade = -8\n"
                              "(negativo = para cima! E não esqueça do global velocidade)"):
                y_no_topo = jogo.bird.y
                av.rodar_frames(90)  # 1,5 segundos sem apertar nada
                av.checar("a gravidade volta a puxar depois do pulo",
                          lambda: jogo.bird.y > y_no_topo,
                          dica="A gravidade precisa agir em TODO frame dentro do\n"
                               "update, não só quando a tecla está solta. Revise a\n"
                               "ordem do update: primeiro velocidade + gravidade,\n"
                               "depois bird.y.")

av.relatorio()
