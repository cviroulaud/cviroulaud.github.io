#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Jan  1 16:09:54 2021

@auteur: Christophe Viroulaud
"""


from random import randint

def aleatoire_100(n: int)->list:
    """
    renvoie une liste de n éléments compris entre 0 et 100
    """
    return [randint(0, 100) for _ in range(n)]

def position(tableau: list, element: int)->int:
    """
    renvoie l'indice de la première position de element

    Parameters
    ----------
    tableau : list
        un tableau d'entiers
    element : int
        un entier.

    Returns
    -------
    l'indice de element.

    """
    for i in range(len(tableau)):
        if tableau[i] == element:
            return i
    return -1

print(position(aleatoire_100(50),10))
