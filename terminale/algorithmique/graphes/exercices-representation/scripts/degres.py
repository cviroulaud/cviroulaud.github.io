#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 29 Janvier 2022 09:39
"""


def degres_sortants(liste: list, s: int) -> int:
    return len(liste[s])


def degres_entrants(liste: list, s: int) -> int:
    deg = 0
    for liste_successeurs in liste:
        for successeurs in liste_successeurs:
            if successeurs == s:
                deg = deg+1
    return deg


suivants = [[3, 5], [3], [4], [], [3, 5], [2]]
print(degres_sortants(suivants, 4))
print(degres_entrants(suivants, 4))
