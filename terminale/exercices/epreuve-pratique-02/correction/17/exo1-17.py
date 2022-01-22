#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 22 Janvier 2022 14:26
"""

import doctest


def nombre_de_mots(phrase: str) -> int:
    """
    compte le nombre de mots

    Args:
        phrase ([str]): phrase à étudier

    Returns:
        [int]: nombre de mots

    LES TESTS NE SONT PAS DEMANDÉS DANS L'EXERCICE
    >>> nombre_de_mots('Le point d exclamation est separe !') 
    6
    >>> nombre_de_mots('Il y a un seul espace entre les mots !') 
    9
    >>> nombre_de_mots('Le point final est colle au dernier mot.') 
    8
    """
    nb = 0
    # nombre d'espace == nombre de mots
    for lettre in phrase:
        if lettre == " ":
            nb = nb+1

    # si se termine par un point, il faut ajouter 1
    if phrase[len(phrase)-1] == ".":
        nb = nb+1
    return nb


if __name__ == "__main__":
    doctest.testmod(verbose=True)
