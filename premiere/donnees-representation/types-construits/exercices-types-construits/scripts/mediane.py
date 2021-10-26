#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 25 Octobre 2021 14:41
"""


def mediane(t: tuple) -> float:
    """
    calcule la médiane du tuple
    indications:
        le tuple est ordonné
        le tuple contient au moins 2 éléments
    """
    taille = len(t)
    milieu = taille//2
    if taille % 2 == 0:  # pair
        # la numérotation commence à 0
        med = (t[milieu-1]+t[milieu])/2
    else:  # impair
        med = t[milieu]
    return med


salaire = (800, 830, 830, 950, 1002, 1100,
           1100, 1103, 1340, 1530, 1600)
salaire1 = (900, 950, 950, 960, 1050, 1060,
            1100, 1160, 1370, 1555)
print(mediane(salaire))
print(mediane(salaire1))
