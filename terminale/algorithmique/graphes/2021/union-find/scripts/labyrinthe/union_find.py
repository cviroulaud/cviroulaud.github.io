#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/09/03 16:16:24

créer un labyrinthe avec algo de kruskal
et union-find
"""

from constantes import *
from random import shuffle


# noeud pour makeset
class Noeud:
    def __init__(self, n: tuple):
        self.nom = n  # pas utile
        self.parent = self
        self.rang = 0


def find(n: Noeud) -> Noeud:
    if n.parent != n:
        n.parent = find(n.parent)  # compression de chemin
    return n.parent


def union(n1: Noeud, n2: Noeud) -> None:
    r1 = find(n1)
    r2 = find(n2)
    if r1 != r2:
        if r1.rang > r2.rang:  # union by rank
            r2.parent = r1
        else:  # < ou =
            r1.parent = r2
            if r1.rang == r2.rang:
                r2.rang = r2.rang+1


def set_arbre_couvrant() -> set:
    """
    principe: crée un graphe "carré" où
    tous les noeuds voisins sont liés.
    puis calcule un arbre couvrant minimum
    avec algo de Kruskal
    """
    # crée tableau des arêtes
    aretes = []
    # arêtes horizontales
    for y in range(hauteur):
        for x in range(largeur-1):
            a = ((x, y), (x+1, y))
            aretes.append(a)

    # arêtes verticales
    for x in range(largeur):
        for y in range(hauteur-1):
            a = ((x, y), (x, y+1))
            aretes.append(a)

    # mélange les arêtes
    shuffle(aretes)

    arbre_couvrant = set()

    # makeset
    equivalence = [[Noeud((i, j)) for i in range(largeur)]
                   for j in range(hauteur)]

    for a in aretes:
        # récupère les 2 noeuds de l'arête
        t1, t2 = a
        n1 = equivalence[t1[0]][t1[1]]
        n2 = equivalence[t2[0]][t2[1]]
        if find(n1) != find(n2):
            arbre_couvrant.add(a)
            union(n1, n2)

    return arbre_couvrant
