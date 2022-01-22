#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 22 Janvier 2022 14:51
"""


def taille(arbre: dict, lettre: str) -> int:
    """
    taille de l'arbre

    Args:
        arbre (dict): arbre sous forme d'un dictionnaire
        lettre (str): racine

    Returns:
        int: taille de l'arbre
    """
    if lettre == "":
        return 0
    else:
        return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])


a = {'F': ['B', 'G'], 'B': ['A', 'D'], 'A': ['', ''], 'D': ['C', 'E'],
     'C': ['', ''], 'E': ['', ''], 'G': ['', 'I'], 'I': ['', 'H'],
     'H': ['', '']}
print(taille(a, 'F'))  # 9
