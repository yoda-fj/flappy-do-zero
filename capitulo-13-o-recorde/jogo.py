# 🐤 MEU JOGO — Capítulo 13: O recorde
# Código dos capítulos anteriores (pronto) + suas novas linhas.
# Siga a LICAO.md e complete os lugares marcados com NOVO.

import pgzrun
import random

WIDTH = 400
HEIGHT = 600

bird = Actor("bird", (100, 300))
gravidade = 0.5
velocidade = 0

BURACO = 180
cano_baixo = Actor("pipe", (350, 590))
cano_cima = Actor("pipe", (350, 10))
cano_cima.angle = 180

grama1 = Actor("grass", (200, 570))
grama2 = Actor("grass", (600, 570))
nuvem1 = Actor("cloud", (120, 90))
nuvem2 = Actor("cloud", (340, 160))

comecou = False
morreu = False
pontos = 0
# NOVO NO CAPÍTULO 13: crie aqui o recorde e o novo_recorde (os dois zerados)


def sortear_canos(x):
    centro = random.randint(230, 370)
    cano_baixo.pos = (x, centro + BURACO / 2 + 200)
    cano_cima.pos = (x, centro - BURACO / 2 - 200)


def recomecar():
    global velocidade, pontos, morreu, comecou
    bird.y = 300
    velocidade = 0
    sortear_canos(350)
    grama1.x = 200
    grama2.x = 600
    pontos = 0
    morreu = False
    comecou = True
    # NOVO NO CAPÍTULO 13: desligue o novo_recorde aqui (mas NUNCA zere
    # o recorde! ele precisa sobreviver ao recomeço)


def draw():
    screen.fill((135, 206, 235))
    nuvem1.draw()
    nuvem2.draw()
    cano_baixo.draw()
    cano_cima.draw()
    bird.draw()
    grama1.draw()
    grama2.draw()
    if not comecou:
        screen.draw.text("FLAPPY DO ZERO", center=(200, 200), fontsize=50, color="white")
        screen.draw.text("Aperte ESPACO para comecar", center=(200, 280), fontsize=25, color="white")
        # NOVO NO CAPÍTULO 13: se já existe recorde, mostre ele na tela inicial
    else:
        screen.draw.text(str(pontos), (180, 30), fontsize=60, color="white")
        if morreu:
            screen.draw.text("GAME OVER", center=(200, 220), fontsize=60, color="red")
            screen.draw.text("Aperte ESPACO para jogar de novo", center=(200, 360), fontsize=25, color="white")
            # NOVO NO CAPÍTULO 13: mostre "NOVO RECORDE!" ou "Recorde: X"
            # entre o GAME OVER e o "Aperte ESPACO"


def update():
    global velocidade, morreu, pontos
    if comecou and not morreu:
        velocidade = velocidade + gravidade
        bird.y = bird.y + velocidade
        cano_baixo.x = cano_baixo.x - 3
        cano_cima.x = cano_cima.x - 3
        grama1.x = grama1.x - 3
        grama2.x = grama2.x - 3
        nuvem1.x = nuvem1.x - 1
        nuvem2.x = nuvem2.x - 1
        if cano_baixo.x < -50:
            sortear_canos(450)
            pontos = pontos + 1
        if grama1.x < -200:
            grama1.x = 600
        if grama2.x < -200:
            grama2.x = 600
        if nuvem1.x < -70:
            nuvem1.x = 470
        if nuvem2.x < -70:
            nuvem2.x = 470
        if bird.colliderect(cano_baixo) or bird.colliderect(cano_cima):
            morreu = True
            # NOVO NO CAPÍTULO 13: aqui, na hora exata da morte, compare
            # os pontos com o recorde (a lição mostra o if completo)


def on_key_down(key):
    global velocidade, comecou
    if key == keys.SPACE:
        if not comecou:
            comecou = True
        elif morreu:
            recomecar()
        else:
            velocidade = -8
    if key == keys.R:
        recomecar()


pgzrun.go()
