#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 11 Mars 2022 15:04
"""
import json
from biblio_graphe import Graphe

# chargement du json
f = open("parcours_noir.json")
list_graphe = json.load(f)

graphe = Graphe(False)
# parcours du graphe
for couple in list_graphe:
    sommet = couple["sommet"]
    adjacents = couple["adjacents"]
    for voisin in adjacents:
        # les sommets sont ajoutés automatiquement
        graphe.ajouter_arete(sommet, voisin)
        
f.close()
print(graphe.predecesseurs(34))
print(graphe.plus_court(34, 19))
