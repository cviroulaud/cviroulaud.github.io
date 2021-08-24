#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/08/23 17:15:55
"""

from random import randint


def somme(tab: list) -> int:
    s = 0
    for i in range(len(tab)):
        s += tab[i]
    return s


def somme_rec(tab: list, deb: int, s: int) -> int:
    """
    calcule la somme des éléments du tableau

    Args:
        tab (list): le tableau
        deb (int): indice de l'élément en cours
        s (int): somme

    Returns:
        int: la somme
    """
    if deb == len(tab):
        return s
    else:
        return somme_rec(tab, deb+1, s+tab[deb])


def somme_rec2(tab: list, s: int) -> int:
    if len(tab) == 0:
        return s
    else:
        tete = tab[0]
        queue = tab[1:]  # slice
        return somme_rec2(queue, s+tete)


t = [randint(1, 100) for _ in range(10)]
print(t)
print(somme(t))
print(somme_rec(t, 0, 0))
print(somme_rec2(t, 0))
