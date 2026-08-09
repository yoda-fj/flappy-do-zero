import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from avaliador import Avaliador, Actor

CAMINHO = sys.argv[1] if len(sys.argv) > 1 else "jogo.py"

av = Avaliador("Capítulo 13 — O recorde", capitulo=13)
jogo = av.carregar(CAMINHO)


def deixar_jogando():
    """Põe o jogo em modo 'jogando' com o pássaro seguro longe dos canos."""
    jogo.comecou = True
    jogo.morreu = False
    jogo.velocidade = 0
    jogo.bird.y = 150
    jogo.cano_baixo.pos = (800, 590)
    jogo.cano_cima.pos = (800, 10)


def morrer_com(pontos):
    """Simula uma partida inteira que termina com `pontos` pontos."""
    deixar_jogando()
    jogo.pontos = pontos
    jogo.cano_baixo.pos = (jogo.bird.x, jogo.bird.y)
    av.rodar_frames(3)


if av.checar("existe a variável recorde, começando em 0",
             lambda: getattr(jogo, "recorde", None) == 0,
             dica="Crie lá em cima, junto com os pontos:\n"
                  "    recorde = 0\n"
                  "(e a bandeira: novo_recorde = False)"):
    # partida 1: morre com 3 pontos -> recorde vira 3
    morrer_com(3)
    if av.checar("ao morrer, a pontuação vira o novo recorde",
                 lambda: jogo.morreu is True and jogo.recorde == 3,
                 dica="A comparação acontece na hora da morte, no if da colisão:\n"
                      "    morreu = True\n"
                      "    if pontos > recorde:\n"
                      "        recorde = pontos\n"
                      "(lembre do recorde e novo_recorde no global do update!)"):
        # recomeça: pontos zeram, recorde NÃO
        av.apertar_espaco()
        if av.checar("jogar de novo zera os pontos mas o recorde SOBREVIVE",
                     lambda: jogo.pontos == 0 and jogo.morreu is False
                     and jogo.recorde == 3,
                     dica="O recomecar() zera os pontos, mas NUNCA o recorde —\n"
                          "senão ele viraria 'pontuação anterior', não recorde!\n"
                          "A única coisa nova no recomecar é: novo_recorde = False"):
            # partida 2: morre com 1 ponto -> recorde não pode cair
            morrer_com(1)
            if av.checar("recorde NUNCA desce (1 ponto não apaga o 3)",
                         lambda: jogo.recorde == 3,
                         dica="Faltou a comparação! Só troca o recorde se for MAIOR:\n"
                              "    if pontos > recorde:\n"
                              "        recorde = pontos"):
                # partida 3: morre com 7 -> recorde sobe E tem festa na tela
                av.apertar_espaco()  # recomeça
                morrer_com(7)
                if av.checar("bater o recorde de novo atualiza para 7",
                             lambda: jogo.recorde == 7,
                             dica="Se o recorde parou no 3, confira o if: é > (maior),\n"
                                  "não >= nem <. E ele precisa estar DENTRO do if da colisão."):
                    av.desenhar()
                    amarelos = 0
                    for x in range(60, 340, 3):
                        for y in range(270, 330, 3):
                            r, g, b = av.pixel(x, y)
                            if r > 170 and g > 170 and b < 130:
                                amarelos += 1
                    av.checar("a tela de game over COMEMORA o novo recorde",
                              amarelos > 20,
                              dica="Quando a bandeira novo_recorde estiver True, escreva\n"
                                   "a festa em AMARELO no draw, entre o GAME OVER e o\n"
                                   "'Aperte ESPACO':\n"
                                   "    if novo_recorde:\n"
                                   '        screen.draw.text("NOVO RECORDE!", center=(200, 300), fontsize=40, color="yellow")')

        # regressão: depois de tudo isso, o jogo ainda joga normal
        av.apertar_espaco()
        if av.checar("depois de várias partidas, o jogo continua funcionando",
                     lambda: jogo.pontos == 0 and jogo.morreu is False
                     and jogo.comecou is True,
                     dica="O recomecar precisa zerar pontos e morreu e ligar o comecou\n"
                          "(capítulo 11). O recorde fica fora dessa zerada!"):
            av.apertar_espaco()
            y_antes = jogo.bird.y
            av.rodar_frames(6)
            av.checar("o pulo continua funcionando (cap. 4 não quebrou)",
                      lambda: jogo.bird.y < y_antes,
                      dica="Confira o terceiro emprego do ESPAÇO: velocidade = -8.")

av.relatorio()
