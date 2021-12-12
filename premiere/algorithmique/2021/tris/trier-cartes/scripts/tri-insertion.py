#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/10 22:23:23
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


cartes = [i for i in range(1, 14)]
shuffle(cartes)
tri_insertion(cartes)
print(cartes)
