# 🐤 Capítulo 12 — Cenário com parallax: grama e nuvens

## 🎯 O que vamos fazer

Seu jogo funciona, mas o cenário é um céu azul vazio. Neste capítulo
final o Flappy ganha **chão de grama** e **nuvens no céu** — e o
melhor: cada camada se move numa velocidade diferente, criando o
efeito de profundidade que os jogos profissionais usam. O nome
bonito disso é **parallax**.

## 📖 Coisas novas que você vai aprender

- **Parallax**: coisas longe andam devagar, coisas perto andam rápido
- **Duas cópias do mesmo desenho** para um chão infinito
- Revisão: teletransporte (cap. 6) e ordem do draw (cap. 5)

## 💡 A ideia do parallax

Quando você anda de carro, as montanhas lá longe passam devagarinho e
os postes na beira da estrada voam. No jogo é igual:

- **Canos e grama** (perto): andam 3 pixels por frame
- **Nuvens** (longe): andam 1 pixel por frame

E o chão infinito? São **duas gramas de 400 pixels**, uma na frente da
outra, como dois vagões de trem. Quando uma sai da tela pela esquerda,
ela teletransporta para a direita e entra na fila de novo. 🚂

## ✍️ Passo a passo

### 1. Os quatro atores novos (lá em cima)

```python
grama1 = Actor("grass", (200, 570))
grama2 = Actor("grass", (600, 570))
nuvem1 = Actor("cloud", (120, 90))
nuvem2 = Actor("cloud", (340, 160))
```

- A imagem da grama tem 400 pixels de largura — a largura exata da
  tela! Por isso `grama1` no centro (x=200) cobre a tela toda e
  `grama2` espera escondida à direita (x=600).
- As nuvens ficam em alturas diferentes para o céu não ficar simétrico
  e chato.

### 2. A ordem do draw importa

```python
def draw():
    screen.fill((135, 206, 235))
    nuvem1.draw()
    nuvem2.draw()
    cano_baixo.draw()
    cano_cima.draw()
    bird.draw()
    grama1.draw()
    grama2.draw()
    # ... textos continuam por último
```

- Quem é desenhado DEPOIS aparece POR CIMA. Ordem: céu → nuvens →
  canos → pássaro → grama → textos.
- A grama por cima dos canos faz eles parecerem "plantados" no chão.

### 3. Movendo tudo no update

Dentro do `if comecou and not morreu:`, depois dos canos:

```python
        grama1.x = grama1.x - 3
        grama2.x = grama2.x - 3
        nuvem1.x = nuvem1.x - 1
        nuvem2.x = nuvem2.x - 1
```

- A grama anda na velocidade dos canos (3): ela ESTÁ no mundo do jogo.
- A nuvem anda 1: três vezes mais devagar. Esse contraste É o parallax.

### 4. O teletransporte (igual ao capítulo 6!)

Ainda dentro do if, depois do if dos canos:

```python
        if grama1.x < -200:
            grama1.x = 600
        if grama2.x < -200:
            grama2.x = 600
        if nuvem1.x < -70:
            nuvem1.x = 470
        if nuvem2.x < -70:
            nuvem2.x = 470
```

- A grama tem 400 de largura, então ela some de vez quando o centro
  passa de -200 (metade). Nessa hora ela volta para x=600, colada
  atrás da outra grama.
- A nuvem tem 140 de largura: some em -70 e renasce em 470, entrando
  devagarinho pela direita.

### 5. Resetando a grama no recomeço

Dentro do `recomecar()`:

```python
    grama1.x = 200
    grama2.x = 600
```

- Sem isso, depois de morrer várias vezes a grama podia estar fora do
  lugar no jogo novo.

## ▶️ Rodando o jogo

```
python jogo.py
```

🎮 Preste atenção: o chão corre junto com os canos, as nuvens deslizam
devagar, e o jogo inteiro ganhou profundidade. UM efeito profissional,
feito com coisas que você já sabia!

## ✅ Testando seu capítulo

```
python teste.py
```

O teste mede de verdade as velocidades: a grama PRECISA andar mais
rápido que a nuvem, e cada uma precisa voltar quando sai da tela.

## 🧩 Desafios extras

1. Nuvem que nasce em altura sorteada: no teletransporte, use
   `nuvem1.y = random.randint(50, 200)`.
2. Morreu ao encostar no chão? Adicione no if da colisão:
   `or bird.colliderect(grama1) or bird.colliderect(grama2)`.
3. Uma terceira camada! Crie montanhas (imagem sua) andando a 2 pixels
   por frame, entre as nuvens e os canos.
