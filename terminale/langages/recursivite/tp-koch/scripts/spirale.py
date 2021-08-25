#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/08/24 22:55:10
"""


from turtle import *
from random import randint


def creer_couleur() -> tuple:
    """
    renvoie une couleur (r, g, b)
    """
    return (randint(0, 255) for _ in range(3))


def dessiner(dim: int) -> None:
    """
    dessine une spirale carrée
    """
    if dim >= 0:
        pencolor(creer_couleur())
        forward(dim)
        right(90)
        dessiner(dim-10)


# initialisation
colormode(255)
speed(5)
hideturtle()

dessiner(200)

exitonclick()
# done()
