# 🐤 Capítulo 7 — Colisão

## 🎯 O que vamos fazer

Hora do perigo de verdade: se o pássaro encostar no cano, **o jogo
congela** — fim da brincadeira. É a colisão que transforma um passarinho
voando em um JOGO com desafio.

## 📖 Coisas novas que você vai aprender

- **colliderect**: perguntar se dois Actors estão se tocando
- Variável **verdadeiro/falso** (booleana) para guardar o estado do jogo
- A palavra **not** (não)
- "Congelar" o jogo pulando o update

## ✍️ Passo a passo

### 1. A variável de estado (lá em cima)

```python
morreu = False
```

- `morreu` guarda o ESTADO do jogo: `False` (falso = jogando) ou
  `True` (verdadeiro = bateu). Variáveis que só valem verdadeiro ou
  falso se chamam **booleanas** — são os interruptores do programa.

### 2. O update com trava de segurança (SUBSTITUA o update inteiro)

```python
def update():
    global velocidade, morreu
    if not morreu:
        velocidade = velocidade + gravidade
        bird.y = bird.y + velocidade
        cano.x = cano.x - 3
        if cano.x < -50:
            cano.x = 450
        if bird.colliderect(cano):
            morreu = True
```

- `global velocidade, morreu`: dá para listar várias variáveis com
  vírgula! Precisamos mexer nas duas.
- `if not morreu:` = "se NÃO morreu". Todo o miolo do update ficou com
  mais um recuo de 4 espaços, porque agora ele só roda ENQUANTO o
  jogador está vivo. Quando `morreu` vira True: tudo congela. 🧊
- `bird.colliderect(cano)` pergunta: "os retângulos do pássaro e do
  cano estão se encostando?". Responde True ou False — perfeito para um if.
- `morreu = True`: bateu! O interruptor desliga o jogo no próximo frame.

### 3. O pulo também trava (pequeno ajuste no on_key_down)

```python
def on_key_down(key):
    global velocidade
    if key == keys.SPACE and not morreu:
        velocidade = -8
```

- `and` = "e". O pulo só funciona se as DUAS coisas forem verdade:
  a tecla é ESPAÇO **e** o pássaro não morreu.

## ▶️ Rodando o jogo

```
python jogo.py
```

Voe e encoste no cano de propósito: TUDO para. O jogo finalmente tem
medo e perigo! (No capítulo 9 a gente coloca o botão de recomeçar.)

## ✅ Testando seu capítulo

```
python teste.py
```

## 🧩 Desafio extra (opcional)

O que acontece se a linha `morreu = True` ficar FORA do `if` da colisão?
Teste, veja o efeito, e explique para alguém (ou para o seu pato de
borracha 🦆) por que o jogo ficou quebrado.
