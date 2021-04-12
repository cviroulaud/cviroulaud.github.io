#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Oct 28 14:40:05 2020

@auteur: Christophe Viroulaud
"""


class Graphe:
    """
    Crée un graphe sous forme de dictionnaire d'adjacence
    """

    def __init__(self):
        self.sommets = {}

    def ajouter_sommet(self, s)->None:
        if not(s in self.sommets):
            self.sommets[s] = set()

    def ajouter_arete(self, s1, s2)->None:
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.sommets[s1].add(s2)
        self.sommets[s2].add(s1)

    def sont_relies(self, s1, s2)->bool:
        return s1 in self.sommets[s2]

    def get_adjacents(self, s)->set:
        return self.sommets[s]

    def get_sommets(self)->list:
        return list(self.sommets)