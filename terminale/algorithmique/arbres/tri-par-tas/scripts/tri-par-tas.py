#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mardi 07 Décembre 2021 23:12
"""
from random import randint


def echanger(t: list, i1: int, i2: int) -> None:
    """
    inverse les deux valeurs du tableau
    """
    t[i1], t[i2] = t[i2], t[i1]


def get_i_fils_max(t: list, i_pere: int, i_max: int) -> int:
    """
    l'indice du fils max ou l'indice du père s'il est le plus grand

    Args:
        t (list): tableau
        i_pere (int): indice du père
        i_max (int): indice à ne pas dépasser (partie triée)

    Returns:
        int: indice du max
    """
    potentiel = i_pere
    i_gauche = 2*i_pere+1
    if i_gauche <= i_max:
        if t[i_gauche] > t[potentiel]:
            potentiel = i_gauche

        i_droit = 2*i_pere+2
        if i_droit <= i_max:
            if t[i_droit] > t[potentiel]:
                potentiel = i_droit

    return potentiel


def tamiser(t: list, i_pere: int, i_max: int) -> None:
    """
    tamise le noeud i_pere pour retrouver un tas
    on s'arrête avant i_max (partie triée)
    Args:
        t (list): le tableau
        i_pere (int): indice du noeud à tamiser
        i_max (int): limite ou s'arrête le tamisage
    """
    i_fils_max = get_i_fils_max(t, i_pere, i_max)
    if i_fils_max != i_pere:
        echanger(t, i_pere, i_fils_max)
        tamiser(t, i_fils_max, i_max)


def entasser(t: list) -> None:
    """
    transforme le tableau en tas
    en commençant par la fin

    Args:
        t (list): le tableau
    """
    # indice du dernier noeud qui n'est pas une feuille
    i = len(t)//2 - 1
    while i >= 0:
        tamiser(t, i, len(t)-1)
        i -= 1


def tri_par_tas(t: list) -> None:
    """
    tri (en place) le tableau

    Args:
        t (list): le tableau
    """
    entasser(t)
    dernier = len(t) - 1
    while dernier > 0:
        echanger(t, 0, dernier)
        tamiser(t, 0, dernier-1)
        dernier -= 1


tab = [randint(0, 100) for _ in range(10)]
print(tab)
tri_par_tas(tab)
print(tab)
