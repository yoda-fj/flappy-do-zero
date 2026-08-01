# 🐤 Capítulo 04 — VERSÃO COMPLETA (branch solucao)
# Este é o jogo pronto deste capítulo. No branch main, este arquivo
# vem vazio para o aluno preencher seguindo a LICAO.md.

import pgzrun

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


pgzrun.go()
