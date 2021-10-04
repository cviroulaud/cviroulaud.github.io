#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Sep 28 11:01:42 2020

@auteur: Christophe Viroulaud
"""


from PIL import Image

def rotation_auxiliaire(px: object, x: int, y: int, t: int)->None:
    if t == 1:
        # on ne fait rien: inutile de tourner 1 pixel carré
        return
    else:
        t //= 2
        rotation_auxiliaire(px, x, y, t)
        rotation_auxiliaire(px, x+t, y, t)
        rotation_auxiliaire(px, x, y+t, t)
        rotation_auxiliaire(px, x+t, y+t, t)

    for l in range(x, x+t):
        for c in range(y, y+t):
            px[x1,y1+t], px[x1+t,y1+t], px[x1+t,y1  ], px[x1  ,y1] = \
            px[x1,y1  ], px[x1  ,y1+t], px[x1+t,y1+t], px[x1+t,y1]

def rotation(px: object, taille: int)->None:
    rotation_auxiliaire(px, 0, 0, taille)

im = Image.open("../ressources/angry.png")
largeur, hauteur = im.size
px = im.load()

im.show()
rotation(px, largeur)
im.show()
#im.save("rotation.png")