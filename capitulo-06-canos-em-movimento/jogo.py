# 🐤 MEU JOGO — Capítulo 6: Canos em movimento
# Código dos capítulos anteriores (pronto) + suas novas linhas.
# Siga a LICAO.md e complete os lugares marcados com NOVO.

import pgzrun

WIDTH = 400
HEIGHT = 600

bird = Actor("bird", (100, 300))
gravidade = 0.5
velocidade = 0

cano = Actor("pipe", (350, 300))


def draw():
    screen.fill((135, 206, 235))
    cano.draw()
    bird.draw()


def update():
    global velocidade
    velocidade = velocidade + gravidade
    bird.y = bird.y + velocidade
    # NOVO NO CAPÍTULO 6: mova o cano e faça ele voltar (2 linhas + if)


def on_key_down(key):
    global velocidade
    if key == keys.SPACE:
        velocidade = -8


pgzrun.go()
