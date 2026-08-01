# 🐤 Capítulo 3 — A gravidade

## 🎯 O que vamos fazer

O pássaro está parado no ar, desafiando a física. Hora de criar a
**gravidade**: quando o jogo começar, o pássaro vai cair sozinho,
como qualquer coisa solta no ar.

## 📖 Coisas novas que você vai aprender

- A função **update()**: onde o jogo "pensa"
- Mudar o valor de uma variável usando ela mesma
- A diferença entre draw() (desenhar) e update() (atualizar)

## ✍️ Passo a passo

### A função update (embaixo de tudo)

```python
def update():
    bird.y = bird.y + 3
```

- Assim como o `draw()`, o `update()` é um nome especial: o Pygame Zero
  chama essa função **60 vezes por segundo**, o tempo todo.
- Qual a diferença entre os dois?
  - `draw()` = **desenhar** as coisas na tela (a parte que aparece)
  - `update()` = **atualizar** o jogo (a parte que pensa: mover, cair, contar)
- `bird.y` é a posição vertical do pássaro. O ponto (`.`) quer dizer
  "de dentro do": é o y **de dentro do** bird.
- `bird.y = bird.y + 3` parece estranho na matemática, né? Mas no Python
  o `=` não é "igual" — é "**guarde**". Leia assim:
  "pegue o valor atual de bird.y, some 3, e guarde o resultado de volta
  em bird.y". A cada frame, o pássaro desce 3 pixels.
- Como o y cresce para baixo (lembra?), SOMAR no y faz o pássaro CAIR. 🍎

## ▶️ Rodando o jogo

```
pgzrun jogo.py
```

O pássaro despenca e some por baixo da tela! No próximo capítulo vamos
dar a ele um jeito de lutar contra a gravidade (o pulo).

## ✅ Testando seu capítulo

```
python teste.py
```

⚠️ **O erro mais comum deste capítulo:** escrever `bird.y = bird.y + 3`
FORA da função update (sem os 4 espaços). Aí a linha roda uma vez só,
quando o jogo abre, e o pássaro não cai de verdade. O teste percebe isso!

## 🧩 Desafios extras (opcional)

1. Mude o `3` para `1` (câmera lenta) e depois para `8` (meteorito!).
   Qual número deixa o jogo mais legal?
2. Pergunta para pensar: por que usamos uma função que roda 60 vezes por
   segundo em vez de somar 180 de uma vez?
