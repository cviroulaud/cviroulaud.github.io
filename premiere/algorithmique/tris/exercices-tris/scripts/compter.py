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


def max_occurrences(tab: list) -> tuple:
    """
    renvoie l'élément le plus présent dans le tableau

    Args:
        tab (list): tableau     

    Returns:
        tuple: élément le plus présent et son nombre d'apparition
    """
    tri_insertion(tab)
    # départ 1° série
    en_cours = tab[0]
    serie_en_cours = 1
    elt_max = tab[0]
    serie_max = 1
    for i in range(1, len(tab)):
        # cas même élément que le précédent
        if en_cours == tab[i]:
            serie_en_cours += 1
        else:
            """
            un nouvel élément: 
            on vérifie alors la taille de la dernière série
            """
            if serie_en_cours > serie_max:
                serie_max = serie_en_cours
                elt_max = en_cours
            # départ nouvelle série
            en_cours = tab[i]
            serie_en_cours = 1
    return (elt_max, serie_max)


t = [randint(0, 10) for _ in range(100)]
maxi = max_occurrences(t)
print(f"Le nombre {maxi[0]} est apparu {maxi[1]} fois.")
