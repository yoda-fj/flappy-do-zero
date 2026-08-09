"""
🤖 AVALIADOR — motor de testes do curso "Flappy do Zero".

Roda o jogo do aluno de forma INVISÍVEL (sem abrir janela) e verifica
o comportamento de verdade: gravidade, pulo, desenho na tela, etc.

Uso (dentro da pasta de cada capítulo):
    python teste.py            → testa o arquivo jogo.py
    python teste.py outro.py   → testa outro arquivo (uso interno)
"""
import os
import sys
import inspect
import traceback

# Tela e som falsos: o jogo roda sem abrir janela nenhuma
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")

import pygame
from types import ModuleType
from pgzero import loaders, builtins
from pgzero.actor import Actor
import pgzero.screen
import pgzero.game


class Avaliador:
    def __init__(self, titulo, capitulo, total=13):
        self.titulo = titulo
        self.capitulo = capitulo
        self.total = total
        self.resultados = []  # lista de (passou?, nome, dica)
        self.jogo = None
        self.tela = None
        self.caminho = "jogo.py"

    # ---------------------------------------------------------- carregar
    def carregar(self, caminho="jogo.py"):
        """Importa o jogo do aluno com os mesmos poderes que o pgzrun daria."""
        if not os.path.exists(caminho):
            self._falha_fatal(
                f"Não encontrei o arquivo {caminho}!\n"
                "Crie o arquivo jogo.py nesta pasta e escreva seu código nele."
            )
        with open(caminho, encoding="utf-8") as f:
            src = f.read()
        self.caminho = caminho
        try:
            code = compile(src, caminho, "exec", dont_inherit=True)
        except SyntaxError as e:
            linhas = src.splitlines()
            trecho = linhas[e.lineno - 1] if e.lineno and e.lineno <= len(linhas) else ""
            self._falha_fatal(
                f"Tem um erro de digitação na linha {e.lineno} do seu {caminho}:\n\n"
                f"    {trecho}\n\n"
                f'O Python reclamou: "{e.msg}"\n'
                "💡 Compare essa linha com a LICAO.md. Se ela parecer certa, olhe a linha\n"
                "   de CIMA — é comum esquecer de fechar parêntese ou aspas na linha anterior."
            )

        nome = os.path.splitext(os.path.basename(caminho))[0]
        mod = ModuleType(nome)
        mod.__file__ = os.path.abspath(caminho)
        sys.modules[nome] = mod
        loaders.set_root(mod.__file__)
        # O display precisa existir ANTES de carregar imagens (convert_alpha)
        pygame.display.set_mode((100, 100))
        # Se o aluno usar "import pgzrun" + pgzrun.go(), o go() vira no-op aqui:
        # quem manda no loop de teste é o avaliador, não o pgzero.
        sys._pgzrun = True
        mod.__dict__.update(builtins.__dict__)
        try:
            exec(code, mod.__dict__)
        except Exception as e:
            self._falha_fatal(self._explicar_erro(e, caminho))

        largura = int(getattr(mod, "WIDTH", 800))
        altura = int(getattr(mod, "HEIGHT", 600))
        self.tela = pygame.display.set_mode((largura, altura))
        mod.screen = pgzero.screen.Screen(self.tela)
        pgzero.game.screen = self.tela  # Actor.draw() usa este global interno
        self.jogo = mod
        return mod

    # ----------------------------------------------------------- verificar
    def checar(self, nome, condicao, dica=None):
        """Registra uma verificação. `condicao` pode ser valor ou função."""
        try:
            ok = bool(condicao() if callable(condicao) else condicao)
        except Exception as e:
            ok = False
            if dica is None:
                dica = f"(o teste encontrou um erro: {type(e).__name__}: {e})"
        self.resultados.append((ok, nome, dica))
        return ok

    # ----------------------------------------------------------- simular
    def rodar_frames(self, n, dt=1 / 60):
        """Roda o update() do aluno n vezes, como o jogo faria (60x/segundo)."""
        update = getattr(self.jogo, "update", None)
        if update is None:
            return
        com_dt = len(inspect.signature(update).parameters) > 0
        for _ in range(n):
            update(dt) if com_dt else update()

    def apertar(self, tecla):
        """Simula o aluno apertando uma tecla (ex.: self.jogo.keys.R)."""
        handler = getattr(self.jogo, "on_key_down", None)
        if handler:
            handler(tecla)

    def apertar_espaco(self):
        """Simula o aluno apertando a tecla ESPAÇO."""
        self.apertar(self.jogo.keys.SPACE)

    def desenhar(self):
        """Roda o draw() do aluno. Registra falha se der erro."""
        try:
            self.jogo.draw()
            return True
        except Exception as e:
            self.checar("a função draw() roda sem erros", False,
                        dica=self._explicar_erro(e, self.caminho))
            return False

    def pixel(self, x, y):
        """Cor (r, g, b) de um ponto da tela depois do draw()."""
        x = max(0, min(int(x), self.tela.get_width() - 1))
        y = max(0, min(int(y), self.tela.get_height() - 1))
        return self.tela.get_at((x, y))[:3]

    # ----------------------------------------------------------- relatório
    def relatorio(self):
        print()
        print("=" * 48)
        print(f"🐤 {self.titulo}")
        print("=" * 48)
        acertos = 0
        for ok, nome, dica in self.resultados:
            print(("✅" if ok else "❌"), nome)
            if ok:
                acertos += 1
            elif dica:
                for i, linha in enumerate(str(dica).splitlines()):
                    print(("   💡 " if i == 0 else "      ") + linha)
        total = len(self.resultados)
        print("-" * 48)
        if acertos == total:
            print(f"🎉 PARABÉNS! Capítulo {self.capitulo} completo ({acertos}/{total})!")
            print(f"   Progresso: {self.capitulo} de {self.total} capítulos do jogo.")
            if self.capitulo < self.total:
                print("   Próximo passo: abra a pasta do próximo capítulo e leia a LICAO.md")
            else:
                print("   🏆 CURSO COMPLETO! Você programou um Flappy Bird inteiro!")
                print("   Compartilhe o jogo com a família — e invente suas próprias fases!")
            sys.exit(0)
        else:
            print(f"Quase lá! {acertos} de {total} verificações passaram.")
            print("Corrija o que está com ❌ e rode o teste de novo:")
            print("    python teste.py")
            sys.exit(1)

    # ----------------------------------------------------------- internos
    def _falha_fatal(self, mensagem):
        print()
        print("=" * 48)
        print(f"🐤 {self.titulo}")
        print("=" * 48)
        print("❌ Não consegui rodar o seu jogo:")
        print()
        print(mensagem)
        sys.exit(1)

    def _explicar_erro(self, e, caminho):
        """Traduz erros do Python para uma linguagem amigável."""
        tb = traceback.extract_tb(e.__traceback__)
        frames_jogo = [f for f in tb if os.path.basename(f.filename) == os.path.basename(caminho)]
        if frames_jogo:
            onde = f"na linha {frames_jogo[-1].lineno} do seu código"
            trecho = frames_jogo[-1].line or ""
        else:
            onde, trecho = "ao carregar", ""

        msg = f"Seu jogo deu erro {onde}:\n\n    {trecho}\n\n"
        if isinstance(e, NameError):
            nome = str(e).split("'")[1] if "'" in str(e) else "?"
            msg += (f"O nome '{nome}' não foi criado ainda.\n"
                    "💡 Confira a digitação (Python diferencia MAIÚSCULAS de minúsculas)\n"
                    "   e veja se você criou essa variável ANTES da linha que usa ela.")
        elif isinstance(e, (FileNotFoundError, pygame.error)) and (
                "No such file" in str(e) or "couldn't open" in str(e).lower()):
            msg += ("Não achei um arquivo de imagem que o jogo pediu.\n"
                    "💡 A pasta images/ precisa estar JUNTO do jogo.py, com o arquivo\n"
                    "   dentro (ex.: images/bird.png). Nome tudo em minúsculo, sem espaço.")
        else:
            msg += (f"Erro: {type(e).__name__}: {e}\n"
                    "💡 Mostre essa mensagem para um adulto ou compare com o gabarito.py.")
        return msg
