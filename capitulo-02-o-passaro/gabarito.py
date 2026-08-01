# 🐤 Capítulo 2 — GABARITO (só olhe depois de tentar!)

import pgzrun

WIDTH = 400
HEIGHT = 600

bird = Actor("bird", (100, 300))


def draw():
    screen.fill((135, 206, 235))
    bird.draw()


pgzrun.go()
