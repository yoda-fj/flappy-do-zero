# 🐤 Capítulo 1 — Acendendo a tela

## 🎯 O que vamos fazer

Todo jogo começa com uma janela. Neste capítulo você vai criar a janela
do seu jogo e pintar o fundo com a cor do céu. Parece pouco, mas é o
palco onde tudo vai acontecer!

## 📖 Coisas novas que você vai aprender

- O que é uma **variável** (um nome que guarda um valor)
- O que é uma **função** (um bloco de instruções com um nome)
- Cores no computador: **RGB**

## ✍️ Passo a passo

Abra o arquivo `jogo.py` e digite o código abaixo.
**Digite você mesmo, não copie e cole!** É digitando que o cérebro aprende.

### As duas primeiras linhas — o tamanho da janela

```python
WIDTH = 400
HEIGHT = 600
```

- `WIDTH` significa **largura** e `HEIGHT` significa **altura** (em inglês).
- Aqui criamos duas **variáveis**: nomes que guardam valores.
  `WIDTH = 400` quer dizer: "guarde o número 400 dentro do nome WIDTH".
- Esses dois nomes são especiais: o Pygame Zero procura por eles para
  saber o tamanho da janela. Por isso precisam ser escritos ASSIM,
  em letras MAIÚSCULAS.
- 400 e 600 são medidas em **pixels** — os pontinhos que formam a tela.
  Nossa janela terá 400 pixels de largura e 600 de altura: mais alta do
  que larga, igual à tela de um celular em pé. Perfeito para o Flappy!

### A função que desenha

```python
def draw():
    screen.fill((135, 206, 235))
```

- `def` vem de "definir". Estamos **definindo uma função**: um bloco de
  instruções com um nome.
- `draw` (desenhar, em inglês) é outro nome especial: o Pygame Zero chama
  essa função **60 vezes por segundo**, o tempo todo, para desenhar a tela.
- A linha de baixo começa com **4 espaços**. Isso se chama **indentação**
  e é SUPER importante no Python: é assim que ele sabe que essa linha
  faz parte da função `draw`.
- `screen` é a tela do jogo e `fill` é "preencher". Então
  `screen.fill(...)` = "preencha a tela inteira com esta cor".
- A cor é escrita com 3 números: **(vermelho, verde, azul)** — a sigla
  **RGB** (Red, Green, Blue). Cada número vai de 0 a 255, e misturando
  as três luzes você cria qualquer cor! `(135, 206, 235)` é um azul-céu.
  - `(255, 0, 0)` → vermelho puro
  - `(0, 0, 0)` → preto
  - `(255, 255, 255)` → branco

## ▶️ Rodando o jogo

No terminal, dentro desta pasta, digite:

```
pgzrun jogo.py
```

(ou dê duplo clique no arquivo `jogar.bat`)

Você deve ver uma janela azul-céu. Ela fica aberta até você fechar.

## ✅ Testando seu capítulo

```
python teste.py
```

(ou duplo clique em `testar.bat`)

O avaliador roda o seu jogo sem abrir janela e verifica se está tudo
certo. Se algo estiver errado, ele dá uma dica. Todos os ✅? Capítulo completo!

## 🧩 Desafio extra (opcional)

Mude a cor do fundo para a sua cor favorita. Descubra os números RGB
misturando os três valores, ou pesquise "rgb color picker" na internet.
