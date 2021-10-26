#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 25 Octobre 2021 14:57
"""


def ecart_max(t: list) -> int:
    maxi = 0
    # attention à ne par sortir du tableau
    for i in range(len(t)-1):
        ecart = t[i+1]-t[i]
        if ecart > maxi:
            maxi = ecart
    return maxi

mesures = [10, 15, 16, 23, 25, 38, 41, 43]
print(ecart_max(mesures))