# 📋 PLANO — Capítulos 5 a 13

Filosofia do curso (vale para todos os capítulos):

1. **Uma novidade por capítulo.** O jogo nunca dá um salto grande.
2. **A lição explica cada linha**, sempre com o "por quê", não só o "o quê".
3. **O teste verifica comportamento, não código.** Resolver de outro jeito
   e funcionar = passou. Isso ensina a pensar, não a copiar.
4. **Erros clássicos viram dicas.** Cada verificação tem uma dica escrita
   para o erro que uma criança realmente cometeria ali.
5. Feedback sempre em português, encorajador, com 💡 dica acionável.

---

## Capítulo 5 — O primeiro cano
- **Conceito novo:** mais um Actor; aparecer fora da tela (x > WIDTH)
- **Código novo:** `cano = Actor("pipe", (450, 300))` + `cano.draw()`
- **Imagem nova:** `images/pipe.png` (gerar com ferramentas/gerar_imagens.py)
- **Testes:** cano existe, é Actor, começa à direita da tela, aparece no draw
- **Erro clássico:** esquecer `cano.draw()` → cano invisível

## Capítulo 6 — Canos em movimento
- **Conceito novo:** mover no eixo x; "voltar pro começo" com if
- **Código novo:** no update: `cano.x = cano.x - 3` e
  `if cano.x < -50: cano.x = 450`
- **Testes:** cano anda para a esquerda; depois de sair da tela, reaparece
  à direita; o pássaro continua caindo/pulando (cap. 4 não quebrou)
- **Erro clássico:** mover com `+` (cano vai pra direita e some pra sempre)

## Capítulo 7 — Colisão
- **Conceito novo:** `colliderect`; estado do jogo (variável `morreu`)
- **Código novo:** `if bird.colliderect(cano): morreu = True` e o update
  para de mover quando morreu
- **Testes:** simular cano passando pela posição do pássaro → `morreu`
  vira True; sem colisão, continua False
- **Erro clássico:** checar colisão uma vez só, fora do update

## Capítulo 8 — Pontuação
- **Conceito novo:** variável contadora; desenhar texto com
  `screen.draw.text()`
- **Código novo:** `pontos = 0`; quando o cano passa do pássaro,
  `pontos = pontos + 1`; no draw: `screen.draw.text(str(pontos), ...)`
- **Testes:** simular cano ultrapassando o pássaro → pontos aumenta;
  texto aparece na tela (pixel da área do placar muda)
- **Erro clássico:** esquecer `str(pontos)` no texto

## Capítulo 9 — Game over e recomeço
- **Conceito novo:** telas/estados; reiniciar variáveis numa função
- **Código novo:** função `recomecar()` que zera tudo; tecla R chama ela;
  texto "GAME OVER" quando morreu
- **Testes:** morrer → jogo para; apertar R → posições e pontos zeram
  e o jogo volta
- **Erro clássico:** recomeçar mas esquecer de zerar a velocidade
  (pássaro renasce caindo rápido)

## Capítulo 10 — Polimento (projeto livre guiado)
- **Conceito novo:** revisão geral; duas metades de cano com buraco;
  número aleatório com `random`
- **Código novo:** cano de cima + cano de baixo com espaço no meio;
  altura do buraco sorteada a cada cano; opcional: `bird.angle` girando
- **Testes:** existe um buraco entre os canos; o buraco muda de altura;
  tudo dos capítulos anteriores continua funcionando (teste de regressão!)
- **Final:** 🏆 certificado "Eu programei meu primeiro jogo"

## Capítulo 11 — A tela inicial ✅ implementado
- **Conceito novo:** estado do jogo (variável `comecou`); `and` no if;
  if/elif/else dando três empregos para a mesma tecla
- **Código novo:** `comecou = False`; update vira `if comecou and not morreu:`;
  draw mostra título quando não começou; ESPAÇO: começa / joga de novo / pula;
  `recomecar()` liga `comecou = True`
- **Testes:** mundo congelado antes do começo (bird.y e cano.x não mudam);
  título visível (pixels na faixa do título); ESPAÇO começa; gravidade volta;
  pulo, colisão e R como regressão
- **Erro clássico:** esquecer `comecou` no `global` do on_key_down
  (jogo nunca começa)

## Capítulo 12 — Cenário com parallax ✅ implementado
- **Conceito novo:** parallax (camadas em velocidades diferentes);
  duas cópias da mesma imagem para chão infinito
- **Código novo:** `grama1/grama2` (400px de largura, y=570) e
  `nuvem1/nuvem2`; grama anda -3 (com os canos), nuvem -1;
  teletransportes: grama -200→600, nuvem -70→470; draw: céu → nuvens →
  canos → pássaro → grama → textos
- **Imagens novas:** `images/grass.png` e `images/cloud.png`
  (ferramentas/gerar_imagens.py)
- **Testes:** atores por nome de imagem (`actor.image`); medição real das
  velocidades (grama > nuvem); teletransporte dos dois; pixel verde no pé
  da tela; regressão de pontos/colisão/recomeço
- **Erro clássico:** nuvem na mesma velocidade da grama (sem parallax)

## Capítulo 13 — O recorde ✅ implementado
- **Conceito novo:** variáveis que SOBREVIVEM ao recomeço (recorde não
  entra no recomecar); comparação com `>`; variável bandeira
  (`novo_recorde`)
- **Código novo:** `recorde = 0` e `novo_recorde = False`; na morte:
  `if pontos > recorde: recorde = pontos; novo_recorde = True`; draw do
  game over mostra "NOVO RECORDE!" (amarelo) ou "Recorde: X"; recorde
  também aparece na tela inicial quando > 0
- **Testes:** três partidas simuladas em sequência — recorde vira 3,
  sobrevive ao recomeço, não desce com 1 ponto, sobe para 7 com festa
  amarela na tela (pixel amarelo na faixa do texto); regressão de
  recomeço e pulo
- **Erro clássico:** zerar o recorde dentro do recomecar()

---

## Ideias para depois do curso (página "e agora?")

- Sons com `sounds.pulo.play()` (precisa pasta `sounds/`)
- Recorde salvo em arquivo
- Dia/noite alternando a cor do céu
- Publicar o jogo para os amigos com pygbag (roda no navegador)
