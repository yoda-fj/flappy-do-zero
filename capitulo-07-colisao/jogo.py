# 🐤 MEU JOGO — Capítulo 7: Colisão
# Código dos capítulos anteriores (pronto) + suas novas linhas.
# ATENÇÃO: o update muda bastante neste capítulo — a lição mostra o novo.
# Siga a LICAO.md e complete os lugares marcados com NOVO.

import pgzrun

WIDTH = 400
HEIGHT = 600

bird = Actor("bird", (100, 300))
gravidade = 0.5
velocidade = 0

cano = Actor("pipe", (350, 300))

# NOVO NO CAPÍTULO 7: crie a variável morreu aqui


def draw():
    screen.fill((135, 206, 235))
    cano.draw()
    bird.draw()


def update():
    global velocidade
    velocidade = velocidade + gravidade
    bird.y = bird.y + velocidade
    cano.x = cano.x - 3
    if cano.x < -50:
        cano.x = 450
    # NOVO NO CAPÍTULO 7: a colisão entra aqui — mas leia a lição!
    # O update inteiro precisa ficar dentro de "if not morreu:"


def on_key_down(key):
    global velocidade
    if key == keys.SPACE:
        velocidade = -8


pgzrun.go()
