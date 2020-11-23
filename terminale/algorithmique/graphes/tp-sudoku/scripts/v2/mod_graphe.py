#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Oct 28 14:40:05 2020

@auteur: Christophe Viroulaud
"""


class Case:
    def __init__(self):
        self.voisins = set()
        self.val = 0

class Graphe:
    """
    Crée un graphe sous forme de tableau de tableaux de Case()
    à la dimension du sudoku
    ATTENTION: il ne s'agit pas d'une matrice d'ajacence
    """

    def __init__(self, taille):
        self.taille = taille
        self.sommets = [[Case() for _ in range(self.taille)] for _ in range(self.taille)]

    def ajouter_arete(self, s1: tuple, s2: tuple)->None:
        """
        ajoute les coordonnées du sommet adjacent dans
        l'ensemble attribut 'voisins'
        """
        self.sommets[s1[1]][s1[0]].voisins.add(s2)
        self.sommets[s2[1]][s2[0]].voisins.add(s1)

    def sont_relies(self, s1: tuple, s2: tuple)->bool:
        return s1 in self.sommets[s2[1]][s2[0]].voisins

    def get_adjacents(self, s)->set:
        """
        renvoie l'ensemble des coordonnées (tuple)
        des Case() voisines de s
        """
        return self.sommets[s[1]][s[0]].voisins

    def get_sommet(self, s: tuple)->Case:
        """
        renvoie la Case() de coordonnées s
        """
        return self.sommets[s[1]][s[0]]
