#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 22 Janvier 2022 12:06
"""

import doctest


def convertir(T: list) -> int:
    """
    T est un tableau d'entiers, dont les éléments sont 0 ou 1 et
    représentant un entier écrit en binaire. Renvoie l'écriture
    décimale de l'entier positif dont la représentation binaire
    est donnée par le tableau T

    LES TESTS NE SONT PAS DEMANDÉS DANS L'EXERCICE
    >>> convertir([1, 0, 1, 0, 0, 1, 1])
    83
    >>> convertir([1, 0, 0, 0, 0, 0, 1, 0])
    130
    """
    res = 0
    for i in range(len(T)):
        # le premier élément du tableau est l'exposant le plus grand
        res = res + T[i] * 2**(len(T)-1-i)
    return res


if __name__ == "__main__":
    doctest.testmod(verbose=True)
