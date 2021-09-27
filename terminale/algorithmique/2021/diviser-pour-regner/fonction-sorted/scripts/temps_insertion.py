#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Sep  21 10:48:28 2020

@auteur: Christophe Viroulaud
"""


from random import randint
from time import time

def duree_tri(fonction, t: tuple)->tuple:
    deb = time()
    fonction(list(t))
    fin = time()
    return (fonction.__name__, fin-deb)

def tri_insertion(tab):
    taille = len(tab)
    for i in range(1,taille):
        en_cours = tab[i]
        j = i-1
        while j >= 0 and tab[j] > en_cours:
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = en_cours
    return tab

l = tuple(randint(0,100) for _ in range(10000))
print(duree_tri(tri_insertion, l))
print(duree_tri(sorted, l))

