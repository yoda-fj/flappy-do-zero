# 🐤 Capítulo 8 — Pontuação

## 🎯 O que vamos fazer

Todo herói merece pontos! Cada cano que o pássaro ultrapassa vale **1
ponto**, e o placar aparece grandão no topo da tela.

## 📖 Coisas novas que você vai aprender

- Variável **contadora** (que acumula: 0, 1, 2, 3...)
- **str()**: transformar número em texto
- **screen.draw.text()**: escrever na tela

## ✍️ Passo a passo

### 1. O placar (lá em cima)

```python
pontos = 0
```

- Começa em zero, claro. Ninguém nasce pontuando!

### 2. Somando pontos (no update, dentro do if do teletransporte)

```python
        if cano.x < -50:
            cano.x = 450
            pontos = pontos + 1
```

- Quando o cano sai da tela e volta para a direita, significa que o
  pássaro PASSOU por ele. Momento exato de marcar o ponto!
- Como mudamos `pontos` dentro do update, o global precisa avisar:
  `global velocidade, morreu, pontos`

### 3. Mostrando o placar (no draw, por último)

```python
    screen.draw.text(str(pontos), (180, 30), fontsize=60, color="white")
```

- `screen.draw.text` escreve um texto na tela.
- `str(pontos)`: o computador guarda pontos como NÚMERO (para somar),
  mas escrever exige TEXTO. `str()` faz a conversão. Esquecer isso dá
  erro — teste depois para ver a mensagem!
- `(180, 30)` é a posição, `fontsize=60` o tamanhão, `color="white"` a cor.

## ▶️ Rodando o jogo

```
python jogo.py
```

Passe do cano e veja o placar subir! Quantos pontos você consegue fazer
antes de bater?

## ✅ Testando seu capítulo

```
python teste.py
```

## 🧩 Desafios extras (opcional)

1. Mude a cor e a posição do placar.
2. Faça cada cano valer 10 pontos. E valendo 100? (Fácil demais, né? É
   assim que se faz um jogo fácil ou difícil: mexendo nos números!)
