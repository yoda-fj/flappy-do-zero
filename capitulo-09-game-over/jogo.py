# 🐤 MEU JOGO — Capítulo 9: Game over e recomeço
# Código dos capítulos anteriores (pronto) + suas novas linhas.
# Siga a LICAO.md e complete os lugares marcados com NOVO.

import pgzrun

WIDTH = 400
HEIGHT = 600

bird = Actor("bird", (100, 300))
gravidade = 0.5
velocidade = 0

cano = Actor("pipe", (350, 300))
morreu = False
pontos = 0


# NOVO NO CAPÍTULO 9: crie aqui a função recomecar()


def draw():
    screen.fill((135, 206, 235))
    cano.draw()
    bird.draw()
    screen.draw.text(str(pontos), (180, 30), fontsize=60, color="white")
    # NOVO NO CAPÍTULO 9: mostre GAME OVER aqui, mas SÓ quando morreu


def update():
    global velocidade, morreu, pontos
    if not morreu:
        velocidade = velocidade + gravidade
        bird.y = bird.y + velocidade
        cano.x = cano.x - 3
        if cano.x < -50:
            cano.x = 450
            pontos = pontos + 1
        if bird.colliderect(cano):
            morreu = True


def on_key_down(key):
    global velocidade
    if key == keys.SPACE and not morreu:
        velocidade = -8
    # NOVO NO CAPÍTULO 9: adicione o if da tecla R aqui


pgzrun.go()
