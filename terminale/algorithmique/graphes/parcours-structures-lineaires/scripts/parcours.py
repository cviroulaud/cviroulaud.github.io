#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 19 Février 2022 08:57
"""
from structures import Pile, File
BLANC, GRIS, NOIR = 0, 1, 2


def dfs(graphe: list) -> list:
    """
    parcours en profondeur

    Args:
        graphe (list): graphe non vide

    Returns:
        list: ordre du parcours
    """
    parcours = []
    p = Pile()
    p.empiler(0)
    while not p.est_vide():
        en_cours = p.depiler()
        if en_cours not in parcours:
            parcours.append(en_cours)

            for voisin in graphe[en_cours]:
                p.empiler(voisin)
    return parcours


def dfs_aretes(graphe: list) -> list:
    """
    parcours en profondeur et
    stockage des arêtes

    Args:
        graphe (list): graphe non vide

    Returns:
        list: liste des arêtes parcourues
    """
    parcours = []
    etats = [BLANC for _ in range(len(graphe))]
    p = Pile()
    p.empiler(0)
    while not p.est_vide():
        en_cours = p.depiler()
        for voisin in graphe[en_cours]:
            if etats[voisin] == BLANC:
                etats[voisin] = GRIS
                p.empiler(voisin)
            # stockage arête parcourue
            parcours.append((en_cours, voisin))
                
        etats[en_cours] = NOIR
    return parcours


def bfs(graphe: list) -> list:
    """
    parcours en largeur

    Args:
        graphe (list): graphe non vide

    Returns:
        list: ordre du parcours
    """
    parcours = []
    f = File()
    f.enfiler(0)
    while not f.est_vide():
        en_cours = f.defiler()
        if en_cours not in parcours:
            parcours.append(en_cours)

            for voisin in graphe[en_cours]:
                f.enfiler(voisin)
    return parcours


def bfs_aretes(graphe: list) -> list:
    """
    parcours en largeur et
    stockage des arêtes

    Args:
        graphe (list): graphe non vide

    Returns:
        list: liste des arêtes parcourues
    """
    parcours = []
    etats = [BLANC for _ in range(len(graphe))]
    f = File()
    f.enfiler(0)
    etats[0]=GRIS
    while not f.est_vide():
        en_cours = f.defiler()
        for voisin in graphe[en_cours]:
            if etats[voisin] == BLANC:
                etats[voisin] = GRIS
                f.enfiler(voisin)
            # stockage arête parcourue
            parcours.append((en_cours, voisin))
                
        etats[en_cours] = NOIR
    return parcours


graphe = [
    [3, 5, 6],
    [2, 9],
    [1, 3, 4],
    [0, 2, 4],
    [2, 3],
    [0, 6, 7],
    [0, 5, 7],
    [5, 6, 8],
    [7],
    [1]
]
print(dfs(graphe))
print(dfs_aretes(graphe))
print(bfs(graphe))
print(bfs_aretes(graphe))
