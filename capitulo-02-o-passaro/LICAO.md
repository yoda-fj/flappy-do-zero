# 🐤 Capítulo 2 — O pássaro aparece

## 🎯 O que vamos fazer

A janela azul já existe. Agora vamos colocar o personagem principal nela:
o pássaro! No final deste capítulo você vai vê-lo parado no meio da tela.

## 📖 Coisas novas que você vai aprender

- O que é um **Actor** (um personagem com imagem e posição)
- Coordenadas **x** e **y** na tela
- Por que a **ordem** das linhas dentro do draw() importa

## ✍️ Passo a passo

Abra o `jogo.py`. Ele já vem com o código do Capítulo 1 — o jogo cresce
assim, um capítulo em cima do outro. Você vai adicionar só as partes novas.

### O pássaro (lá em cima, perto do WIDTH e HEIGHT)

```python
bird = Actor("bird", (100, 300))
```

- `Actor` é um **ator**, como no teatro: um personagem que aparece no palco.
  Ele tem uma imagem e uma posição.
- `"bird"` é o nome da imagem: o arquivo `images/bird.png` que está na
  pasta deste capítulo. Repare que escrevemos `"bird"` **sem** o `.png`.
- `(100, 300)` é a posição onde ele começa: **x = 100** (distância da
  borda esquerda) e **y = 300** (distância do TOPO da tela).
- ⚠️ Atenção: no computador, o **y cresce para BAIXO**! É o contrário da
  aula de matemática. y = 0 é o topo da tela, y = 600 é lá embaixo.

### Desenhando o pássaro (dentro do draw)

```python
def draw():
    screen.fill((135, 206, 235))
    bird.draw()
```

- `bird.draw()` = "desenhe o pássaro na posição dele".
- Repare na ORDEM: primeiro pintamos o fundo, DEPOIS desenhamos o pássaro.
- Se fosse ao contrário, o que aconteceria? O fundo azul seria pintado
  POR CIMA do pássaro, e ele sumiria! É como pintar uma parede: primeiro
  a tinta, depois o quadro pendurado.

## ▶️ Rodando o jogo

```
pgzrun jogo.py
```

Um pássaro amarelo parado no céu azul. Ele ainda não se mexe — isso é
assunto do próximo capítulo!

## ✅ Testando seu capítulo

```
python teste.py
```

## 🧩 Desafios extras (opcional)

1. Mova o pássaro de lugar mudando os números `(100, 300)`.
   O que acontece com x = 350? E com y = 50?
2. Tente colocar `bird.draw()` ANTES do `screen.fill(...)` e rode o jogo.
   Entendeu o que aconteceu? Depois desfaça (o teste também percebe isso!).
