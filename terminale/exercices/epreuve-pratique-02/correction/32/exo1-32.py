#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 22 Janvier 2022 11:47
"""

import doctest


def recherche(elt: int, tab: list) -> int:
    """
    recherche l'occurrence du dernier élément

    Args:
        elt (int): élément cherché
        tab (list): tableau des éléments

    Returns:
        int: indice de l'élément, -1 si pas présent

    LES TESTS NE SONT PAS DEMANDÉS DANS L'EXERCICE
    >>> recherche(1,[2,3,4])
    -1
    >>> recherche(1,[10,12,1,56])
    2
    >>> recherche(1,[1,50,1])
    2
    >>> recherche(1,[8,1,10,1,7,1,8])
    5
    """
    indice = -1
    for i in range(len(tab)):
        if tab[i] == elt:
            indice = i
    return indice


if __name__ == "__main__":
    doctest.testmod(verbose=True)
