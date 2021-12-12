#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/10 22:23:23
"""

from random import shuffle


def tri_insertion(tab: list) -> None:
    """
    tri le tableau de tuples dans l'ordre croissant
    """
    for i in range(len(tab)):
        # mémoriser
        en_cours = tab[i]
        pos = i
        # décaler
        while pos > 0 and en_cours[0] < tab[pos-1][0]:
            tab[pos] = tab[pos-1]
            pos = pos-1
        # insérer
        tab[pos] = en_cours


tab = [(5, "a"), (8, "b"), (1, "e"), (5, "d"), (7, "f"), (8, "c")]
tri_insertion(tab)
print(tab)
