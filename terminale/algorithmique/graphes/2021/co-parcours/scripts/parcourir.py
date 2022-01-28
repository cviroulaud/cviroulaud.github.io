#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Nov  6 16:32:57 2020

@auteur: Christophe Viroulaud
"""


from mod_graphe import Graphe

g = Graphe()
g.ajouter_arete("I", "H")
g.ajouter_arete("G", "H")
g.ajouter_arete("A", "H")
g.ajouter_arete("E", "B")
g.ajouter_arete("A", "C")
g.ajouter_arete("E", "C")
g.ajouter_arete("A", "J")
g.ajouter_arete("D", "C")
g.ajouter_arete("J", "D")
g.ajouter_arete("D", "F")

print(g.DFS("I"))
print(g.DFS_rec("I"))
print(g.BFS("H"))
print(g.plus_court_chemin("H", "E"))
print(g.plus_court_chemin_detail("H", "E"))