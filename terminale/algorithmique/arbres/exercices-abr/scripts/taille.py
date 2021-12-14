#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 12 Décembre 2021 14:46
"""


def taille(a: dict, s: str) -> int:
    if a[s][0] == '' and a[s][1] == '':  # pas de fils
        return 1
    elif a[s][0] == '':  # pas de fils gauche
        return 1 + taille(a, a[s][1])
    elif a[s][1] == '':  # pas de fils droit
        return 1 + taille(a, a[s][0])
    else:  # deux fils
        return 1 + taille(a, a[s][1]) + taille(a, a[s][0])


a = {'F': ['B', 'G'], 'B': ['A', 'D'], 'A': ['', ''], 'D': ['C', 'E'], 'C': [
    '', ''], 'E': ['', ''], 'G': ['', 'I'], 'I': ['', 'H'], 'H': ['', '']}
print(taille(a, 'F'))
