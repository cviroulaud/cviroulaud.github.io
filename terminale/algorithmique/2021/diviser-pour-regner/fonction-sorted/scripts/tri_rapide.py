#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/06/22 22:56:11

version tri en place
"""

from random import randint


def partitionner(tab: list, deb: int, fin: int) -> None:
    pivot = tab[deb]
    pos = deb
    for i in range(deb+1, fin+1):
        if tab[i] < pivot:
            pos += 1
            tab[i], tab[pos] = tab[pos], tab[i]
    # place le pivot
    tab[deb], tab[pos] = tab[pos], tab[deb]
    return pos


def tri_rapide(tab: list, deb: int, fin: int) -> None:
    if deb < fin:
        pivot = partitionner(tab, deb, fin)
        tri_rapide(tab, deb, pivot-1)
        tri_rapide(tab, pivot+1, fin)


t = [randint(0, 100) for _ in range(10)]
print(t)
tri_rapide(t, 0, len(t)-1)
print(t)
