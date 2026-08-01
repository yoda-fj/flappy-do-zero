# 🐤 Capítulo 4 — O pulo

## 🎯 O que vamos fazer

Este é o capítulo mais importante: o pássaro vai **voar**! Apertando a
barra de ESPAÇO, ele pula para cima; soltando, a gravidade puxa de volta.
No final, você já consegue JOGAR (ainda sem canos).

## 📖 Coisas novas que você vai aprender

- **Velocidade**: uma variável que guarda "para onde e quão rápido"
- A palavra **global** (usar uma variável de fora dentro da função)
- A função **on_key_down()**: reagir ao teclado
- O **if**: fazer algo SOMENTE SE uma condição for verdade

## 🤔 Primeiro, um problema para pensar

No capítulo 3, o pássaro caía sempre na mesma velocidade (+3 por frame).
Mas um pássaro de verdade não cai assim: ele vai caindo cada vez MAIS
RÁPIDO. E para pular, ele precisa de uma força para cima que vai
enfraquecendo aos poucos.

A solução dos jogos é guardar a velocidade numa **variável**, em vez de
usar um número fixo. É por isso que neste capítulo vamos SUBSTITUIR o
update antigo por um novo.

## ✍️ Passo a passo

### 1. As duas variáveis novas (lá em cima, perto do bird)

```python
gravidade = 0.5
velocidade = 0
```

- `gravidade` = quanto a velocidade aumenta a cada frame (para baixo).
- `velocidade` = quão rápido o pássaro está se movendo NESTE momento.
  Começa em 0 (parado). Positivo = caindo. Negativo = subindo.

### 2. O update novo (SUBSTITUA o antigo)

```python
def update():
    global velocidade
    velocidade = velocidade + gravidade
    bird.y = bird.y + velocidade
```

- `global velocidade` = "a velocidade que vou mexer aqui dentro é aquela
  lá de fora, não uma nova". Sem essa linha, o Python criaria uma
  velocidade separada que some quando a função termina.
- Linha 2: a gravidade puxa a velocidade para baixo a cada frame.
  Repare que 0.5 é pequeno — mas somando 60 vezes por segundo, acumula!
- Linha 3: o pássaro se move de acordo com a velocidade atual.
- Agora o pássaro cai devagar no começo e vai ganhando velocidade.
  Igualzinho à vida real! 🍎

### 3. Reagindo ao teclado (embaixo de tudo)

```python
def on_key_down(key):
    global velocidade
    if key == keys.SPACE:
        velocidade = -8
```

- `on_key_down` é outro nome especial: o Pygame Zero chama essa função
  TODA VEZ que uma tecla é apertada, e conta qual foi na variável `key`.
- `if` = "se". O código com recuo embaixo dele só roda SE a condição
  for verdade. Repare no `==` (DOIS sinais de igual): UM `=` guarda,
  DOIS `==` compara. Esse é um dos erros mais famosos da programação!
- `keys.SPACE` é a barra de espaço.
- `velocidade = -8`: negativo = para CIMA. O pulo é um empurrão forte
  para cima — e a gravidade vai comendo esse empurrão aos poucos, até
  o pássaro parar de subir e começar a cair de novo. Física de verdade!

## ▶️ Rodando o jogo

```
pgzrun jogo.py
```

Aperte ESPAÇO várias vezes seguidas e mantenha o pássaro voando.
PARABÉNS — você está jogando o seu próprio jogo! 🎮

## ✅ Testando seu capítulo

```
python teste.py
```

## 🧩 Desafios extras (opcional)

1. Deixe o pulo mais forte ou mais fraco mudando o `-8`.
2. Deixe a gravidade da Lua: mude `0.5` para `0.2`. E a de Júpiter: `1.0`.
3. **Desafio difícil:** impeça o pássaro de sair voando pelo TETO.
   Dica: dentro do update, use `if bird.y < 0: bird.y = 0`.
