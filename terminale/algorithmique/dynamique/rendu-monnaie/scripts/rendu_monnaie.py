#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/05/26 16:32:57
"""


def rendu_glouton(somme: int, systeme: list) -> list:
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


def rendu_glouton_rec(somme: int, systeme: list, i_piece: int) -> list:
    """
    version récursive
    """
    if somme > 0:
        # si pièce est trop grande
        if systeme[i_piece] > somme:
            # on avance dans le système
            i_piece += 1
            return rendu_glouton_rec(somme, systeme, i_piece)
        else:
            # on rend la pièce
            somme -= systeme[i_piece]
            return [systeme[i_piece]] + rendu_glouton_rec(somme, systeme, i_piece)

    else:
        # cas limite
        return []


def rendu_naif(somme: int, systeme: list) -> list:
    global C
    if somme > 0:
        mini = [1 for _ in range(somme)]  # somme = 1 + 1 + 1 ...
        # Teste toutes les possibilités pour chaque pièce du système
        for piece in systeme:
            if piece <= somme:
                C += 1
                pieces = [piece] + rendu_naif(somme-piece, systeme)
                if len(pieces) < len(mini):
                    mini = pieces
        # garde le rendu minimum
        return mini
    else:
        return []


def rendu_td(somme: int, systeme: list, track: list) -> list:
    global C
    # le choix de pièces a déjà été calculé
    if len(track[somme]) > 0:
        return track[somme]
    elif somme > 0:
        mini = [1 for _ in range(somme)]  # somme = 1 + 1 + 1 ...
        # Teste toutes les possibilités pour chaque pièce du système
        for piece in systeme:
            if piece <= somme:
                C += 1
                pieces = [piece] + rendu_td(somme-piece, systeme, track)
                if len(pieces) < len(mini):
                    mini = pieces
        # garde le rendu minimum
        track[somme] = mini
        return mini
    else:
        return []


def rendu_bu(somme: int, systeme: list) -> list:
    global C
    track = [[] for _ in range(somme+1)]
    # pour chaque pièce de track on cherche le nombre minimum de pièces à rendre
    for x in range(1, somme+1):
        # on ne rend que des pièces de 1
        mini = [1 for _ in range(somme)]
        for piece in systeme:
            if piece <= x:
                C += 1
                # prend la solution optimale pour 'x-piece'
                pieces = [piece] + track[x-piece]
                if len(pieces) < len(mini):
                    mini = pieces
        track[x] = mini
    print(track)
    return track[somme]


s = 14
C = 0
print(rendu_glouton(s, [10, 5, 2, 1]))
print(rendu_glouton_rec(s, [10, 5, 2, 1], 0))
print(rendu_naif(s, [10, 5, 2, 1]))
print(C)
C = 0
track = [[] for _ in range(s+1)]
print(rendu_td(s, [10, 5, 2, 1], track))
print(C)
C = 0
print(rendu_bu(s, [10, 5, 2, 1]))
print(C)
