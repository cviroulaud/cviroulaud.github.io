#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sun Nov 22 11:35:01 2020

@auteur: Christophe Viroulaud
"""


from mod_graphe import Graphe
import networkx as nx
import matplotlib.pyplot as plt

rive = Graphe()
rive.ajouter_sommet("chou, chèvre, loup, berger")
rive.ajouter_sommet("chèvre, loup, berger")
rive.ajouter_sommet("chou, loup, berger")
rive.ajouter_sommet("chou, chèvre, berger")
rive.ajouter_sommet("chèvre, berger")
rive.ajouter_sommet("chou, loup")
rive.ajouter_sommet("loup")
rive.ajouter_sommet("chèvre")
rive.ajouter_sommet("chou")
rive.ajouter_sommet("-")

rive.ajouter_arete("chou, chèvre, loup, berger", "chou, loup")
rive.ajouter_arete("chèvre, loup, berger", "loup")
rive.ajouter_arete("chèvre, loup, berger", "chèvre")
rive.ajouter_arete("chou, loup, berger", "loup")
rive.ajouter_arete("chou, loup, berger", "chou")
rive.ajouter_arete("chou, loup, berger", "chou, loup")
rive.ajouter_arete("chou, chèvre, berger", "chou")
rive.ajouter_arete("chou, chèvre, berger", "chèvre")
rive.ajouter_arete("chèvre, berger", "chèvre")
rive.ajouter_arete("chèvre, berger", "-")

print(rive.plus_court_chemin_detail("chou, chèvre, loup, berger", "-"))

g = nx.Graph()
for s in rive.get_sommets():
    g.add_node(s)

for s in rive.get_sommets():
    for a in rive.get_adjacents(s):
        g.add_edge(s, a)

nx.draw(g,with_labels=True)
plt.savefig("Graph.png", format="PNG")