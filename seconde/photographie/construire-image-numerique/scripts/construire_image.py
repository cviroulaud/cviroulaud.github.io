#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 20 Septembre 2021 22:21
"""

from PIL import Image
from random import randint


def trait_horizontal(position):
    for x in range(800):
        image.putpixel((x, position), (0, 0, 0))


def trait_vertical(position):
    for y in range(600):
        image.putpixel((position, y), (0, 0, 0))


def trait_horizontal2(position, couleur):
    for x in range(800):
        image.putpixel((x, position), couleur)


def carre(origine_x, origine_y, longueur):
    for x in range(origine_x, origine_x+longueur):
        for y in range(origine_y, origine_y+longueur):
            image.putpixel((x, y), (0, 0, 0))


image = Image.new('RGB', (800, 600), (255, 255, 255))

for y in range(0, 600, 10):
    trait_horizontal2(y, (randint(0, 255), randint(0, 255), randint(0, 255)))

for x in range(0, 800, 10):
    trait_vertical(x)

carre(50, 100, 20)
image.show()
