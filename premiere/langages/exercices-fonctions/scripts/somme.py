#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mercredi 06 Octobre 2021 11:46
"""


def somme(n: int) -> int:
    """
    renvoie la somme des entiers de 1 à n
    """
    somme = 0
    for i in range(n+1):
        somme = somme + i
    return somme


print(somme(10))
