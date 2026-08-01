# 📋 PLANO — Capítulos 5 a 10

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

---

## Ideias para depois do curso (página "e agora?")

- Sons com `sounds.pulo.play()` (precisa pasta `sounds/`)
- Recorde salvo em arquivo
- Dia/noite alternando a cor do céu
- Publicar o jogo para os amigos com pygbag (roda no navegador)
