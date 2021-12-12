#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/18 23:18:50
"""

from random import shuffle


def tri_insertion(tab: list) -> None:
    """
    tri le tableau dans l'ordre croissant
    """
    for i in range(len(tab)):
        # mémoriser
        en_cours = tab[i]
        pos = i
        # décaler
        while pos > 0 and en_cours < tab[pos-1]:
            tab[pos] = tab[pos-1]
            pos = pos-1
        # insérer
        tab[pos] = en_cours


def comparer(tab1: list, tab2: list) -> bool:
    for i in range(len(tab1)):
        if not tab1[i] == tab2[i]:
            return False
    return True


t1 = [3, 5, 9, 0, 1, 8, 2]
t2 = [9, 5, 3, 2, 8, 1, 0]
tri_insertion(t1)
tri_insertion(t2)
print(comparer(t1, t2))
