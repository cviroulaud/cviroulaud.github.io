#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mercredi 02 Février 2022 11:44
"""


def ordre(mat: list) -> int:
    return len(mat)


def est_complet_faux(mat: list) -> bool:
    """
    vérifie si chaque sommet est relié à tous
    les autres (sauf lui même)
    """
    for ligne in range(ordre(mat)):
        for col in range(ordre(mat)):
            if ligne != col and mat[ligne][col] == 0:
                return False
    return True


def est_complet(mat: list) -> bool:
    """
    vérifie si chaque sommet est relié à tous
    les autres (sauf lui même)
    """
    for ligne in range(ordre(mat)):
        for col in range(ordre(mat)):
            if (ligne != col and mat[ligne][col] == 0) or \
                    (ligne == col and mat[ligne][col] == 1):
                return False
    return True
