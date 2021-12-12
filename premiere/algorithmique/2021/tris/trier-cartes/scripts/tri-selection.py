#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/07 22:59:29
"""

from random import shuffle


def echanger(tab: list, i: int, j: int) -> None:
    """
    inverse les élément d'indices i et j du tableau
    """
    tab[i], tab[j] = tab[j], tab[i]


def trouver_mini(tab: list, i_depart: int) -> int:
    """
    renvoie l'indice du plus petit élément entre
    i_depart et la fin du tableau
    """
    i_mini = i_depart
    for j in range(i_depart+1, len(tab)):
        if tab[j] < tab[i_mini]:
            i_mini = j
    return i_mini


def tri_selection(tab: list) -> None:
    """
    tri le tableau dans l'ordre croissant
    """
    for i in range(len(tab)):
        position_du_mini = trouver_mini(tab, i)
        echanger(tab, i, position_du_mini)


cartes = [i for i in range(1, 14)]
shuffle(cartes)
tri_selection(cartes)
print(cartes)