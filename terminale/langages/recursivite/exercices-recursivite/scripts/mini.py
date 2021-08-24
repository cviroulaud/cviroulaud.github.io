#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/08/23 17:15:55
"""

from random import randint


def mini(tab: list) -> int:
    m = float("inf")
    for i in range(len(tab)):
        if tab[i] < m:
            m = tab[i]
    return m


def mini_rec(tab: list, deb: int, m: int) -> int:
    """
    cherche le plus petit élément du tableau

    Args:
        tab (list): le tableau
        deb (int): indice de l'élément en cours
        m (int): l'élément mini
    """
    if deb == len(tab):
        return m
    else:
        if tab[deb] < m:
            m = tab[deb]
        return mini_rec(tab, deb+1, m)


def mini_rec2(tab: list, m: int) -> int:
    """
    avec slice
    """
    if len(tab) == 0:
        return m
    else:
        if tab[0] < m:
            m = tab[0]
        return mini_rec2(tab[1:], m)


t = [randint(1, 1000) for _ in range(30)]
print(t)
print(mini(t))
print(mini_rec(t, 0, float("inf")))
print(mini_rec2(t, float("inf")))
