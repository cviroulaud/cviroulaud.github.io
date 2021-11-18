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
        s = s + tab[i]
    return s


def somme_rec(tab: list, i: int) -> int:
    """
    calcule la somme des éléments du tableau
    Args:
        tab (list): le tableau
        deb (int): indice de l'élément en cours

    Returns:
        int: la somme
    """    
    if i == len(tab):
        return 0
    else:
        return tab[i] + somme_rec(tab, i+1)


def somme_rec_term(tab: list, i: int, s: int) -> int:
    """
    version terminale
    Args:
        tab (list): le tableau
        deb (int): indice de l'élément en cours
        s (int): somme

    Returns:
        int: la somme
    """
    if i == len(tab):
        return s
    else:
        return somme_rec_term(tab, i+1, s+tab[i])


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
print(somme_rec(t, 0))
print(somme_rec_term(t, 0, 0))
print(somme_rec2(t, 0))
