import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from avaliador import Avaliador

CAMINHO = sys.argv[1] if len(sys.argv) > 1 else "jogo.py"

av = Avaliador("Capítulo 9 — Game over e recomeço", capitulo=9)
jogo = av.carregar(CAMINHO)

# estado inicial, para comparar depois do recomeço
y_inicial = jogo.bird.y
x_inicial = jogo.cano.x

# grade de pontos no centro da tela (onde o GAME OVER aparece)
def foto_centro():
    return [av.pixel(x, y) for x in range(100, 301, 20) for y in range(210, 341, 15)]

if av.checar("a função recomecar() existe",
             lambda: callable(getattr(jogo, "recomecar", None)),
             dica="Crie: def recomecar(): — a lição mostra o que vai dentro"):
    # deixa o pássaro cair bastante antes de morrer: assim a velocidade
    # acumula e o teste pega quem esqueceu de zerá-la no recomecar()
    av.rodar_frames(40)
    jogo.cano.pos = jogo.bird.pos  # colisão garantida
    av.rodar_frames(3)
    if av.checar("a colisão continua funcionando (cap. 7 não quebrou)",
                 lambda: jogo.morreu is True,
                 dica="Confira o if da colisão no update (capítulo 7)."):
        # compara a MESMA cena congelada com morreu False e True:
        # a única diferença possível é o aviso de GAME OVER
        jogo.morreu = False
        av.desenhar()
        foto_sem_aviso = foto_centro()
        jogo.morreu = True
        av.desenhar()
        foto_com_aviso = foto_centro()
        if av.checar("o aviso de GAME OVER aparece na tela quando morre",
                     lambda: foto_com_aviso != foto_sem_aviso,
                     dica="No draw, no final, use um if:\n"
                          "    if morreu:\n"
                          '        screen.draw.text("GAME OVER", center=(200, 250), ...)'):
            # recomeça com a tecla R
            av.apertar(jogo.keys.R)
            if av.checar("apertar R recomeça o jogo (morreu volta a False)",
                         lambda: jogo.morreu is False,
                         dica="No on_key_down, adicione:\n"
                              "    if key == keys.R:\n"
                              "        recomecar()"):
                av.checar("o recomeço zera tudo (pássaro, cano e pontos)",
                          lambda: (jogo.bird.y == y_inicial
                                   and jogo.cano.x == x_inicial
                                   and jogo.pontos == 0),
                          dica="Dentro de recomecar(), coloque tudo de volta:\n"
                               "bird.y = 300, cano.x = 350, pontos = 0, morreu = False")
                av.rodar_frames(10)
                av.checar("a velocidade também é zerada (não renasce despencando)",
                          lambda: jogo.bird.y < y_inicial + 40,
                          dica="Faltou zerar a velocidade! Adicione velocidade = 0\n"
                               "dentro de recomecar() (e ela no global da função).")

av.relatorio()
