#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Jan 12 13:46:43 2021

@auteur: Christophe Viroulaud
"""

# Première étape: stocker les images
from PIL import Image
image_visible = # à compléter
image_secrete = # à compléter

colonne, ligne = image_visible.size

# Deuxième étape: parcourir la grille pour modifier chaque pixel
for y in range(ligne):
    for x in range(colonne):
        # garde les bits de poids fort de l'image visible
        pixel_visible = image_visible.getpixel((x,y))
        r1 = pixel_visible[0]&240
        v1 = pixel_visible[1]&240
        b1 = pixel_visible[2]&240

        # garde les bits de poids fort de l'image secrète
        pixel_secret = image_secrete.getpixel((x,y))
        r2 = pixel_secret[0]>>4
        v2 = pixel_secret[1]>>4
        b2 = pixel_secret[2]>>4

        # replace le nouveau pixel
        image_visible.putpixel((x,y), (r1|r2, v1|v2, b1|b2))

# Troisième étape: enregistrer l'image
image_visible.save("image-finale.bmp")
image_visible.show()
