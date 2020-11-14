#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Nov 11 14:20:02 2020

@auteur: Christophe Viroulaud
"""


from mod_graphe_pondere import Graphe
from graphviz import Graph

g = Graphe()
g.ajouter_arete("A", "B", 2)
g.ajouter_arete("A", "C", 7)
g.ajouter_arete("A", "D", 10)
g.ajouter_arete("D", "B", 8)
g.ajouter_arete("D", "E", 4)
g.ajouter_arete("C", "E", 2)
g.ajouter_sommet("F")
print(g)

dot = Graph(format="png")
sommets = g.get_sommets()
for s in sommets:
    dot.node(s, s)

deja_vus = set()
for s in sommets:
    # pour ne pas avoir double arête
    deja_vus.add(s)
    for adj in g.get_adjacents(s):
        if adj[0] not in deja_vus:
            dot.edge(s, adj[0], str(adj[1]))

dot.render(filename="test", view=True)