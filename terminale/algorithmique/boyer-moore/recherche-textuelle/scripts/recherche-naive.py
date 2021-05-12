#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/05/10 11:48:22
"""


def recherche_naive(texte: str, motif: str) -> int:
    """
    renvoie la position du motif dans le texte
    -1 s'il n'est pas présent
    """
    for i in range(len(texte)-len(motif)+1):
        j = 0
        while (j < len(motif)) and (motif[j] == texte[i+j]):
            j += 1
        if j == len(motif):
            return i
    return -1


t = "atgatccatga"
m = "cat"
print(recherche_naive(t, m))
