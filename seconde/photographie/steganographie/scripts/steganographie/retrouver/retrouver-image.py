#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Jan 12 13:46:43 2021

@auteur: Christophe Viroulaud
"""

# Première étape: stocker les images
from PIL import Image
image_visible = # à compléter

colonne, ligne = image_visible.size

# Deuxième étape: parcourir la grille pour modifier chaque pixel
for y in range(ligne):
    for x in range(colonne):
        # garde les bits de poids faible de l'image visible
        pixel_visible = image_visible.getpixel((x,y))
        r = pixel_visible[0]<<4&255
        v = pixel_visible[1]<<4&255
        b = pixel_visible[2]<<4&255

        # on replace le nouveau pixel
        image_visible.putpixel((x,y), (r, v, b))

# Troisième étape: enregistrer l'image
image_visible.save("image-retrouvee.bmp")
image_visible.show()
