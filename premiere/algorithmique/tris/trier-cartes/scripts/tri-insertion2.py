#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/07/09 08:19:37

versions qui font remonter l'élément i dans 0...i-1
(un peu comme tri à bulles)
"""

from random import shuffle


def tri_insertion(tab: list) -> None:
    for i in range(len(tab)):
        j = i-1
        while j >= 0 and tab[j] > tab[j+1]:
            tab[j], tab[j+1] = tab[j+1], tab[j]
            j -= 1


cartes = [i for i in range(1, 14)]
shuffle(cartes)
tri_insertion(cartes)
print(cartes)


def inserer(tab: list, j: int) -> None:
    if j >= 0 and tab[j] > tab[j+1]:
        tab[j], tab[j+1] = tab[j+1], tab[j]
        inserer(tab, j-1)


def tri_insertion_rec(tab: list) -> None:
    for i in range(len(tab)):
        inserer(tab, i-1)


cartes = [i for i in range(1, 14)]
shuffle(cartes)
tri_insertion_rec(cartes)
print(cartes)
