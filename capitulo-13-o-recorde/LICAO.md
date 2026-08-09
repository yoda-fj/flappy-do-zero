# 🐤 Capítulo 13 — O recorde

## 🎯 O que vamos fazer

Jogar de novo depois de perder você já consegue (capítulo 11). Mas falta
a pergunta mais importante de qualquer fliperama: **"bati meu
recorde?"** Neste capítulo o jogo guarda a sua MAIOR pontuação e comemora
quando você supera ela.

## 📖 Coisas novas que você vai aprender

- **Variáveis que sobrevivem ao recomeço** (nem tudo zera!)
- Comparar com **maior que** (`>`)
- Uma variável "bandeira" 🚩 que lembra se algo aconteceu

## 💡 A ideia: o que zera e o que não zera

Quando você aperta para jogar de novo, o `recomecar()` zera os pontos,
a velocidade, a posição... faz sentido: é uma partida NOVA. Mas o
**recorde** não pode zerar — senão não seria recorde, seria só
"pontuação da partida anterior"!

Então a regra de ouro deste capítulo é:

> O recorde nasce zerado UMA VEZ, lá em cima do arquivo, e o
> `recomecar()` **nunca** encosta nele.

E para a comemoração, usamos uma **bandeira**: `novo_recorde`, que fica
`True` só naquela partida em que o recorde caiu.

## ✍️ Passo a passo

### 1. As duas variáveis novas (lá em cima)

```python
recorde = 0
novo_recorde = False
```

### 2. A comparação acontece na hora da morte

No `update`, dentro do if da colisão, logo depois de `morreu = True`:

```python
        if bird.colliderect(cano_baixo) or bird.colliderect(cano_cima):
            morreu = True
            if pontos > recorde:
                recorde = pontos
                novo_recorde = True
```

- `pontos > recorde`: "os pontos passaram o recorde?" — só atualiza se
  for MAIOR. Fez menos pontos? O recorde antigo continua valendo.
- `novo_recorde = True`: levanta a bandeira 🚩 — "nessa partida, bateu!"
- Como criamos duas variáveis novas aqui dentro, o `global` do update
  precisa avisar: `global velocidade, morreu, pontos, recorde, novo_recorde`

### 3. O recomeço abaixa a bandeira (só ela!)

No `recomecar()`, adicione no final (e no `global`):

```python
    novo_recorde = False
```

- Partida nova, bandeira abaixada. E o `recorde`? **Nem aparece no
  recomecar** — é assim que ele sobrevive de uma partida para outra.

### 4. Mostrando na tela de game over

No `draw()`, entre o "GAME OVER" e o "Aperte ESPACO":

```python
            if novo_recorde:
                screen.draw.text("NOVO RECORDE!", center=(200, 300), fontsize=40, color="yellow")
            else:
                screen.draw.text("Recorde: " + str(recorde), center=(200, 300), fontsize=30, color="white")
```

- Bateu o recorde? Festa amarela! Não bateu? Mostra qual é o recorde
  para a pessoa tentar de novo.
- `"Recorde: " + str(recorde)`: o `str` transforma o número em texto,
  como você aprendeu no capítulo 8.

### 5. Bônus: recorde na tela inicial

Na parte do `if not comecou:` no draw, depois do "Aperte ESPACO":

```python
        if recorde > 0:
            screen.draw.text("Recorde: " + str(recorde), center=(200, 340), fontsize=30, color="white")
```

- O `if recorde > 0` esconde o "Recorde: 0" na primeira vez que o jogo
  abre — recorde zero não impressiona ninguém. 😄

## ▶️ Rodando o jogo

```
python jogo.py
```

🎮 Faça alguns pontos, morra de propósito, jogue de novo: o recorde
continua lá! Supere ele e veja a comemoração amarela.

## ✅ Testando seu capítulo

```
python teste.py
```

O teste joga várias partidas seguidas: morre com 3 pontos (recorde vira
3), recomeça (recorde não pode zerar!), morre com 1 (recorde não pode
CAIR para 1) e morre com 7 (recorde sobe e a festa amarela aparece).

## 🧩 Desafios extras

1. Faça o texto "NOVO RECORDE!" piscar (use o truque do `tempo % 60`
   do capítulo 11).
2. Toque um som de festa quando bater o recorde (precisa da pasta
   `sounds/` com um arquivo, ex.: `sounds.recorde.play()`).
3. Salve o recorde num ARQUIVO para ele sobreviver mesmo depois de
   fechar o jogo (peça ajuda a um adulto: é o `open()` do Python).
