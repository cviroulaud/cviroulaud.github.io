#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/08/06 14:58:38

crée un ABR de 100 éléments (de 1 à 1000) max
!!il y a possibilité de dépasser la taille du tableau!!
"""

from random import randint


def inserer(val: int, abr: list, i_pere: int) -> None:
    if abr[i_pere] == 0:  # cel vide
        abr[i_pere] = val
    elif val < abr[i_pere]:
        inserer(val, abr, 2*i_pere+1)  # gauche
    else:
        inserer(val, abr, 2*i_pere+2)  # droite


def rechercher(val: int, abr: list, i_pere: int) -> bool:
    if abr[i_pere] == 0:
        return False
    elif abr[i_pere] == val:
        return True
    elif val < abr[i_pere]:
        rechercher(val, abr, 2*i_pere+1)
    else:
        rechercher(val, abr, 2*i_pere+2)


abr = [0 for _ in range(100)]
for _ in range(15):
    inserer(randint(1, 1000), abr, 0)
print(abr)
