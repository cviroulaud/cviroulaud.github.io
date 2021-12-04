#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Jan 27 11:11:30 2021

@auteur: Christophe Viroulaud
"""


import json


def i_feuille_gauche(arbre: list) -> int:
    """
    indice de la feuille la plus à gauche

    Args:
        arbre (list): arbre binaire parfait

    Returns:
        int: l'indice
    """
    i = 0
    while (2*i+1) < len(arbre):
        i = 2*i+1
    return i


def get_matchs(arbre: list) -> list:
    """
    huitième de finale

    Args:
        arbre (list): tableau du tournoi

    Returns:
        list: tableau de tuples
    """
    matchs = []
    i = i_feuille_gauche(arbre)
    while i < len(arbre):
        matchs.append((arbre[i], arbre[i+1]))
        i = i+2
    return matchs


f = open("cdm2018.json")
tab_cdm = json.load(f)
f.close()
print(i_feuille_gauche(tab_cdm))
print(get_matchs(tab_cdm))
