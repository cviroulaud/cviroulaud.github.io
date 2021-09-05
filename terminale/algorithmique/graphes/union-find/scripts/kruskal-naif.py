#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/08/31 17:55:18

implémentation find-union avec liste chainée
une ref intéressante
https://fr.wikipedia.org/wiki/Union-find#Impl%C3%A9mentation_utilisant_des_listes_cha%C3%AEn%C3%A9es
"""


class Maillon:
    def __init__(self, n: str):
        self.n = n
        self.suiv = None
        self.prec = None


class Arete:
    def __init__(self, n1: str, n2: str, w: int):
        self.noeuds = {n1, n2}
        self.poids = w

    def get_noeuds(self):
        return tuple(n for n in self.noeuds)


def est_presente(aretes: list, n1: str, n2: str):
    """
    vérifie si cette arête est déjà dans la liste
    """
    for arete_presente in aretes:
        if n1 in arete_presente.noeuds and n2 in arete_presente.noeuds:
            return True
    return False


def find(eq: dict, u: str) -> str:
    """
    renvoie le nom de la racine

    Args:
        eq (dict): dico des équivalences
        u (str): nom du noeud

    Returns:
        str: nom du noeud équivalent
    """
    if eq[u].prec is None:  # racine
        return eq[u].n
    else:
        return find(eq, eq[u].prec.n)


def union(eq: dict, u: str, v: str, r2: str) -> None:
    """
    attache la tête (r2) de la liste contenant (v) 
    à la fin de la liste contenant (u)

    Args:
        eq (dict): dico des équivalences
        u (str): nom d'un noeud
        v (str): nom d'un noeud
        r2 (str): nom de la racine de v
    """
    # descend en bas d'1 liste
    dernier = u
    while eq[dernier].suiv is not None:
        dernier = eq[dernier].suiv.n
    # attache la tête de la 2° liste à la fin de la 1°
    eq[dernier].suiv = eq[r2]
    eq[r2].prec = eq[dernier]


graphe = {"A": {("B", 4), ("H", 8)},
          "B": {("A", 4), ("C", 8), ("H", 11)},
          "C": {("B", 8), ("D", 7), ("F", 4), ("I", 2)},
          "D": {("C", 7), ("E", 9), ("F", 14)},
          "E": {("D", 9), ("F", 10)},
          "F": {("E", 10), ("D", 14), ("C", 4),("G",2)},
          "G": {("F", 2), ("I", 6), ("H", 1)},
          "H": {("G", 1), ("I", 7), ("B", 11), ("A", 8)},
          "I": {("C", 2), ("G", 6), ("H", 7)}}

# crée tableau des arêtes triées par poids
aretes = []
for noeud, voisins in graphe.items():
    for v in voisins:
        if not est_presente(aretes, noeud, v[0]):
            a = Arete(noeud, v[0], v[1])
            aretes.append(a)
aretes.sort(key=lambda a: a.poids)

arbre_couvrant = set()

# Make
equivalence = {}
for key in graphe.keys():
    equivalence[key] = Maillon(key)

# find - union
for a in aretes:
    noeuds = a.get_noeuds()
    r1 = find(equivalence, noeuds[0])
    r2 = find(equivalence, noeuds[1])
    if r1 != r2:  # pas la même racine
        arbre_couvrant.add(a)
        union(equivalence, noeuds[0], noeuds[1], r2)

for a in arbre_couvrant:
    print(a.noeuds, a.poids)
