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


def rotation(px: object, x: int, y: int, t: int) -> None:
    if t > 1:
        t //= 2
        rotation(px, x, y, t)
        rotation(px, x+t, y, t)
        rotation(px, x, y+t, t)
        rotation(px, x+t, y+t, t)

        tourner(px, x, y, t)


im = Image.open("angry.png")
largeur, hauteur = im.size
px = im.load()

im.show()
rotation(px, 0, 0, largeur)

im.show()
# im.save("rotation.png")
