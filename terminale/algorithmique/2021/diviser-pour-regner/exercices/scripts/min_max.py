#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Sep 24 19:05:26 2020

@auteur: Christophe Viroulaud
"""

from random import randint

def min_max(tab: list)->tuple:
    mini = float("inf")
    maxi = -1
    for x in tab:
        if x < mini:
            mini = x
        if x > maxi:
            maxi = x
    return (mini,maxi)

def min_max_rec(tab: list, debut: int = 0, fin: int = -1)->tuple:
    #initialise 'fin'
    if fin == -1:
        fin = len(tab)
    #1 seul élément
    if debut == (fin-1):
        return (tab[debut], tab[debut])
    else:
        milieu = (debut + fin)//2
        gauche = min_max_rec(tab, debut, milieu)
        droite = min_max_rec(tab, milieu, fin)
        if (gauche[0] < droite[0]):
            mini = gauche[0]
        else:
            mini = droite[0]
        if (gauche[1] > droite[1]):
            maxi = gauche[1]
        else:
            maxi = droite[1]
        return (mini, maxi)

l = [randint(0,1000) for _ in range(20)]
print(l)
print(min_max(l))
print(min_max_rec(l))