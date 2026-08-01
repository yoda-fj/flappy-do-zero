# 🐤 Capítulo 10 — VERSÃO COMPLETA (branch solucao)
# Este é o jogo pronto deste capítulo. No branch main, este arquivo
# vem vazio para o aluno preencher seguindo a LICAO.md.

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


def draw():
    screen.fill((135, 206, 235))
    cano_baixo.draw()
    cano_cima.draw()
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
