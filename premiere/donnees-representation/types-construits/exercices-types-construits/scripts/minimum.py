#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 25 Octobre 2021 14:37
"""


def mini(t: tuple) -> int:
    """
    renvoie l'entier minimum de t
    """
    minimum = 101
    for elt in t:
        if elt < minimum:
            minimum = elt
    return minimum


tup = (17, 32, 8, 4, 35, 13)
print(mini(tup))
