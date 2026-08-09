# 🐤 Capítulo 7 — GABARITO (só olhe depois de tentar!)

import pgzrun

WIDTH = 400
HEIGHT = 600

bird = Actor("bird", (100, 300))
gravidade = 0.5
velocidade = 0

cano = Actor("pipe", (350, 300))
morreu = False


def draw():
    screen.fill((135, 206, 235))
    cano.draw()
    bird.draw()


def update():
    global velocidade, morreu
    if not morreu:
        velocidade = velocidade + gravidade
        bird.y = bird.y + velocidade
        cano.x = cano.x - 3
        if cano.x < -50:
            cano.x = 450
        if bird.colliderect(cano):
            morreu = True


def on_key_down(key):
    global velocidade
    if key == keys.SPACE and not morreu:
        velocidade = -8


pgzrun.go()
