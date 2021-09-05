#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/08/29 22:17:53
"""
from random import randint


def choix_machine():
    valeur = randint(1, 3)
    if valeur == 1:
        choix = "pierre"
    elif valeur == 2:
        choix = "feuille"
    else:
        choix = "ciseaux"
    return choix


def choix_machine2(variante):
    """
    Donne la proposition de la machine.

    Args:
        variante (booléen): choix de la variante

    Returns:
        str: renvoie le choix de la machine
    """
    if variante:
        valeur = randint(1, 5)        
    else:
        valeur = randint(1, 3)
        
    if valeur == 1:
        choix = "pierre"
    elif valeur == 2:
        choix = "feuille"
    elif valeur == 3:
        choix = "ciseaux"
    elif valeur == 4:
        choix = "lézard"
    else:
        choix = "Spock"
    return choix


joueur = int(input("pierre, feuille, ciseaux? "))
machine = choix_machine()
