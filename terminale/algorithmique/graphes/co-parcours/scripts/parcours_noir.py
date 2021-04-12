#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Oct 28 14:47:45 2020

@auteur: Christophe Viroulaud
"""


from mod_graphe import Graphe
import json

parcours_noir = Graphe()

with open("parcours_noir.json", "r") as fichier:
    data = json.load(fichier)
    """
    data["sommets"] est une liste de dictionnaires
    chacun de ces dictionnaires contient:
            le sommet
            la liste des ses adjacents
    """
    for dico in data["sommets"]:
        for adj in dico["adjacents"]:
            parcours_noir.ajouter_arete(dico["sommet"], adj)

print(parcours_noir.est_connexe())
print(parcours_noir.DFS(75))
print(parcours_noir.BFS(75))
print(parcours_noir.plus_court_chemin(75,34))
print(parcours_noir.plus_court_chemin_detail(75,34))
print(parcours_noir.plus_court_chemin_detail(75,26))
print(parcours_noir.DFS_rec(75))
print(parcours_noir.DFS_rec(75))


