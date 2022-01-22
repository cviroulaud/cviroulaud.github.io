#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 22 Janvier 2022 14:58
"""
import doctest


def tri_iteratif(tab: list) -> list:
    """
    effectue un tri itératif

    Args:
        tab (list): tableau à trier

    Returns:
        list: tableau trié

    LES TESTS NE SONT PAS DEMANDÉS DANS L'EXERCICE
    >>> tri_iteratif([41, 55, 21, 18, 12, 6, 25]) 
    [6, 12, 18, 21, 25, 41, 55]
    """
    for k in range(len(tab)-1, 0, -1):
        imax = k
        for i in range(0, k):
            if tab[i] > tab[imax]:
                imax = i
        if tab[imax] > tab[k]:
            tab[k], tab[imax] = tab[imax], tab[k]
    return tab


if __name__ == "__main__":
    doctest.testmod(verbose=True)
