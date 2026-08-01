# 🐤 Capítulo 6 — Canos em movimento

## 🎯 O que vamos fazer

O cano parado vira um cano que **anda** — deslizando da direita para a
esquerda, sem parar. E quando sair da tela, ele volta lá para a direita,
como um trem em loop. É assim que o Flappy cria canos infinitos!

## 📖 Coisas novas que você vai aprender

- Mover no eixo **x** (horizontal)
- "Sair da tela" = coordenada negativa
- Usar `if` para fazer algo voltar ao começo (o truque do **teletransporte**)

## ✍️ Passo a passo

Tudo acontece dentro do `update()`, depois das linhas da gravidade:

```python
def update():
    global velocidade
    velocidade = velocidade + gravidade
    bird.y = bird.y + velocidade
    cano.x = cano.x - 3
    if cano.x < -50:
        cano.x = 450
```

- `cano.x = cano.x - 3`: a cada frame, o cano anda 3 pixels para a
  **esquerda** (subtrair no x = ir para a esquerda).
- Quando o cano sai pela esquerda, o x dele fica cada vez mais negativo:
  -100, -200... `if cano.x < -50` percebe quando ele já sumiu de vez.
- Aí vem o truque: `cano.x = 450` teletransporta ele para ANTES da borda
  direita (nossa tela tem 400 de largura). Ele entra de novo na tela
  como se fosse um cano novinho!
- É exatamente assim que jogos criam mundos "infinitos": o mesmo cano
  dando voltas, e a gente nem percebe. 🎩✨

## ▶️ Rodando o jogo

```
python jogo.py
```

O cano desliza sem parar e o pássaro voa com ESPAÇO. Já dá para desviar
do cano de verdade — mas bater nele ainda não acontece nada. Capítulo 7!

## ✅ Testando seu capítulo

```
python teste.py
```

## 🧩 Desafios extras (opcional)

1. Deixe o jogo mais rápido: mude o `-3` para `-5`. E mais devagar?
2. Pergunta para pensar: por que usamos `-50` e não `0` no `if`?
   (Dica: o que aconteceria visualmente com `0`?)
