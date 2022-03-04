#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 22 Janvier 2022 14:13
"""

import doctest


def recherche(tab: list) -> list:
    """
    couple d'entiers consécutifs

    Args:
        tab ([list]): tableau d'entiers

    Returns:
        [list]: tableau de tuples d'entiers consécutifs

    LES TESTS NE SONT PAS DEMANDÉS DANS L'EXERCICE
    >>> recherche([1, 4, 3, 5]) 
    []
    >>> recherche([1, 4, 5, 3]) 
    [(4, 5)]
    >>> recherche([7, 1, 2, 5, 3, 4]) 
    [(1, 2), (3, 4)]
    >>> recherche([5, 1, 2, 3, 8, -5, -4, 7]) 
    [(1, 2), (2, 3), (-5, -4)]
    """
    res = []
    for i in range(len(tab)-1):
        if tab[i+1] == tab[i]+1:
            res.append((tab[i], tab[i+1]))
    return res


def recherche2(tab: list) -> list:
    """
    version par compréhension
    >>> recherche2([1, 4, 3, 5]) 
    []
    >>> recherche2([1, 4, 5, 3]) 
    [(4, 5)]
    >>> recherche2([7, 1, 2, 5, 3, 4]) 
    [(1, 2), (3, 4)]
    >>> recherche2([5, 1, 2, 3, 8, -5, -4, 7]) 
    [(1, 2), (2, 3), (-5, -4)]
    """
    return [(tab[i], tab[i+1]) for i in range(len(tab)-1) if tab[i+1] == tab[i]+1]


if __name__ == "__main__":
    doctest.testmod(verbose=True)
