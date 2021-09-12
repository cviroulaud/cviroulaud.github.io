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

        # on replace le nouveau pixel
        mon_image.putpixel((x,y), (pixel[0], 0, 0))

# Troisième étape: enregistrer l'image
mon_image.save("maisons-colorees-rouge.bmp")
mon_image.show()
