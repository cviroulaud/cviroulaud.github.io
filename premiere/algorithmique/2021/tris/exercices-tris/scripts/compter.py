#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/18 23:23:39
"""

from random import randint


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


def max_occurrences(tab: list) -> int:
    """
    renvoie l'élément le plus présent dans le tableau
    """
    tri_insertion(tab)
    en_cours = tab[0]
    nb_en_cours = 1
    elt_max = tab[0]
    nb_max = 1
    for i in range(1, len(tab)):
        if en_cours == tab[i]:
            nb_en_cours += 1
        else:
            if nb_en_cours > nb_max:
                nb_max = nb_en_cours
                elt_max = en_cours
            en_cours = tab[i]
            nb_en_cours = 1
    return elt_max


t = [randint(0, 10) for _ in range(100)]
print(max_occurrences(t))
