#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov 16 11:20:57 2020

@auteur: Christophe Viroulaud
"""


from mod_graphe import Graphe, Cellule
from graphviz import Graph

TAILLE = 4
grille = Graphe()
# création des sommets
for i in range(TAILLE):
    for j in range(TAILLE):
        grille.ajouter_sommet((j,i))

# arêtes verticales
for j in range(TAILLE):
    for i in range(TAILLE-1):
        for k in range(i+1, TAILLE):
            grille.ajouter_arete((j,i),(j,k))

# arêtes horizontales
for i in range(TAILLE):
    for j in range(TAILLE-1):
        for k in range(j+1, TAILLE):
            grille.ajouter_arete((j,i),(k,i))

print(grille.get_sommets())
print(grille.get_adjacents((2,2)))




