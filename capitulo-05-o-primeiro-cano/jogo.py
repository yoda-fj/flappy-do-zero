# 🐤 MEU JOGO — Capítulo 5: O primeiro cano
# Código dos capítulos anteriores (pronto) + suas novas linhas.
# Siga a LICAO.md e complete os lugares marcados com NOVO.

import pgzrun

WIDTH = 400
HEIGHT = 600

bird = Actor("bird", (100, 300))
gravidade = 0.5
velocidade = 0

# NOVO NO CAPÍTULO 5: crie o cano aqui (a lição mostra como)


def draw():
    screen.fill((135, 206, 235))
    # NOVO NO CAPÍTULO 5: desenhe o cano aqui (ANTES do pássaro!)
    bird.draw()


def update():
    global velocidade
    velocidade = velocidade + gravidade
    bird.y = bird.y + velocidade


def on_key_down(key):
    global velocidade
    if key == keys.SPACE:
        velocidade = -8


pgzrun.go()
