# 🐤 MEU JOGO — Capítulo 11: A tela inicial
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

# NOVO NO CAPÍTULO 11: crie aqui a variável comecou (começa valendo False)

morreu = False
pontos = 0


def sortear_canos(x):
    centro = random.randint(230, 370)
    cano_baixo.pos = (x, centro + BURACO / 2 + 200)
    cano_cima.pos = (x, centro - BURACO / 2 - 200)


def recomecar():
    global velocidade, pontos, morreu
    bird.y = 300
    velocidade = 0
    sortear_canos(350)
    pontos = 0
    morreu = False
    # NOVO NO CAPÍTULO 11: quem recomeça já quer jogar — ligue o comecou aqui
    # (não esqueça de avisar o global lá em cima!)


def draw():
    screen.fill((135, 206, 235))
    cano_baixo.draw()
    cano_cima.draw()
    bird.draw()
    screen.draw.text(str(pontos), (180, 30), fontsize=60, color="white")
    if morreu:
        screen.draw.text("GAME OVER", center=(200, 250), fontsize=60, color="red")
        screen.draw.text("Aperte ESPACO para jogar de novo", center=(200, 320), fontsize=25, color="white")
    # NOVO NO CAPÍTULO 11: se o jogo NÃO começou, desenhe a tela inicial
    # (título + "Aperte ESPACO para comecar") — a lição mostra o jeito


def update():
    global velocidade, morreu, pontos
    if not morreu:
        velocidade = velocidade + gravidade
        bird.y = bird.y + velocidade
        cano_baixo.x = cano_baixo.x - 3
        cano_cima.x = cano_cima.x - 3
        if cano_baixo.x < -50:
            sortear_canos(450)
            pontos = pontos + 1
        if bird.colliderect(cano_baixo) or bird.colliderect(cano_cima):
            morreu = True


def on_key_down(key):
    global velocidade
    if key == keys.SPACE and not morreu:
        velocidade = -8
    if key == keys.R:
        recomecar()


pgzrun.go()
