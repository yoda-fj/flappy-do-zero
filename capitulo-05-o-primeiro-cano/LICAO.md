# 🐤 Capítulo 5 — O primeiro cano

## 🎯 O que vamos fazer

O pássaro já voa, mas Flappy sem canos não é Flappy! Neste capítulo
aparece o primeiro cano verde, parado no meio da tela. Ele ainda não se
move — um passo de cada vez.

## 📖 Coisas novas que você vai aprender

- Um jogo pode ter **vários Actors**
- A ordem do draw() decide o que fica **na frente** e o que fica **atrás**

## ✍️ Passo a passo

### O cano (lá em cima, depois do bird)

```python
cano = Actor("pipe", (350, 300))
```

- Igualzinho ao pássaro! `Actor` serve para qualquer personagem/objeto.
- `"pipe"` é o arquivo `images/pipe.png` — um cano verde bem comprido.
- `(350, 300)`: perto da borda direita, no meio da altura.

### Desenhando o cano (dentro do draw)

```python
def draw():
    screen.fill((135, 206, 235))
    cano.draw()
    bird.draw()
```

- Repare: o cano é desenhado ANTES do pássaro. Assim, se os dois se
  cruzarem, o pássaro aparece **na frente** do cano.
- A ordem do draw é como colar figurinhas num álbum: a última colada
  fica por cima das outras.

## ▶️ Rodando o jogo

```
python jogo.py
```

Você vai ver o cano verde parado e o pássaro caindo (aperte ESPAÇO para
voar). Por enquanto o cano é só decoração — ele nem se mexe, nem machuca.
Isso muda nos próximos dois capítulos... 😈

## ✅ Testando seu capítulo

```
python teste.py
```

## 🧩 Desafios extras (opcional)

1. Mude a posição do cano. O que acontece com x = 200? E y = 100?
2. Crie um SEGUNDO cano com outro nome (`cano2`) em outra posição.
   (No capítulo 10 isso vira oficial!)
