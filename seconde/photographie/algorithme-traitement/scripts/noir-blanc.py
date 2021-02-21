#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Jan 12 13:46:43 2021

@auteur: Christophe Viroulaud
"""

# Première étape: stocker l'image
from PIL import Image
mon_image = Image.open("maisons-colorees.bmp")
colonne, ligne = mon_image.size

# Deuxième étape: parcourir la grille pour modifier chaque pixel
for y in range(ligne):
    for x in range(colonne):
        # récupérer le pixel
        pixel = mon_image.getpixel((x,y))

        moyenne = (pixel[0] + pixel[1] + pixel[2]) // 3
        # si la moyenne des couleurs RVB est inférieure à un seuil
        if moyenne < 128:
            # le pixel sera noir
            r = 0
            v = 0
            b = 0
        else:
            # le pixel sera blanc
            r = 255
            v = 255
            b = 255

        # on replace le nouveau pixel
        mon_image.putpixel((x,y), (r,v,b))

# Troisième étape: enregistrer l'image
mon_image.save("maisons-colorees-NB.bmp")
mon_image.show()