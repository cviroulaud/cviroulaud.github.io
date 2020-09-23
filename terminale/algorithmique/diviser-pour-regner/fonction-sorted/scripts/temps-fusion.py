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

def fusionner(gauche: list, droite: list)-> list:
    res = []
    i,j = 0,0
    while i < len(gauche) and j < len(droite):
        if droite[j] < gauche[i]:
            res.append(droite[j])
            j += 1
        else:
            res.append(gauche[i])
            i += 1

    #ajout de la fin de liste restante
    if i == len(gauche):
        res.extend(droite[j:])
    if j == len(droite):
        res.extend(gauche[i:])
    return res

def fusionner2(gauche: list,droite: list)->list:
    res = []
    while gauche and droite:
        if gauche[0] < droite[0]:
            res.append(gauche.pop(0))
        else:
            res.append(droite.pop(0))

    #ajout de la fin de liste restante
    if gauche:
        res.extend(gauche)
    if droite:
        res.extend(droite)
    return res

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

