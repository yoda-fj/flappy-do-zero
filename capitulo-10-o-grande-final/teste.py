import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from avaliador import Avaliador, Actor

CAMINHO = sys.argv[1] if len(sys.argv) > 1 else "jogo.py"

av = Avaliador("Capítulo 10 — O grande final", capitulo=10)
jogo = av.carregar(CAMINHO)

if av.checar("existem DOIS canos: cano_baixo e cano_cima",
             lambda: isinstance(getattr(jogo, "cano_baixo", None), Actor)
             and isinstance(getattr(jogo, "cano_cima", None), Actor),
             dica="Crie os dois com a mesma imagem:\n"
                  '    cano_baixo = Actor("pipe", (350, 590))\n'
                  '    cano_cima = Actor("pipe", (350, 10))\n'
                  "    cano_cima.angle = 180"):
    if av.checar("existe um buraco entre os canos (100 a 260 pixels)",
                 lambda: 100 <= (jogo.cano_baixo.top - jogo.cano_cima.bottom) <= 260,
                 dica="O buraco é a distância entre a base do cano de cima e o\n"
                      "topo do cano de baixo. Use a constante BURACO = 180 e a\n"
                      "matemática da lição para posicionar os dois."):
        # o buraco muda de altura quando o cano volta? (3 tentativas)
        alturas = set()
        for _ in range(3):
            jogo.cano_baixo.x = -49
            jogo.cano_cima.x = -49
            av.rodar_frames(3)
            alturas.add(round(jogo.cano_baixo.y))
        av.checar("o buraco muda de altura a cada cano (sorteio)",
                  lambda: len(alturas) > 1,
                  dica="Use random.randint(230, 370) para sortear o centro do\n"
                       "buraco dentro de sortear_canos(). Não esqueça do import random!")
        av.checar("passar do cano continua somando ponto (cap. 8 não quebrou)",
                  lambda: jogo.pontos >= 1,
                  dica="No update, quando o cano voltar: sortear_canos(450) e\n"
                       "pontos = pontos + 1.")

        # colisão com os DOIS canos
        jogo.morreu = False
        jogo.cano_baixo.pos = (jogo.bird.x, jogo.bird.y)
        av.rodar_frames(3)
        bateu_baixo = jogo.morreu is True
        jogo.morreu = False
        jogo.cano_baixo.pos = (450, 590)  # tira o de baixo da frente
        jogo.cano_cima.pos = (jogo.bird.x, jogo.bird.y)
        av.rodar_frames(3)
        bateu_cima = jogo.morreu is True
        av.checar("bater em QUALQUER um dos dois canos mata",
                  lambda: bateu_baixo and bateu_cima,
                  dica="O if da colisão precisa testar os dois com or:\n"
                       "    if bird.colliderect(cano_baixo) or bird.colliderect(cano_cima):")

        # regressão final: R recomeça e o pulo funciona
        av.apertar(jogo.keys.R)
        if av.checar("apertar R recomeça o jogo (cap. 9 não quebrou)",
                     lambda: jogo.morreu is False and jogo.pontos == 0,
                     dica="No recomecar(), chame sortear_canos(350) e zere tudo."):
            av.apertar_espaco()
            y_antes = jogo.bird.y
            av.rodar_frames(6)
            av.checar("o pulo continua funcionando (cap. 4 não quebrou)",
                      lambda: jogo.bird.y < y_antes,
                      dica="Confira o on_key_down: espaço só pula se não morreu.")

av.relatorio()
