#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Jan 12 13:46:43 2021

@auteur: Christophe Viroulaud
"""


from PIL import Image
mon_image = Image.open("maisons-colorees.bmp")
largeur,hauteur = mon_image.size

nouvelle_image = Image.new("RGB",(largeur,hauteur))
seuil = 128# seuil de gris en-dessous duquel un pixel sera noir
for y in range(hauteur):
    for x in range(largeur):
        pixel = mon_image.getpixel((x,y))
        moyenne = (pixel[0]+pixel[1]+pixel[2])//3

        # si la moyenne des couleurs RVB est inférieure au seuil
        if moyenne < seuil:
            # le pixel sera noir
            r = 0
            v = 0
            b = 0
        else:
            r = 255
            v = 255
            b = 255

        # on place le pixel dans la nouvelle image
        nouvelle_image.putpixel((x,y),(r,v,b))

nouvelle_image.save("maisons-colorees-moyenne.bmp")
nouvelle_image.show()