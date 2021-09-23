#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mercredi 22 Septembre 2021 18:17
"""
BLANC, GRIS, NOIR = 0, 1, 2


def tri_topo(l: dict) -> list:
    noeuds = {i: BLANC for i in l.keys()}
    tri = []
    for n in l.keys():
        if noeuds[n] == BLANC:
            dfs(l, noeuds, n, tri)
    return tri


def dfs(l: dict, noeuds: dict, dep: int, tri: list) -> list:
    noeuds[dep] = GRIS
    for v in l[dep]:
        if noeuds[v] == BLANC:
            dfs(l, noeuds, v, tri)
    noeuds[dep] = NOIR
    tri.append(dep)


l = {
    1: {2, 8},
    2: {3},
    3: {6},
    4: {3, 5},
    5: {6},
    6: set(),
    7: {8},
    8: set()
}

print(tri_topo(l))
