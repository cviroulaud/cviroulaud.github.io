#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Sep 28 11:01:42 2020

@auteur: Christophe Viroulaud
"""


from PIL import Image


def tourner(px: object, x: int, y: int, t: int) -> None:
    for l in range(y, y+t):
        for c in range(x, x+t):
            px[l, c+t], px[l+t, c+t], px[l+t, c], px[l, c] = \
                px[l, c], px[l, c+t], px[l+t, c+t], px[l+t, c]


def rotation_auxiliaire(px: object, x: int, y: int, t: int) -> None:
    if t == 1:
        # on ne fait rien: inutile de continuer à découper
        return
    else:
        t //= 2
        rotation_auxiliaire(px, x, y, t)
        rotation_auxiliaire(px, x+t, y, t)
        rotation_auxiliaire(px, x, y+t, t)
        rotation_auxiliaire(px, x+t, y+t, t)

    tourner(px, x, y, t)


def rotation(px: object, taille: int) -> None:
    rotation_auxiliaire(px, 0, 0, taille)


im = Image.open("../ressources/carre2.png")
largeur, hauteur = im.size
px = im.load()

im.show()
rotation(px, largeur)
im.show()
# im.save("rotation.png")
