#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sun Nov 22 11:35:01 2020

@auteur: Christophe Viroulaud
"""


from mod_graphe import Graphe
import networkx as nx
import matplotlib.pyplot as plt

laby = Graphe()

laby.ajouter_arete("A0", "B0")
laby.ajouter_arete("C0", "B0")
laby.ajouter_arete("C0", "C1")
laby.ajouter_arete("C1", "D1")
laby.ajouter_arete("D1", "D0")
laby.ajouter_arete("C1", "B1")
laby.ajouter_arete("B1", "B2")
laby.ajouter_arete("B2", "B3")
laby.ajouter_arete("A3", "B3")
laby.ajouter_arete("A3", "A2")
laby.ajouter_arete("A2", "A1")
laby.ajouter_arete("B2", "C2")
laby.ajouter_arete("C2", "C3")
laby.ajouter_arete("C2", "D2")
laby.ajouter_arete("D3", "D2")
laby.ajouter_arete("D3", "D4")
laby.ajouter_arete("C4", "D4")
laby.ajouter_arete("C4", "B4")
laby.ajouter_arete("A4", "B4")


print(laby.plus_court_chemin_detail("A0", "A4"))

g = nx.Graph()
for s in laby.get_sommets():
    g.add_node(s)

for s in laby.get_sommets():
    for a in laby.get_adjacents(s):
        g.add_edge(s, a)

nx.draw(g,with_labels=True)
plt.savefig("Graph.png", format="PNG")