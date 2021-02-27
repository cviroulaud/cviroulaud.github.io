#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/02/27 21:02:01
"""

from time import time
from abr import ABR
from random import randint

def duree_tri(fonction, tab: list) -> tuple:
    deb = time()
    tab = fonction(tab)
    fin = time()
    return (fonction.__name__, fin-deb)


def tri_selection(tab):
    taille = len(tab)
    for i in range(taille):
        rang_mini = i
        for j in range(i+1, taille):
            if tab[j] < tab[rang_mini]:
                rang_mini = j
        tab[i], tab[rang_mini] = tab[rang_mini], tab[i]
    return tab

def tri_rapide(tab: list)->list:
    if not tab:
        return []
    else:
        pivot = tab[0]
        petit = [x for x in tab if x < pivot]
        grand = [x for x in tab[1:] if x >= pivot]
        return tri_rapide(petit) + [pivot] + tri_rapide(grand)
    
def tri_ABR(tab):
    arbre = ABR()
    for e in big_tab:
        arbre.inserer(e)
    arbre.infixe()
    return tab

big_tab = [randint(0, 1000) for _ in range(5000)]

print(duree_tri(tri_selection, big_tab.copy()))
print(duree_tri(tri_rapide, big_tab.copy()))
print(duree_tri(tri_ABR, big_tab.copy()))
