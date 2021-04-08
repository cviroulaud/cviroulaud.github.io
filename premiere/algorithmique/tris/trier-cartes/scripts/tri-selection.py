#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/07 22:59:29
"""

from random import shuffle


def selection(tab: list) -> list:
    for i in range(len(tab)):
        mini = tab[i]
        indice_mini = i
        for j in range(i, len(tab)):
            if tab[j] < mini:
                mini = tab[j]
                indice_mini = j
        tab[i], tab[indice_mini] = tab[indice_mini], tab[i]
    return tab


cartes = [i for i in range(1, 14)]
shuffle(cartes)
print(cartes)
selection(cartes)
print(cartes)
