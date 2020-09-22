#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Sep 22 10:31:39 2020

@auteur: Christophe Viroulaud
"""


from random import randint
from time import time

def duree_tri(fonction, t: tuple)->tuple:
    deb = time()
    fonction(list(t))
    fin = time()
    return (fonction.__name__, fin-deb)

def fusionner(gauche,droite):
    res = []
    while gauche and droite:
        if gauche[0] < droite[0]:
            res.append(gauche.pop(0))
        else:
            res.append(droite.pop(0))
    if gauche:
        res.extend(gauche)
    if droite:
        res.extend(droite)
    return res

def fusionner2(l1,l2):
    nb1 = len(l1)
    nb2 = len(l2)
    l = []
    i,j = 0,0
    while i < nb1 and j < nb2:
        if l2[j] < l1[i]:
            l.append(l2[j])
            j += 1
        else:
            l.append(l1[i])
            i += 1
    if i == nb1:
        l.extend(l2[j:])
    if j == nb2:
        l.extend(l1[i:])
    return l

def tri_fusion(tab):
    taille = len(tab)
    if taille <= 1:
        return tab
    else:
        milieu = taille//2
        gauche = tri_fusion(tab[:milieu])
        droite = tri_fusion(tab[milieu:])
        return fusionner(gauche,droite)

l = tuple(randint(0,100) for _ in range(10000))
print(duree_tri(tri_fusion, l))
print(duree_tri(sorted, l))

