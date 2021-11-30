#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/05/26 16:32:57
"""


def rendu_monnaie(somme: int, systeme: list) -> list:
    """
    renvoie tableau des pièces à rendre
    algo glouton: rend la plus grosse pièce d'abord

    Args:
        somme (int): somme à rendre
        systeme (list): système monétaire

    Returns:
        list: tableau des pièces à rendre
    """
    res = []
    i_piece = 0
    while somme > 0:
        # si pièce est trop grande
        if systeme[i_piece] > somme:
            # on avance dans le système
            i_piece += 1
        else:
            res.append(systeme[i_piece])
            somme -= systeme[i_piece]
    return res


def rendu_monnaie2(somme: int, systeme: list) -> list:
    res = []
    while somme != 0:
        i_piece = 0
        while systeme[i_piece] > somme:
            i_piece += 1
        res.append(systeme[i_piece])
        somme -= systeme[i_piece]
    return res


print(rendu_monnaie(14, [10, 5, 2, 1]))
print(rendu_monnaie2(14, [10, 5, 2, 1]))
