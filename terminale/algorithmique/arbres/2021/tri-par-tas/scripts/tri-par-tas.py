#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Feb 18 10:42:14 2021

@auteur: Christophe Viroulaud
"""


def echanger(t: list, i1: int, i2: int)->None:
    """
    inverse les deux valeurs du tableau
    """
    t[i1], t[i2] = t[i2], t[i1]

def tamiser_temp(t: list, i_pere: int)->None:
    """
    tamise le tableau pour retrouver un tas
    """
    i_gauche = 2*i_pere + 1
    i_droit = 2*i_pere + 2
    i_fils_max = i_gauche
    # i_pere n'est pas une feuille
    # ou ne dépasse pas les éléments déjà triés
    if i_fils_max < len(t)-1:
        # récupère l'indice du plus grand fils
        if t[i_gauche] < t[i_droit]:
            i_fils_max = i_droit

    if i_fils_max <= len(t)-1:
        # tamise récursivement
        if t[i_fils_max] > t[i_pere]:
            echanger(t, i_pere, i_fils_max)
            tamiser_temp(t, i_fils_max)

def tamiser(t: list, i_pere: int, i_max: int)->None:
    """
    tamise le tableau pour retrouver un tas
    """
    i_gauche = 2*i_pere + 1
    i_droit = 2*i_pere + 2
    i_fils_max = i_gauche
    # i_pere n'est pas une feuille
    # ou ne dépasse pas les éléments déjà triés
    if i_fils_max < i_max:
        # récupère l'indice du plus grand fils
        if t[i_gauche] < t[i_droit]:
            i_fils_max = i_droit

    if i_fils_max <= i_max:
        # tamise récursivement
        if t[i_fils_max] > t[i_pere]:
            echanger(t, i_pere, i_fils_max)
            tamiser(t, i_fils_max, i_max)

def entasser(t: list)->None:
    """
    transforme le tableau en tas
    en commençant par la fin
    """
    # indice du dernier noeud qui n'est pas une feuille
    i = len(t)//2 - 1
    while i >= 0:
        tamiser(t, i, len(t)-1)
        i -= 1

def tri_par_tas(t: list)->None:
    """
    tri (en place) le tableau
    """
    entasser(t)
    dernier = len(t) - 1
    while dernier >= 0:
        echanger(t, 0, dernier)
        tamiser(t, 0, dernier-1)
        dernier -= 1


from random import randint
tab = [randint(0,100) for _ in range(10)]
tri_par_tas(tab)
print(tab)


tas = [9, 17, 6, 10, 12, 4 ,1 , 2, 1, 5, 3]
tamiser_temp(tas,0)
print(tas)
