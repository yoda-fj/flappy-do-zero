# 🐤 Capítulo 11 — A tela inicial

## 🎯 O que vamos fazer

Todo jogo de verdade tem uma **tela inicial**: o mundo aparece parado,
o título brilha no meio, e o jogo só começa quando o jogador aperta uma
tecla. Neste capítulo o seu Flappy ganha isso — e de brinde, o ESPAÇO
também serve para **jogar de novo** depois do game over.

## 📖 Coisas novas que você vai aprender

- **Estado do jogo**: uma variável que diz em que "momento" o jogo está
- **and**: juntar duas condições no mesmo `if`
- if / elif / else: três caminhos para a mesma tecla

## 💡 A ideia: uma variável "semáforo"

Seu jogo já tem o `morreu`, que trava tudo quando bate no cano. Agora
vamos criar o `comecou`, que faz o contrário: **trava tudo ANTES de
começar**. Os dois juntos funcionam como um semáforo:

- `comecou = False` → 🛑 tela inicial, mundo congelado
- `comecou = True` e `morreu = False` → 🟢 jogando
- `morreu = True` → 🔴 game over, esperando o recomeço

## ✍️ Passo a passo

### 1. A variável nova (lá em cima, perto do `morreu`)

```python
comecou = False
```

- O jogo ABRE na tela inicial, então ela começa valendo `False`.

### 2. O update só anda depois do começo

Troque a primeira linha do update:

```python
    if comecou and not morreu:
```

- `and` = "e": as DUAS coisas precisam ser verdade. O mundo só se move
  quando o jogo começou **e** o pássaro está vivo.
- Antes do começo, o update roda 60 vezes por segundo mas não faz nada:
  pássaro parado, canos parados. É a tela inicial congelada!

### 3. Desenhando a tela inicial

No `draw()`, a pontuação e o game over só fazem sentido depois do
começo. Reorganize o final do draw assim:

```python
    if not comecou:
        screen.draw.text("FLAPPY DO ZERO", center=(200, 200), fontsize=50, color="white")
        screen.draw.text("Aperte ESPACO para comecar", center=(200, 280), fontsize=25, color="white")
    else:
        screen.draw.text(str(pontos), (180, 30), fontsize=60, color="white")
        if morreu:
            screen.draw.text("GAME OVER", center=(200, 250), fontsize=60, color="red")
            screen.draw.text("Aperte ESPACO para jogar de novo", center=(200, 320), fontsize=25, color="white")
```

- `else` = "senão": ou mostra a tela inicial, ou mostra o jogo. Nunca os dois.
- Repare que os canos e o pássaro continuam sendo desenhados sempre —
  é o cenário parado atrás do título, igual ao Flappy de verdade.

### 4. Uma tecla, três funções

O ESPAÇO agora tem três empregos: **começar**, **jogar de novo** e
**pular**. Troque o miolo do `on_key_down`:

```python
def on_key_down(key):
    global velocidade, comecou
    if key == keys.SPACE:
        if not comecou:
            comecou = True
        elif morreu:
            recomecar()
        else:
            velocidade = -8
    if key == keys.R:
        recomecar()
```

- `elif` = "senão, se": o Python testa de cima para baixo e para no
  primeiro que for verdade.
  1. Ainda não começou? → começa!
  2. Começou mas morreu? → joga de novo!
  3. Senão (jogando normal)? → pula!
- Não esqueça do `comecou` no `global`, senão o Python cria uma variável
  falsa só dentro da função e o jogo nunca começa.

### 5. O recomeço já entra jogando

Dentro do `recomecar()`, adicione no final (e no `global`):

```python
    comecou = True
```

- Quem apertou para jogar de novo não quer ver a tela inicial de novo —
  quer jogar! Por isso o recomeço já liga o `comecou`.

## ▶️ Rodando o jogo

```
python jogo.py
```

🎮 O jogo abre parado, com o título. ESPAÇO começa. Morreu? ESPAÇO
(ou R) joga de novo na hora. Ficou com cara de jogo de fliperama!

## ✅ Testando seu capítulo

```
python teste.py
```

O teste verifica se o mundo fica congelado antes do começo, se o título
aparece na tela, se o ESPAÇO cumpre os três papéis — e se tudo dos
capítulos anteriores continua funcionando.

## 🧩 Desafios extras

1. Faça o título piscar: crie uma variável `tempo` que cresce no update
   e use `if tempo % 60 < 30:` para desenhar o título só metade do tempo.
2. Na tela inicial, faça o pássaro boiar suavemente: `bird.y = 300` com
   um sobe-e-desce de mentira (dica: use o `tempo` do desafio 1).
3. Guarde a MAIOR pontuação numa variável `recorde` e mostre na tela de
   game over... (mentira, guarda essa energia: é exatamente o capítulo 13! 😄)
