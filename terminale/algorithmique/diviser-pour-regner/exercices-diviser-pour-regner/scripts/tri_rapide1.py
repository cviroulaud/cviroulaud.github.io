#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Sep 24 18:05:39 2020

@auteur: Christophe Viroulaud
"""

from random import randint


def tri_rapide(tab: list) -> list:
    if not tab:
        return []
    else:
        pivot = tab[0]
        petit = [x for x in tab if x < pivot]
        grand = [x for x in tab[1:] if x >= pivot]
        return tri_rapide(petit) + [pivot] + tri_rapide(grand)


l = [randint(0, 100) for _ in range(20)]
print(tri_rapide(l))


def tri_rapide2(tab: list) -> list:
    if not tab:
        return []
    else:
        pivot = tab[0]
        petit = [x for x in tab if x[0] < pivot[0]]
        grand = [x for x in tab[1:] if x[0] >= pivot[0]]
        return tri_rapide2(petit) + [pivot] + tri_rapide2(grand)


l1 = [(9, 8), (9, 7), (5, 3), (5, 2), (1, 1), (3, 4), (8, 6), (9, 3), (9, 5)]
print(tri_rapide2(l1))
