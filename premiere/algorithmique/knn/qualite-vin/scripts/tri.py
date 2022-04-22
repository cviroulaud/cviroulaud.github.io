#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 15 Avril 2022 12:14
"""
def echanger(tab: list, i: int, j: int) -> None:
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp


def inserer(tab: list, j: int) -> None:
    """
    tri en fonction du second élément du tuple

    Args:
        tab (list): tableau de tuples
        j (int): rang
    """    
    # Le changement se fait dans la comparaison
    while j-1 >= 0 and tab[j-1][1] > tab[j][1]:
        echanger(tab, j-1, j)
        j = j-1


def tri_insertion(tab: list) -> None:
    for i in range(len(tab)):
        inserer(tab, i)