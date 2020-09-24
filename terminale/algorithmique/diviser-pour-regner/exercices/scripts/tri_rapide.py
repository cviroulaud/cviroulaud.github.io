#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Sep 24 18:05:39 2020

@auteur: Christophe Viroulaud
"""

from random import randint

def tri_rapide(tab: list)->list:
    if not tab:
        return []
    else:
        pivot = tab[0]
        petit = [x for x in tab if x < pivot]
        grand = [x for x in tab[1:] if x >= pivot]
        return tri_rapide(petit) + [pivot] + tri_rapide(grand)

l = [randint(0,100) for _ in range(20)]
print(tri_rapide(l))

l1 = [(1, 2), (9, 8), (9, 7), (3, 4), (8, 6), (9, 3), (9, 6)]
print(tri_rapide(l1))

