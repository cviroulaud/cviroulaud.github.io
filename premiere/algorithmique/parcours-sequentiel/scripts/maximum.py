#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 12 Décembre 2021 12:19
"""
from random import randint


def maximum(tab: list) -> int:
    """
    valeur maximale de tab

    Args:
        tab (list): tableau

    Returns:
        int: valeur max
    """
    new_maxi = 0
    for val in tab:
        if val > new_maxi:
            new_maxi = val
    # fin de la boucle, renvoie le maxi
    return new_maxi

def maximum2(tab: list) -> int:
    """
    valeur maximale de tab

    Args:
        tab (list): tableau

    Returns:
        int: valeur max
    """
    new_maxi = 0
    for i in range(len(tab)):
        if tab[i] > new_maxi:
            new_maxi = tab[i]
    # fin de la boucle, renvoie le maxi
    return new_maxi

tab = [randint(1, 100) for _ in range(10)]
print(tab)
print(maximum(tab))
print(maximum2(tab))