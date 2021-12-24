#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/09/06 13:00:03
"""
from file_priorite import *

graphe = {"A": {("B", 4), ("H", 8)},
          "B": {("A", 4), ("C", 8), ("H", 11)},
          "C": {("B", 8), ("D", 7), ("F", 4), ("I", 2)},
          "D": {("C", 7), ("E", 9), ("F", 14)},
          "E": {("D", 9), ("F", 10)},
          "F": {("E", 10), ("D", 14), ("C", 4), ("G", 2)},
          "G": {("F", 2), ("I", 6), ("H", 1)},
          "H": {("G", 1), ("I", 7), ("B", 11), ("A", 8)},
          "I": {("C", 2), ("G", 6), ("H", 7)}}

arbre_couvrant = set()

# dico des noeuds avec nom = lettre
sommets = {chr(65+i): Noeud(chr(65+i)) for i in range(9)}
sommets["A"].cout = 0

f = []
for s in sommets:
    enfiler(f, sommets, s)

visites = set()

while len(f) > 0:
    n = defiler(f, sommets)  # nom du sommet
    visites.add(n)
    for arete in graphe[n]:  # ensemble de tuples ("Sommet", arête)
        if arete[0] not in visites:
            if sommets[arete[0]].cout > arete[1]:
                sommets[arete[0]].cout = arete[1]
                sommets[arete[0]].pred = n
                maj_file(f, sommets, arete[0])

# Affichage
for s, n in sommets.items():
    print(f"{n.nom} -- {n.pred}: {n.cout}")
