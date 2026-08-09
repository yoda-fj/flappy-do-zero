import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from avaliador import Avaliador, Actor

CAMINHO = sys.argv[1] if len(sys.argv) > 1 else "jogo.py"

av = Avaliador("Capítulo 12 — Cenário com parallax", capitulo=12)
jogo = av.carregar(CAMINHO)


def atores_com(imagem):
    return [a for a in vars(jogo).values()
            if isinstance(a, Actor) and getattr(a, "image", "") == imagem]


def deixar_jogando():
    """Põe o jogo em modo 'jogando' com o pássaro seguro longe dos canos."""
    jogo.comecou = True
    jogo.morreu = False
    jogo.velocidade = 0
    jogo.bird.y = 150
    jogo.cano_baixo.pos = (800, 590)
    jogo.cano_cima.pos = (800, 10)


if av.checar("existem DUAS gramas e DUAS nuvens (imagens grass e cloud)",
             lambda: len(atores_com("grass")) >= 2 and len(atores_com("cloud")) >= 2,
             dica="Crie quatro atores lá em cima:\n"
                  '    grama1 = Actor("grass", (200, 570))\n'
                  '    grama2 = Actor("grass", (600, 570))\n'
                  '    nuvem1 = Actor("cloud", (120, 90))\n'
                  '    nuvem2 = Actor("cloud", (340, 160))\n'
                  "(as imagens grass.png e cloud.png já estão na pasta images/)"):
    gramas = atores_com("grass")
    nuvens = atores_com("cloud")

    if av.checar("a grama forma o CHÃO do jogo (lá embaixo)",
                 lambda: any(g.y > 400 for g in gramas),
                 dica="A grama é o chão: y perto de 570. Se ela flutuar no meio\n"
                      "da tela, o pássaro vai parecer que voa em cima de nada!"):
        deixar_jogando()
        x_grama = gramas[0].x
        x_nuvem = nuvens[0].x
        av.rodar_frames(30)
        andou_grama = x_grama - gramas[0].x
        andou_nuvem = x_nuvem - nuvens[0].x
        if av.checar("PARALLAX: a grama anda mais rápido que a nuvem",
                     lambda: andou_grama > 0 and 0 < andou_nuvem < andou_grama,
                     dica="Parallax = velocidades diferentes! A grama anda com os\n"
                          "canos (-3 por frame) e a nuvem bem devagar (-1).\n"
                          "As duas andam DENTRO do update, para a esquerda (-)."):
            # teletransporte da grama
            deixar_jogando()
            gramas[0].x = -199
            av.rodar_frames(3)
            if av.checar("a grama que sai da tela volta para a direita (chão infinito)",
                         lambda: gramas[0].x > 300,
                         dica="É o teletransporte do capítulo 6! A grama tem 400 de\n"
                              "largura: some em x < -200 e volta em 600, atrás da outra:\n"
                              "    if grama1.x < -200:\n"
                              "        grama1.x = 600"):
                # teletransporte da nuvem
                deixar_jogando()
                nuvens[0].x = -69
                av.rodar_frames(3)
                av.checar("a nuvem que sai da tela também volta para a direita",
                          lambda: nuvens[0].x > 400,
                          dica="A nuvem tem 140 de largura: some em x < -70 e volta\n"
                               "mais à direita, em 470, para entrar devagarinho:\n"
                               "    if nuvem1.x < -70:\n"
                               "        nuvem1.x = 470")

            # a grama aparece de verdade no pé da tela?
            gramas[0].x = 200
            gramas[1].x = 600
            av.desenhar()
            r, g, b = av.pixel(200, 595)
            av.checar("a grama aparece desenhada no pé da tela",
                      g > r and g > b,
                      dica="Lembrou de chamar grama1.draw() e grama2.draw() no draw()?\n"
                           "Desenhe DEPOIS dos canos: assim a grama cobre o pé deles,\n"
                           "como se os canos estivessem plantados no chão.")

        # regressão: pontos, colisão e recomeço continuam valendo
        deixar_jogando()
        jogo.pontos = 0
        jogo.cano_baixo.pos = (-49, 590)
        jogo.cano_cima.pos = (-49, 10)
        av.rodar_frames(3)
        if av.checar("passar do cano continua somando ponto (cap. 8 não quebrou)",
                     lambda: jogo.pontos >= 1,
                     dica="Confira se o if do cano saindo da tela continua no update:\n"
                          "    if cano_baixo.x < -50:\n"
                          "        sortear_canos(450)\n"
                          "        pontos = pontos + 1"):
            deixar_jogando()
            jogo.cano_baixo.pos = (jogo.bird.x, jogo.bird.y)
            av.rodar_frames(3)
            if av.checar("bater no cano continua matando (cap. 7 não quebrou)",
                         lambda: jogo.morreu is True,
                         dica="O if da colisão testa os DOIS canos com or — não mexa nele!"):
                av.apertar_espaco()
                av.checar("ESPAÇO depois de perder joga de novo (cap. 11 não quebrou)",
                          lambda: jogo.morreu is False and jogo.pontos == 0
                          and jogo.comecou is True,
                          dica="O recomecar() precisa zerar tudo E ligar o comecou.\n"
                               "Repare que ele também deve devolver as gramas para\n"
                               "as posições iniciais (200 e 600)!")

av.relatorio()
