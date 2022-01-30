#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 29 Janvier 2022 23:12
"""


def ordre(mat: list) -> int:
    return len(mat)


def est_complet(mat: list) -> bool:
    """
    vérifie si chaque sommet est relié à tous
    les autres (sauf lui même)
    """
    for ligne in range(ordre(mat)):
        for col in range(ordre(mat)):
            if ligne != col and mat[ligne][col] == 0:
                return False
    return True


mat = [[0, 1, 1, 1, 1],
       [1, 0, 1, 1, 1],
       [1, 1, 0, 1, 1],
       [1, 1, 1, 0, 1],
       [1, 1, 1, 1, 0]]
print(ordre(mat))
print(est_complet(mat))
