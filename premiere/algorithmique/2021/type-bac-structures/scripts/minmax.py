#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/12 13:41:31
"""


def recherche_minmax(tab: list)->dict:
    """
    renvoie les valeurs min et max
    de tab, sous forme d'un dictionnaire
    """
    if not tab:
        return {"min": None, "max": None}
    else:
        dico = {"min": tab[0], "max": tab[0]}
        for val in tab:
            if val < dico["min"]:
                dico["min"] = val
            if val > dico["max"]:
                dico["max"] = val
        return dico
    
    
print(recherche_minmax([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))
print(recherche_minmax([]))
    