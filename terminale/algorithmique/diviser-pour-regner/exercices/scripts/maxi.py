#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Sep 24 19:05:26 2020

@auteur: Christophe Viroulaud
"""

from random import randint

def maxi(tab: list)->int:
    val = -1
    for x in tab:
        if x > val:
            val = x
    return val

def mystere(tab: list, debut: int = 0, fin: int = -1)->int:
    #initialise 'fin'
    if fin == -1:
        fin = len(tab)
    if debut == (fin-1):
        return tab[debut]
    else:
        milieu = (debut + fin)//2
        gauche = mystere(tab, debut, milieu)
        droite = mystere(tab, milieu, fin)
        if (gauche > droite):
            return gauche
        else:
            return droite

l = [randint(0,1000) for _ in range(20)]
print(l)
print(maxi(l))
print(mystere(l))