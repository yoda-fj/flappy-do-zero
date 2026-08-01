# 🐤 MEU JOGO — Capítulo 10: O grande final
# Código dos capítulos anteriores (pronto) + suas novas linhas.
# ATENÇÃO: o cano único vira DOIS canos neste capítulo — a lição explica.
# Siga a LICAO.md e complete os lugares marcados com NOVO.

import pgzrun
# NOVO NO CAPÍTULO 10: importe a caixa de ferramentas de sorteio aqui

WIDTH = 400
HEIGHT = 600

bird = Actor("bird", (100, 300))
gravidade = 0.5
velocidade = 0

cano = Actor("pipe", (350, 300))
morreu = False
pontos = 0

# NOVO NO CAPÍTULO 10: apague o cano único acima e crie no lugar:
# a constante BURACO, o cano_baixo e o cano_cima (lição mostra como)


# NOVO NO CAPÍTULO 10: crie aqui a função sortear_canos(x)


def recomecar():
    global velocidade, pontos, morreu
    bird.y = 300
    velocidade = 0
    cano.x = 350
    pontos = 0
    morreu = False


def draw():
    screen.fill((135, 206, 235))
    cano.draw()
    bird.draw()
    screen.draw.text(str(pontos), (180, 30), fontsize=60, color="white")
    if morreu:
        screen.draw.text("GAME OVER", center=(200, 250), fontsize=60, color="red")
        screen.draw.text("Aperte R para recomecar", center=(200, 320), fontsize=30, color="white")


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
    if key == keys.R:
        recomecar()


pgzrun.go()
