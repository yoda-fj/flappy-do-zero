# 🐤 Capítulo 9 — Game over e recomeço

## 🎯 O que vamos fazer

Bater no cano e o jogo simplesmente congelar é frustrante. Todo jogo que
se preza mostra **GAME OVER** e deixa o jogador tentar DE NOVO. Vamos
colocar os dois!

## 📖 Coisas novas que você vai aprender

- Criar uma **função sua** (não só as prontas do Pygame Zero)
- **Reiniciar** variáveis para o estado inicial
- Responder a **duas teclas** diferentes
- Mostrar texto **só às vezes** (if dentro do draw)

## ✍️ Passo a passo

### 1. A função de recomeçar (antes do draw)

```python
def recomecar():
    global velocidade, pontos, morreu
    bird.y = 300
    velocidade = 0
    cano.x = 350
    pontos = 0
    morreu = False
```

- `recomecar` não é um nome especial do Pygame Zero — é um nome que NÓS
  inventamos! Funções assim guardam um pedaço de tarefa para usar depois.
- Recomeçar = colocar TUDO de volta no lugar: pássaro no meio, velocidade
  zerada, cano na direita, placar no zero, e o interruptor `morreu`
  desligado.
- ⚠️ Esquecer de zerar a **velocidade** é o bug clássico: o pássaro
  renasce já despencando rapidão e morre de novo na hora!

### 2. A tecla R (no on_key_down)

```python
def on_key_down(key):
    global velocidade
    if key == keys.SPACE and not morreu:
        velocidade = -8
    if key == keys.R:
        recomecar()
```

- Um `if` para cada tecla. Apertou R? Chama nossa função. Repare que são
  dois ifs separados, não `else` — ESPAÇO e R são independentes.

### 3. O aviso de GAME OVER (no draw, no final)

```python
    if morreu:
        screen.draw.text("GAME OVER", center=(200, 250), fontsize=60, color="red")
        screen.draw.text("Aperte R para recomecar", center=(200, 320), fontsize=30, color="white")
```

- `center=(200, 250)` centraliza o texto num ponto — metade da largura
  (400 ÷ 2 = 200) e um pouco acima do meio da altura.
- O `if` faz o texto só aparecer quando morreu. Jogando? Tela limpa.

## ▶️ Rodando o jogo

```
python jogo.py
```

Bata no cano, veja o GAME OVER, aperte R e jogue de novo. E de novo.
E de novo. Seu jogo agora é INFINITAMENTE rejogável! 🔁

## ✅ Testando seu capítulo

```
python teste.py
```

## 🧩 Desafio extra (opcional)

Adicione uma variável `recorde` que guarda a maior pontuação da sessão
e aparece na tela de GAME OVER. Você vai precisar de mais um global!
