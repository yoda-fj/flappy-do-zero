# 🐤 MEU JOGO — Capítulo 12: Cenário com parallax
# Código dos capítulos anteriores (pronto) + suas novas linhas.
# ATENÇÃO: este capítulo usa duas imagens novas (grass.png e cloud.png)
# que já estão na pasta images/. Siga a LICAO.md e complete os NOVO.

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

# NOVO NO CAPÍTULO 12: crie aqui grama1, grama2, nuvem1 e nuvem2
# (a lição explica por que são DUAS de cada e as posições certas)

comecou = False
morreu = False
pontos = 0


def sortear_canos(x):
    centro = random.randint(230, 370)
    cano_baixo.pos = (x, centro + BURACO / 2 + 200)
    cano_cima.pos = (x, centro - BURACO / 2 - 200)


def recomecar():
    global velocidade, pontos, morreu, comecou
    bird.y = 300
    velocidade = 0
    sortear_canos(350)
    pontos = 0
    morreu = False
    comecou = True


def draw():
    screen.fill((135, 206, 235))
    # NOVO NO CAPÍTULO 12: desenhe as nuvens aqui (logo depois do céu)
    cano_baixo.draw()
    cano_cima.draw()
    bird.draw()
    # NOVO NO CAPÍTULO 12: desenhe as gramas aqui (por cima dos canos!)
    if not comecou:
        screen.draw.text("FLAPPY DO ZERO", center=(200, 200), fontsize=50, color="white")
        screen.draw.text("Aperte ESPACO para comecar", center=(200, 280), fontsize=25, color="white")
    else:
        screen.draw.text(str(pontos), (180, 30), fontsize=60, color="white")
        if morreu:
            screen.draw.text("GAME OVER", center=(200, 250), fontsize=60, color="red")
            screen.draw.text("Aperte ESPACO para jogar de novo", center=(200, 320), fontsize=25, color="white")


def update():
    global velocidade, morreu, pontos
    if comecou and not morreu:
        velocidade = velocidade + gravidade
        bird.y = bird.y + velocidade
        cano_baixo.x = cano_baixo.x - 3
        cano_cima.x = cano_cima.x - 3
        # NOVO NO CAPÍTULO 12: mova as gramas (rápido) e as nuvens (devagar)
        # e faça cada uma voltar para a direita quando sair da tela
        if cano_baixo.x < -50:
            sortear_canos(450)
            pontos = pontos + 1
        if bird.colliderect(cano_baixo) or bird.colliderect(cano_cima):
            morreu = True


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
