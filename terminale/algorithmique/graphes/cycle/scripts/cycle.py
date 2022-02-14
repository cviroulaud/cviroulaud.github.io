#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Sunday 13 February 2022 21:11
"""

BLANC, GRIS, NOIR = 0, 1, 2


def dfs(mat: list, dep: int, vis: list) -> bool:
    if vis[dep] == GRIS:  # cycle
        return True
    if vis[dep] == NOIR:
        return False

    # marque le sommet en cours de visite
    vis[dep] = GRIS
    for i in range(len(mat[dep])):
        # c'est un successeur
        if mat[dep][i] == 1:
            if dfs(mat, i, vis):
                # remontée des appels récursifs
                return True

    # fin de la visite
    vis[dep] = NOIR
    return False


def a_cycle(mat: list) -> bool:
    visites = [BLANC for _ in range(len(mat))]
    for i in range(len(mat)):
        # lance un parcours depuis chaque sommet
        if dfs(mat, i, visites):
            return True
    return False


cycle_non = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

cycle_oui = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
print(a_cycle(cycle_non))
print(a_cycle(cycle_oui))
