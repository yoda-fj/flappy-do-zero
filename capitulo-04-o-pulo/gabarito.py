# 🐤 Capítulo 4 — GABARITO (só olhe depois de tentar!)

WIDTH = 400
HEIGHT = 600

bird = Actor("bird", (100, 300))
gravidade = 0.5
velocidade = 0


def draw():
    screen.fill((135, 206, 235))
    bird.draw()


def update():
    global velocidade
    velocidade = velocidade + gravidade
    bird.y = bird.y + velocidade


def on_key_down(key):
    global velocidade
    if key == keys.SPACE:
        velocidade = -8
