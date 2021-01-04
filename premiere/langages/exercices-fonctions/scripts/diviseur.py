#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Jan  1 16:04:01 2021

@auteur: Christophe Viroulaud
"""


def diviseur(a):
    """
    renvoie la liste des diviseurs de a
    """
    res = []
    diviseur = 1
    while diviseur < a:
        # si le reste est nul c'est un diviseur
        if a%diviseur == 0:
            res.append(diviseur)
        # passe au diviseur suivant
        diviseur += 1
    return res

print(diviseur(20))