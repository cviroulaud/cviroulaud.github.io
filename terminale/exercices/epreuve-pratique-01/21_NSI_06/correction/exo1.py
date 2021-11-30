#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 26 Novembre 2021 11:04
"""

import doctest


def rendu(somme_a_rendre: int) -> list:
    """
    détermine les pièces à rendre d'une somme

    Args:
        somme_a_rendre (int): la somme à rendre

    Returns:
        list: [n1, n2, n3] où
                n1 = pièces de 5
                n2 = pièces de 2
                n3 = pièces de 1

    LES TESTS NE SONT PAS DEMANDÉS DANS L'EXERCICE
    >>> rendu(13)
    [2, 1, 1]
    >>> rendu(64)
    [12, 2, 0]
    >>> rendu(89)
    [17, 2, 0]
    """
    monnaie = [0, 0, 0]
    # tant qu'il reste de l'argent à rendre
    while somme_a_rendre > 0:
        # on commence par la pièce la plus grande (algo glouton)
        if somme_a_rendre >= 5:
            somme_a_rendre -= 5
            monnaie[0] += 1
        elif somme_a_rendre >= 2:
            somme_a_rendre -= 2
            monnaie[1] += 1
        else:
            somme_a_rendre -= 1
            monnaie[2] += 1
    return monnaie


if __name__ == "__main__":
    doctest.testmod(verbose=True)
