#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Jan  1 16:07:12 2021

@auteur: Christophe Viroulaud
"""


def est_premier(x: int)->bool:
    """
    renvoie True si x est un nombre premier
    """
    diviseur = 2
    # si le reste est nul, c'est que nous avons un diviseur
    while diviseur < x and not(x%diviseur == 0):
        diviseur += 1
    # On a divisé par tous les nombres < x
    if diviseur == x:
        return True
    else: # on s'est arrêté avant
        return False

print(est_premier(12))
