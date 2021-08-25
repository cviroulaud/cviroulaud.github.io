#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sun Sep  6 17:58:22 2020

@auteur: Christophe Viroulaud
"""


from turtle import *
from random import randint

setheading(0)  # Règle l'orientation de la tortue à la valeur 0
hideturtle()
speed(0)
colormode(255)


def creer_couleur() -> tuple:
    """
    renvoie une couleur (r, g, b)
    """
    return (randint(0, 255) for _ in range(3))


def courbe_koch(precision: int, mesure: int) -> None:
    """
    trace un cöté
    """
    if precision == 0:
        pencolor(creer_couleur())
        forward(mesure)
    else:
        courbe_koch(precision-1, mesure//3)
        left(60)
        courbe_koch(precision-1, mesure//3)
        right(120)
        courbe_koch(precision-1, mesure//3)
        left(60)
        courbe_koch(precision-1, mesure//3)


def courbe_koch_carre(precision: int, mesure: int) -> None:
    """
    trace un cöté
    """
    if precision == 0:
        pencolor(creer_couleur())
        forward(mesure)
    else:
        courbe_koch_carre(precision-1, mesure//3)
        left(90)
        courbe_koch_carre(precision-1, mesure//3)
        right(90)
        courbe_koch_carre(precision-1, mesure//3)
        right(90)
        courbe_koch_carre(precision-1, mesure//3)
        left(90)
        courbe_koch_carre(precision-1, mesure//3)


def flocon(precision: int, mesure: int) -> None:
    for _ in range(3):
        courbe_koch(precision, mesure)
        right(120)


def flocon_carre(precision: int, mesure: int) -> None:
    for _ in range(4):
        courbe_koch_carre(precision, mesure)
        right(90)


flocon_carre(3, 400)

exitonclick()
