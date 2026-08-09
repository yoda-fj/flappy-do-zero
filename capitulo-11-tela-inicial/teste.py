import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from avaliador import Avaliador, Actor

CAMINHO = sys.argv[1] if len(sys.argv) > 1 else "jogo.py"

av = Avaliador("Capítulo 11 — A tela inicial", capitulo=11)
jogo = av.carregar(CAMINHO)

CEU = (135, 206, 235)

if av.checar("existe a variável comecou, começando em False",
             lambda: getattr(jogo, "comecou", None) is False,
             dica="Crie lá em cima, perto do morreu = False:\n"
                  "    comecou = False\n"
                  "(False com F maiúsculo!)"):
    # o mundo fica congelado antes do começo
    y_inicial = jogo.bird.y
    x_inicial = jogo.cano_baixo.x
    av.rodar_frames(60)
    if av.checar("antes de começar, o mundo fica PARADO (tela inicial)",
                 lambda: jogo.bird.y == y_inicial and jogo.cano_baixo.x == x_inicial,
                 dica="O update só pode mexer no jogo quando começou:\n"
                      "    if comecou and not morreu:\n"
                      "(o and junta as duas condições)"):
        # o título aparece na tela inicial?
        av.desenhar()
        diferentes = 0
        for x in range(40, 300, 4):
            for y in range(120, 260, 4):
                if av.pixel(x, y) != CEU:
                    diferentes += 1
        av.checar("a tela inicial mostra o título do jogo",
                  diferentes > 100,
                  dica="No draw, quando o jogo NÃO começou, escreva o título:\n"
                       "    if not comecou:\n"
                       '        screen.draw.text("FLAPPY DO ZERO", center=(200, 200), fontsize=50, color="white")')

        # ESPAÇO começa o jogo
        av.apertar_espaco()
        if av.checar("apertar ESPAÇO começa o jogo",
                     lambda: jogo.comecou is True,
                     dica="No on_key_down, o ESPAÇO tem três empregos:\n"
                          "    if not comecou:\n"
                          "        comecou = True\n"
                          "Não esqueça do comecou no global!"):
            av.rodar_frames(10)
            if av.checar("depois de começar, a gravidade volta a derrubar o pássaro",
                         lambda: jogo.bird.y > y_inicial,
                         dica="Se o comecou virou True mas o pássaro não cai, o\n"
                              "problema está no if do update: if comecou and not morreu:"):
                # pulo continua funcionando
                av.apertar_espaco()
                y_antes = jogo.bird.y
                av.rodar_frames(6)
                av.checar("o pulo continua funcionando (cap. 4 não quebrou)",
                          lambda: jogo.bird.y < y_antes,
                          dica="O terceiro emprego do ESPAÇO é pular:\n"
                               "    else:\n"
                               "        velocidade = -8")

        # ESPAÇO depois do game over joga de novo
        jogo.comecou = True
        jogo.morreu = False
        jogo.cano_baixo.pos = (jogo.bird.x, jogo.bird.y)
        av.rodar_frames(3)
        if av.checar("bater no cano ainda mata (cap. 7 não quebrou)",
                     lambda: jogo.morreu is True,
                     dica="Confira o if da colisão no update, com os DOIS canos:\n"
                          "    if bird.colliderect(cano_baixo) or bird.colliderect(cano_cima):"):
            jogo.pontos = 7
            av.apertar_espaco()
            av.checar("apertar ESPAÇO depois de perder joga DE NOVO",
                      lambda: jogo.morreu is False and jogo.pontos == 0
                      and jogo.comecou is True,
                      dica="O segundo emprego do ESPAÇO:\n"
                           "    elif morreu:\n"
                           "        recomecar()\n"
                           "E dentro do recomecar, ligue o comecou = True (com global!).")

        # R continua funcionando
        jogo.comecou = True
        jogo.morreu = True
        jogo.pontos = 5
        av.apertar(jogo.keys.R)
        av.checar("apertar R continua recomeçando (cap. 9 não quebrou)",
                  lambda: jogo.morreu is False and jogo.pontos == 0,
                  dica="Mantenha no on_key_down:\n"
                       "    if key == keys.R:\n"
                       "        recomecar()")

av.relatorio()
