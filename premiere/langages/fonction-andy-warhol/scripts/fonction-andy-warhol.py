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

def img_filtree(image, R, V, B):
    for l in range(ligne):
        for c in range(colonne):
            pixel = image.getpixel((l,c))
            # les valeurs doivent être des entiers
            p = (int(pixel[0]*R), int(pixel[1]*V), int(pixel[2]*B))
            image.putpixel((l,c), p)

    return image

im_rouge = img_filtree(originale.copy(), 1, 0, 0)
im_vert = img_filtree(originale.copy(), 0, 1, 0)
im_bleu = img_filtree(originale.copy(), 0, 0, 1)
im_mix = img_filtree(originale.copy(), 1, 0, 1)

img.paste(im_rouge,(0,0))
img.paste(im_vert,(ligne,0))
img.paste(im_bleu,(0,colonne))
img.paste(im_mix,(ligne,colonne))

img.show()