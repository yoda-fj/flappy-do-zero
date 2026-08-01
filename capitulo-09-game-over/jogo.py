# 🐤 Capítulo 09 — VERSÃO COMPLETA (branch solucao)
# Este é o jogo pronto deste capítulo. No branch main, este arquivo
# vem vazio para o aluno preencher seguindo a LICAO.md.

import pgzrun

WIDTH = 400
HEIGHT = 600

bird = Actor("bird", (100, 300))
gravidade = 0.5
velocidade = 0

cano = Actor("pipe", (350, 300))
morreu = False
pontos = 0


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
