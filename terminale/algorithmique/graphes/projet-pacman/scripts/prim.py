#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Nov 11 14:20:02 2020

@auteur: Christophe Viroulaud
"""


from mod_graphe_pondere import Graphe
from graphviz import Graph
import json

parcours_noir = Graphe()

with open("parcours_noir.json", "r") as fichier:
    data = json.load(fichier)
    """
    data["sommets"] est une liste de dictionnaires
    chacun de ces dictionnaires contient:
            le sommet
            la liste des ses adjacents avec distances
            {"s":7,"d":50}
    """
    for dico in data["sommets"]:
        for adj in dico["adjacents"]:
            parcours_noir.ajouter_arete(dico["sommet"], adj["s"], adj["d"])

#parcours_noir.afficher("parcours")


dot = Graph(format="png")
aretes = parcours_noir.arbre_couvrant_mini()
for a in aretes:
    dot.edge(str(a[0]), str(a[1]), str(a[2]))

dot.render(filename="arbre couvrant minimal", view=True)