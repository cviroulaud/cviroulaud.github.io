#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 26 Novembre 2021 12:45
"""

import doctest


def occurrence_max(chaine: str) -> str:
    """
    renvoie le caractère le plus fréquent de la chaîne

    Args:
        chaine (str): une chaîne de caractère (en minuscules)

    Returns:
        str: le caractère le plus fréquent

    LES TESTS NE SONT PAS DEMANDÉS DANS L'EXERCICE
    >>> occurrence_max("abaaab dfabo")
    'a'
    """
    # on peut faire sans si on veut
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # par compréhension... c'est le minimum...
    occurrence = [0 for _ in range(26)]
    # compte les occurrences de chaque lettre
    for car in chaine:
        i_lettre = 0
        # i_lettre < len(chaine): gestion des caractères hors alphabet (espace)
        while i_lettre < len(chaine) and car != alphabet[i_lettre]:
            i_lettre += 1
        occurrence[i_lettre] += 1

    # si on utilise la fonction max, il faut s'attendre à des questions
    # cherche l'indice max
    k = 0
    for i in range(1, len(occurrence)):
        if occurrence[i] > occurrence[k]:
            k = 1
    # renvoie la lettre correspondante
    return alphabet[k]


if __name__ == "__main__":
    doctest.testmod(verbose=True)
