#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 20 Septembre 2021 22:21
"""

from PIL import Image


def trait_vertical(image, x, debut, fin, couleur):
    for y in range(debut, fin):
        image.putpixel((x, y), couleur)


def trait_horizontal(image, y, debut, fin, couleur):
    for x in range(debut, fin):
        image.putpixel((x, y), couleur)


def carre(image, o_x, o_y, longueur, couleur):
    for x in range(o_x, o_x+longueur):
        for y in range(o_y, o_y+longueur):
            image.putpixel((x, y), couleur)


def cercle(image, o_x, o_y, rayon, couleur):
    for x in range(-rayon, rayon):
        image.putpixel((o_x+x, o_y+int((rayon**2-x**2)**0.5)), couleur)
        image.putpixel((o_x+x, o_y-int((rayon**2-x**2)**0.5)), couleur)


def disque(image, o_x, o_y, rayon, couleur):
    for x in range(-rayon, rayon):
        for y in range(-rayon, rayon):
            if x**2+y**2 <= rayon**2:
                image.putpixel((o_x+x, o_y+y), couleur)
