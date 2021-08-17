#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Oct 23 21:28:07 2020

@auteur: Christophe Viroulaud
"""


from PIL import Image

# récupération de l'image de départ
originale = Image.open("../ressources/joconde.jpg")
ligne, colonne = originale.size

# Création d'une image vide
img = Image.new('RGB', (ligne*2,colonne*2))

#rouge
im_rouge = originale.copy()

for l in range(ligne):
    for c in range(colonne):
        pixel = im_rouge.getpixel((l,c))
        p = (pixel[0],0,0)
        im_rouge.putpixel((l,c), p)

img.paste(im_rouge,(0,0))

#vert
im_vert = originale.copy()

for l in range(ligne):
    for c in range(colonne):
        pixel = im_vert.getpixel((l,c))
        p = (0,pixel[1],0)
        im_vert.putpixel((l,c), p)

img.paste(im_vert,(ligne,0))

#bleu
im_bleu = originale.copy()

for l in range(ligne):
    for c in range(colonne):
        pixel = im_bleu.getpixel((l,c))
        p = (0,0,pixel[2])
        im_bleu.putpixel((l,c), p)

img.paste(im_bleu,(0,colonne))

#violet
im_violet = originale.copy()

for l in range(ligne):
    for c in range(colonne):
        pixel = im_violet.getpixel((l,c))
        p = (pixel[1], 0, pixel[2])
        im_violet.putpixel((l,c), p)

img.paste(im_violet,(ligne,colonne))

img.show()