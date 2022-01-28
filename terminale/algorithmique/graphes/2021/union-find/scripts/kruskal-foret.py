#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/09/03 16:16:24
avec forêt
"""


# Pour construire tableau des arêtes
class Arete:
    def __init__(self, n1: str, n2: str, w: int):
        self.noeuds = {n1, n2}
        self.poids = w

    def get_noeuds(self):
        """
        renvoie les indices des noeuds 
        correspondant à chaque lettre de l'arête

        Returns:
            [type]: tuple de 2 entiers
        """
        return tuple(ord(n)-65 for n in self.noeuds)


def est_presente(aretes: list, n1: str, n2: str):
    """
    vérifie si cette arête est déjà dans la liste
    """
    for arete_presente in aretes:
        if n1 in arete_presente.noeuds and n2 in arete_presente.noeuds:
            return True
    return False

# noeud pour makeset


class Noeud:
    def __init__(self, n: int):
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


graphe = {"A": {("B", 4), ("H", 8)},
          "B": {("A", 4), ("C", 8), ("H", 11)},
          "C": {("B", 8), ("D", 7), ("F", 4), ("I", 2)},
          "D": {("C", 7), ("E", 9), ("F", 14)},
          "E": {("D", 9), ("F", 10)},
          "F": {("E", 10), ("D", 14), ("C", 4), ("G", 2)},
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

# tableau des noeuds avec nom = lettre (makeset)
# indice 0 = "A"
equivalence = [Noeud(65+i) for i in range(9)]

for a in aretes:
    # récupère les indices des 2 noeuds de l'arête
    i1, i2 = a.get_noeuds()
    # noeuds correspondants
    n1 = equivalence[i1]
    n2 = equivalence[i2]
    if find(n1) != find(n2):
        arbre_couvrant.add(a)
        union(n1, n2)

# affichage
for a in arbre_couvrant:
    print(a.noeuds, a.poids)
