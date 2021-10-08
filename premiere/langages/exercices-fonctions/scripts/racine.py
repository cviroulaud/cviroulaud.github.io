#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mercredi 06 Octobre 2021 11:49
"""


def valeur_proche(a: int) -> int:
    """
    renvoie l'entier inférieur le plus proche
    de racine(a)
    """
    entier = 1
    while entier**2 <= a:
        entier += 1
    return entier-1


def racine(a: int) -> float:
    """
    calcule une approximation de
    racine carrée de a
    """
    x = valeur_proche(a)
    for i in range(20):
        x = 0.5*(x+a/x)
    return x


print(racine(50))
