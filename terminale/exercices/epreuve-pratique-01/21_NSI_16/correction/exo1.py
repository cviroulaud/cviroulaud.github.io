#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 26 Novembre 2021 11:55
"""

import doctest


def moyenne(tab: list) -> float:
    """
    Calcule la moyenne des valeurs de tab

    Args:
        tab (list): un tableau non vide

    Returns:
        float: la moyenne
        
    LES TESTS NE SONT PAS DEMANDÉS DANS L'EXERCICE
    >>> moyenne([1.0])
    1.0
    >>> moyenne([1.0, 2.0, 4.0])
    2.3333333333333335
    """
    # question possible: et si le tableau est vide?
    assert len(tab) > 0

    somme = 0.
    for note in tab:
        somme += note
    return somme/len(tab)


if __name__ == "__main__":
    doctest.testmod(verbose=True)
