#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 25 Octobre 2021 15:06
"""


def somme(t1: list, t2: list) -> list:
    tab = [0, 0, 0, 0, 0]
    for i in range(5):
        tab[i] = t1[i]+t2[i]
    return tab


t1 = [12, 17, 8, 10, 13]
t2 = [4, 18, 9, 11, 23]
print(somme(t1, t2))
