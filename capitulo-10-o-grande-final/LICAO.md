# 🐤 Capítulo 10 — O grande final: o buraco no cano

## 🎯 O que vamos fazer

O Flappy de verdade não tem UM cano no meio: tem um cano em cima, um
em baixo, e um **buraco** no meio para o pássaro passar — e o buraco
muda de altura a cada cano! Este capítulo transforma seu protótipo no
jogo completo.

## 📖 Coisas novas que você vai aprender

- **random**: números aleatórios (sorteados)
- Função **com parâmetro** (uma função que recebe um valor)
- Virar uma imagem de ponta-cabeça com **angle**
- **Constantes**: variáveis em MAIÚSCULAS que configuram o jogo

## ✍️ Passo a passo

### 1. Sorteio e as constantes (lá em cima)

```python
import random
```

```python
BURACO = 180
cano_baixo = Actor("pipe", (350, 590))
cano_cima = Actor("pipe", (350, 10))
cano_cima.angle = 180
```

- `import random`: a caixa de ferramentas de sorteio do Python.
- `BURACO` em MAIÚSCULAS é uma **constante**: um valor de configuração
  que não muda durante o jogo. É o tamanho do vão entre os canos.
- Dois Actors com a MESMA imagem! O de cima usa `angle = 180` para
  ficar de ponta-cabeça — a "boca" do cano fica virada para o buraco.
- Os números (590 e 10) deixam o buraco bem no meio da tela no começo.

### 2. A função que sorteia a altura

```python
def sortear_canos(x):
    centro = random.randint(230, 370)
    cano_baixo.pos = (x, centro + BURACO / 2 + 200)
    cano_cima.pos = (x, centro - BURACO / 2 - 200)
```

- `sortear_canos(x)` é uma função **com parâmetro**: quem chama entrega
  o valor de x (a posição horizontal onde os canos vão nascer).
- `random.randint(230, 370)` sorteia um número inteiro entre 230 e 370:
  é a altura do CENTRO do buraco. Cada cano nasce numa altura diferente!
- A matemática: o cano de baixo fica meio buraco ABAIXO do centro, mais
  200 (metade da altura da imagem, que tem 400 pixels). O de cima, o
  contrário. Desenhe no papel que faz sentido! 📐

### 3. Usando no update (troque o miolo do update)

```python
        cano_baixo.x = cano_baixo.x - 3
        cano_cima.x = cano_cima.x - 3
        if cano_baixo.x < -50:
            sortear_canos(450)
            pontos = pontos + 1
        if bird.colliderect(cano_baixo) or bird.colliderect(cano_cima):
            morreu = True
```

- Os DOIS canos andam juntos (mesma velocidade).
- `or` = "ou": bateu em QUALQUER UM dos dois, morreu.
- Ao sair da tela: `sortear_canos(450)` cria um cano novinho, com buraco
  em altura sorteada, lá na direita.

### 4. Ajustes finais

- No `draw()`: `cano_baixo.draw()` e `cano_cima.draw()` (apague o cano antigo!)
- No `recomecar()`: `sortear_canos(350)` no lugar do `cano.x = 350`
- O `cano = Actor(...)` antigo pode ser apagado — ele foi promovido a dois!

## ▶️ Rodando o jogo

```
python jogo.py
```

🎮 **O JOGO ESTÁ COMPLETO!** Desvie dos canos, faça pontos, morra,
aperte R, tente de novo. Você programou TUDO isso, linha por linha.

## ✅ Testando seu capítulo

```
python teste.py
```

O teste deste capítulo é especial: além das novidades, ele re-verifica
TUDO dos capítulos anteriores (gravidade, pulo, colisão, pontos, R).
Programadores chamam isso de **teste de regressão**: garantir que o
código novo não quebrou o antigo.

## 🧩 Desafios extras (agora o jogo é seu!)

1. Deixe o `BURACO` menor (mais difícil) ou maior (mais fácil).
2. Desenhe seu próprio pássaro e salve por cima do `images/bird.png`.
3. Faça o pássaro inclinar: `bird.angle = -velocidade * 3` no update.
4. Invente: canos mais rápidos a cada 5 pontos? Céu que escurece?
