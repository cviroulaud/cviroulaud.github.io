#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/06/22 22:56:11

version tri en place
"""

from random import randint


def partitionner(tab: list, deb: int, fin: int) -> int:
    """
    place les entiers < pivot (1° élément au départ)
    en début de tableau
    Args:
        tab (list): tableau d'entiers
        deb (int): indice de début (inclus)
        fin (int): indice de fin (exclus)
    Returns:
        (int): position du pivot
    """
    pivot = tab[deb]
    pos = deb
    for i in range(deb+1, fin):
        if tab[i] < pivot:
            pos += 1
            tab[i], tab[pos] = tab[pos], tab[i]
    # place le pivot
    tab[deb], tab[pos] = tab[pos], tab[deb]
    return pos


def tri_rapide(tab: list, deb: int, fin: int) -> None:
    """
    Args:
        tab (list): tableau d'entiers
        deb (int): indice de début (inclus)
        fin (int): indice de fin (exclus)
    """
    if deb < fin:
        pivot = partitionner(tab, deb, fin)
        tri_rapide(tab, deb, pivot)
        tri_rapide(tab, pivot+1, fin)


t = [randint(0, 100) for _ in range(10)]
print(t)
tri_rapide(t, 0, len(t))
print(t)
