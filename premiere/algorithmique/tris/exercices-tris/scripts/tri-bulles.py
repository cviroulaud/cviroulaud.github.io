#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/18 14:26:21
"""

from random import randint


def echanger(tab: list, i: int, j: int) -> None:
    """
    échange deux éléments de tab
    """
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp


def tri_bulles(tab: list) -> None:
    for i in range(len(tab)):
        for j in range(1, len(tab)-i):
            if tab[j-1] > tab[j]:
                echanger(tab, j-1, j)


t = [randint(0,1000) for _ in range(20)]
print(t)
tri_bulles(t)
print(t)
