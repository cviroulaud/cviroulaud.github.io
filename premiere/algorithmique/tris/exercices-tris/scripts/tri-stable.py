#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/10 22:23:23
"""


def echanger(tab: list, i: int, j: int) -> None:
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp


def inserer(tab: list, j: int) -> None:
    # Le changement se fait dans la comparaison
    while j-1 >= 0 and tab[j-1][0] > tab[j][0]:
        echanger(tab, j-1, j)
        j = j-1


def tri_insertion(tab: list) -> None:
    for i in range(len(tab)):
        inserer(tab, i)


tab = [(5, "a"), (8, "b"), (1, "e"), (5, "d"), (7, "f"), (8, "c")]
tri_insertion(tab)
print(tab)
