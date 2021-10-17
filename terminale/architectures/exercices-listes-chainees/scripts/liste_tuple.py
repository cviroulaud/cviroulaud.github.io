#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 17 Octobre 2021 01:23
"""


def afficher(lst: tuple) -> str:
    if len(lst) == 0:
        return "fin"
    else:
        return lst[0] + " - " + afficher(lst[1])


def longueur(lst: tuple) -> int:
    if len(lst) == 0:
        return 0
    else:
        return 1+longueur(lst[1])


lst = ("a", ("b", ("c", ("d", ()))))
print((afficher(lst)))
print(longueur(lst))