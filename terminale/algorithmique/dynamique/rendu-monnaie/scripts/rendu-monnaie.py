#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/04 22:18:50
"""


def nb_pieces_glouton(somme: int, systeme: list) -> int:
    nb_piece = 0
    while not somme == 0:
        i = 0
        # l'agorithme choisit la plus grande pièce
        while systeme[i] > somme:
            i += 1
        somme -= systeme[i]
        nb_piece += 1
    return nb_piece


def detail_pieces_glouton(somme: int, systeme: list) -> list:
    pieces = []
    while not somme == 0:
        i = 0
        while systeme[i] > somme:
            i += 1
        somme -= systeme[i]
        pieces.append(systeme[i])
    return pieces


def nb_pieces_naif(somme: int, systeme: list) -> int:
    if somme == 0:
        return 0
    nb_mini = somme + 1  # somme = 1 + 1 + 1 ...
    # Pour chaque pièce du système
    for piece in systeme:
        if piece <= somme:
            nb_pieces = 1 + nb_pieces_naif(somme-piece, systeme)
            if nb_pieces < nb_mini:
                nb_mini = nb_pieces
    return nb_mini


def nb_pieces_TD(somme: int, systeme: list, track: list) -> int:
    if somme == 0:
        track[0] = 0
        return track[0]
    # le nombre de pièces a déjà été calculé
    if track[somme] > 0:
        return track[somme]
    nb_mini = somme + 1  # somme = 1 + 1 + 1 ...
    for piece in systeme:
        if piece <= somme:
            nb_pieces = 1 + nb_pieces_TD(somme-piece, systeme, track)
            if nb_pieces < nb_mini:
                nb_mini = nb_pieces
    # Pour cette somme on a trouvé le nb de pièces mini
    track[somme] = nb_mini
    return track[somme]


def nb_pieces_TD2(somme: int, systeme: list, track: list) -> int:
    if track[somme] >= 0:
        return track[somme]
    nb_mini = somme + 1  # somme = 1 + 1 + 1 ...
    for piece in systeme:
        if piece <= somme:
            nb_pieces = 1 + nb_pieces_TD2(somme-piece, systeme, track)
            if nb_pieces < nb_mini:
                nb_mini = nb_pieces
    track[somme] = nb_mini
    return track[somme]


def nb_pieces_BU(somme: int, systeme: list) -> int:
    track = [0 for _ in range(somme+1)]
    # pour chaque pièce de track on cherche le nombre minimum de pièces à rendre
    for x in range(1, somme+1):
        mini = somme+1
        for piece in systeme:
            if (piece <= x):
                nb_pieces = 1+track[x-piece]
                if nb_pieces < mini:
                    mini = nb_pieces
        track[x] = mini
    return track[somme]


def nb_pieces_BU_sol(somme: int, systeme: list) -> list:
    track = [0 for _ in range(somme+1)]
    # choix[x] contient la première pièce à rendre pour la somme x
    choix = [0 for _ in range(somme+1)]
    # pour chaque pièce de track on cherche le nombre minimum de pièces à rendre
    for x in range(1, somme+1):
        mini = somme+1
        for piece in systeme:
            if (piece <= x):
                nb_pieces = 1+track[x-piece]
                if nb_pieces < mini:
                    mini = nb_pieces
                    choix_piece = piece
        track[x] = mini   
        choix[x] = choix_piece
    # reconstitution des pièces à rendre
    rendre = somme
    resultat = []
    while rendre > 0:
        resultat.append(choix[rendre])
        rendre -= choix[rendre]
    return resultat

systeme = [10, 5, 2, 1]
somme = 8
nb_pieces_glouton(somme, systeme)
detail_pieces_glouton(somme, systeme)
nb_pieces_naif(somme, systeme)

track = [-1 for _ in range(somme+1)]
nb_pieces_TD(somme, systeme, track)

track = [-1 for _ in range(somme+1)]
track[0] = 0
nb_pieces_TD2(somme, systeme, track)

nb_pieces_BU(somme, systeme)
nb_pieces_BU_sol(somme, systeme)

systeme = [10, 4, 3, 1]
somme = 6
nb_pieces_BU_sol(somme, systeme)
detail_pieces_glouton(somme, systeme)
