# 🐤 Capítulo 02 — VERSÃO COMPLETA (branch solucao)
# Este é o jogo pronto deste capítulo. No branch main, este arquivo
# vem vazio para o aluno preencher seguindo a LICAO.md.

import pgzrun

WIDTH = 400
HEIGHT = 600

bird = Actor("bird", (100, 300))


def draw():
    screen.fill((135, 206, 235))
    bird.draw()


pgzrun.go()
