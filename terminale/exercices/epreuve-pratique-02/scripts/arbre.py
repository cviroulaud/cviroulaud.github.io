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


def taille2(arbre: dict, lettre: str) -> int:
    if arbre[lettre][0] == "" and arbre[lettre][1] == "":
        return 1
    elif arbre[lettre][0] == "":
        return 1 + taille2(arbre, arbre[lettre][1])
    elif arbre[lettre][1] == "":
        return 1 + taille2(arbre, arbre[lettre][0])
    else:
        return 1 + taille2(arbre, arbre[lettre][0]) + taille2(arbre, arbre[lettre][1])


def hauteur(arbre: dict, lettre: str) -> int:
    """
    hauteur de l'arbre

    Args:
        arbre (dict): arbre sous forme d'un dictionnaire
        lettre (str): racine

    Returns:
        int: hauteur de l'arbre
    """
    if lettre == "":
        return -1
    else:
        return 1 + max(hauteur(arbre, arbre[lettre][0]), hauteur(arbre, arbre[lettre][1]))


a = {'F': ['B', 'G'], 'B': ['A', 'D'], 'A': ['', ''], 'D': ['C', 'E'],
     'C': ['', ''], 'E': ['', ''], 'G': ['', 'I'], 'I': ['', 'H'],
     'H': ['', '']}
print(taille(a, 'F'))  # 9
print(taille2(a, 'F'))  # 9
print(hauteur(a, 'F'))  # 9
