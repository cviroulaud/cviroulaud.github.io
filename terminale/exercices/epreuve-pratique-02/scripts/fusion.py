#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 22 Janvier 2022 11:30
"""

import doctest


def fusion(tab1: list, tab2: list) -> list:
    """
    fusionne deux tableaux triés

    Args:
        tab1 (list): tableau trié
        tab2 (list): tableau trié

    Returns:
        list: tableau trié, fusion des deux

    LES TESTS NE SONT PAS DEMANDÉS DANS L'EXERCICE
    >>> fusion([3, 5], [2, 5])
    [2, 3, 5, 5]
    >>> fusion([-2, 4], [-3, 5, 10])
    [-3, -2, 4, 5, 10]
    >>> fusion([4], [2, 6])
    [2, 4, 6]
    """
    tab = []
    i1 = 0
    i2 = 0
    while i1 < len(tab1) and i2 < len(tab2):
        # ajout de l'élément le plus petit des 2 tableaux
        if tab1[i1] < tab2[i2]:
            tab.append(tab1[i1])
            i1 = i1+1
        else:
            tab.append(tab2[i2])
            i2 = i2+1

    # ajout des fins de tableau restantes
    for i in range(i1, len(tab1)):
        tab.append(tab1[i])
    for i in range(i2, len(tab2)):
        tab.append(tab2[i])

    return tab

if __name__ == "__main__":
    doctest.testmod(verbose=True)
