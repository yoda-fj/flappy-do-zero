"""Gera as imagens do curso (bird.png etc.) em cada capítulo.

Uso:  python ferramentas/gerar_imagens.py

As imagens são simples de propósito: no capítulo 10 (polimento) uma das
sugestões é a criança desenhar o próprio pássaro e substituir o arquivo.
"""
import os
from PIL import Image, ImageDraw

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CAPITULOS_COM_PASSARO = [
    "capitulo-02-o-passaro",
    "capitulo-03-gravidade",
    "capitulo-04-o-pulo",
]


def gerar_passaro(caminho):
    img = Image.new("RGBA", (50, 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # corpo
    d.ellipse((2, 2, 44, 38), fill=(255, 220, 0, 255), outline=(200, 150, 0, 255))
    # asa
    d.ellipse((10, 14, 30, 30), fill=(240, 180, 0, 255), outline=(200, 150, 0, 255))
    # bico
    d.polygon([(44, 16), (50, 21), (44, 26)], fill=(255, 140, 0, 255))
    # olho
    d.ellipse((28, 8, 40, 20), fill=(255, 255, 255, 255))
    d.ellipse((32, 12, 38, 18), fill=(30, 30, 30, 255))
    img.save(caminho)
    print("criado:", caminho)


def main():
    for capitulo in CAPITULOS_COM_PASSARO:
        pasta = os.path.join(RAIZ, capitulo, "images")
        os.makedirs(pasta, exist_ok=True)
        gerar_passaro(os.path.join(pasta, "bird.png"))


if __name__ == "__main__":
    main()
