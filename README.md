# 🐤 Flappy do Zero

**Curso de programação para crianças: construa o jogo Flappy Bird linha por linha, com um avaliador automático que corrige cada capítulo.**

Feito para crianças a partir de ~10 anos, sem nenhuma experiência anterior.
Linguagem: **Python** com **Pygame Zero**.

## Como o curso funciona

- O jogo é dividido em **13 capítulos pequenos**. Cada capítulo adiciona
  UMA coisa: a janela, o pássaro, a gravidade, o pulo, os canos...
- Cada capítulo tem uma pasta com:
  - **`LICAO.md`** — a lição, explicando cada linha de código
  - **`jogo.py`** — onde a criança escreve o código dela
  - **`teste.py`** — o avaliador automático 🤖
  - **`gabarito.py`** — a solução (só olhar depois de tentar!)
  - **`jogar.bat` / `testar.bat`** — atalhos de duplo clique no Windows
- O avaliador roda o jogo da criança **de verdade** (sem abrir janela),
  simula frames e teclas, e dá feedback em português com dicas:

```
🐤 Capítulo 4 — O pulo
✅ a função update() existe
✅ a função on_key_down() existe
✅ a gravidade derruba o pássaro
❌ apertar ESPAÇO faz o pássaro subir
   💡 Dentro de on_key_down, use:
      if key == keys.SPACE:
          velocidade = -8
```

Importante: o teste verifica o **comportamento**, não se o código está
igual ao gabarito. Se a criança resolver do jeito dela e funcionar, passa.

## Capítulos

| # | Capítulo | Status |
|---|----------|--------|
| 1 | Acendendo a tela (janela + cor de fundo) | ✅ pronto |
| 2 | O pássaro aparece (Actor, coordenadas) | ✅ pronto |
| 3 | A gravidade (update, variáveis que mudam) | ✅ pronto |
| 4 | O pulo (teclado, if, velocidade) | ✅ pronto |
| 5 | O primeiro cano (vários Actors, ordem do draw) | ✅ pronto |
| 6 | Canos em movimento (eixo x, teletransporte) | ✅ pronto |
| 7 | Colisão (colliderect, booleanos, not) | ✅ pronto |
| 8 | Pontuação (contador, str, texto na tela) | ✅ pronto |
| 9 | Game over e recomeço (funções próprias, reset) | ✅ pronto |
| 10 | O grande final (cano duplo, random, regressão) | ✅ pronto |
| 11 | A tela inicial (estados do jogo, and, elif) | ✅ pronto |
| 12 | Cenário com parallax (grama, nuvens, camadas) | ✅ pronto |
| 13 | O recorde (variáveis que sobrevivem ao recomeço, >) | ✅ pronto |

**Branch `solucao`:** versão com o `jogo.py` de cada capítulo já preenchido,
para os pais verem o jogo pronto:
<https://github.com/yoda-fj/flappy-do-zero/archive/refs/heads/solucao.zip>

## 🪟 Instalação no Windows (guia para os pais)

**1. Instale o Python**

- Baixe em <https://www.python.org/downloads/> (botão amarelo "Download Python")
- ⚠️ **Na primeira tela da instalação, marque a caixa
  "Add python.exe to PATH"** — isso é essencial!
- Depois clique em "Install Now"

**2. Baixe este curso**

Duas opções:

- **Mais fácil:** clique no botão verde **"Code" → "Download ZIP"** aqui
  no GitHub e extraia a pasta em algum lugar (ex.: Documentos)
- **Com Git:** `git clone https://github.com/yoda-fj/flappy-do-zero.git`

**3. Instale o Pygame Zero**

Abra o **Prompt de Comando** (tecla Windows, digite `cmd`, Enter) e rode:

```
pip install pgzero
```

Se disser que `pip` não é reconhecido, tente `py -m pip install pgzero`.

**3b. (Opcional) Prefere isolar num ambiente virtual (venv)?**

Para uma criança, o passo 3 simples já basta — mas se você quer manter o
Python do Windows limpo, crie um venv **na pasta do curso**:

```
cd caminho\para\flappy-do-zero
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Os arquivos `jogar.bat` e `testar.bat` detectam o `.venv` automaticamente:
se ele existir, usam o Python dele; se não, usam o global. No terminal,
lembre de ativar o venv (`.venv\Scripts\activate`) antes de rodar
`pgzrun jogo.py` ou `python teste.py` na mão.

**4. Comece a jogar (a criança assume daqui 🙂)**

- Abra a pasta `capitulo-01-a-janela` e leia o arquivo `LICAO.md`
- Para escrever o código, qualquer editor serve: o **IDLE** já vem
  instalado com o Python; **VS Code** é outra boa opção
- Para rodar o jogo: `python jogo.py` dentro da pasta do capítulo
  (também funciona: `pgzrun jogo.py`, F5 no IDLE, ou duplo clique em
  `jogar.bat` no Windows)
- Para corrigir o capítulo: duplo clique em `testar.bat` (ou `python teste.py`)

## Dicas para os pais

- **Deixe a criança digitar.** Copiar e colar não ensina; errar e ler a
  dica do avaliador, sim.
- Ritmo sugerido: 1 capítulo por sessão (20–40 min cada).
- O `gabarito.py` existe para destravar, não para copiar de primeira.
- Se o avaliador passar mas a criança quiser mudar cores, velocidades,
  posições — ótimo! Experimentar faz parte (os "Desafios extras" no fim
  de cada lição incentivam isso).

## Estrutura do repositório

```
flappy-do-zero/
├── avaliador.py          ← motor dos testes (compartilhado)
├── capitulo-01-a-janela/
├── capitulo-02-o-passaro/
├── capitulo-03-gravidade/
├── capitulo-04-o-pulo/
├── ferramentas/          ← scripts de manutenção do curso
├── PLANO.md              ← roadmap dos capítulos 5–13
└── requirements.txt
```
