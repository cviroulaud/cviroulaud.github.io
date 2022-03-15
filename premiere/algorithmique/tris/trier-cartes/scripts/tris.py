#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 14 Mars 2022 17:49
"""

from random import randint


def indice_mini(tab: list, dep: int) -> int:
    i_mini = dep
    mini = tab[dep]
    for i in range(dep, len(tab)):
        if tab[i] < mini:
            i_mini = i
            mini = tab[i]
    return i_mini


def echanger(tab: list, i: int, j: int) -> None:
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp


def inserer(tab: list, j: int) -> None:
    while j-1 >= 0 and tab[j-1] > tab[j]:
        echanger(tab, j-1, j)
        j = j-1


def tri_insertion(tab: list) -> None:
    for i in range(len(tab)):
        inserer(tab, i)


def tri_selection(tab: list) -> None:
    for i in range(len(tab)):
        i_mini = indice_mini(tab, i)
        echanger(tab, i, i_mini)


t = [randint(0, 100) for _ in range(10)]
print(t)
tri_selection(t)
print(t)

t = [randint(0, 100) for _ in range(10)]
print(t)
tri_insertion(t)
print(t)
