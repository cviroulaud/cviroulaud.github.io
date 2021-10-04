#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Sep 24 16:42:30 2020

@auteur: Christophe Viroulaud
"""


def dichotomie_rec(tab: list, x: int, debut: int, fin: int) -> int:
    """
    version récursive
    Retourne la position de x ou -1 s'il n'est pas dans la liste
    """
    if debut <= fin:
        milieu = (debut + fin)//2
        if tab[milieu] == x:
            return milieu
        elif tab[milieu] < x:
            return dichotomie_rec(tab, x, milieu + 1, fin)
        else:
            return dichotomie_rec(tab, x, debut, milieu - 1)
    else:
        return -1


def dichotomie_imp(tab: int, x: int) -> int:
    """
    version impérative
    Retourne la position de x ou -1 s'il n'est pas dans la liste
    """
    debut, fin = 0, len(tab) - 1
    while debut <= fin:
        milieu = (debut + fin)//2
        if tab[milieu] == x:
            return milieu
        elif tab[milieu] < x:
            debut = milieu+1
        else:
            fin = milieu-1
    return -1


l = [i for i in range(50)]
print(dichotomie_imp(l, 10))
print(dichotomie_rec(l, 10, 0, len(l)-1))
print(dichotomie_imp(l, 52))
print(dichotomie_rec(l, 52, 0, len(l)-1))
