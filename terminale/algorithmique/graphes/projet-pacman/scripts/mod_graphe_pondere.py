#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Nov 11 14:20:02 2020

@auteur: Christophe Viroulaud
"""

from graphviz import Graph

class Graphe:
    """
    Crée un graphe sous forme de dictionnaire d'adjacence
    """

    def __init__(self):
        self.sommets = {}

    def ajouter_sommet(self, s)->None:
        if not(s in self.sommets):
            self.sommets[s] = set()

    def ajouter_arete(self, s1, s2, dist)->None:
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.sommets[s1].add((s2,dist))
        self.sommets[s2].add((s1,dist))

    def sont_relies(self, s1, s2)->bool:
        for adj in self.sommets[s2]:
            if adj[0] == s1:
                return True
        return False

    def get_adjacents(self, s)->set:
        """
        retourne un ensemble de tuple
        (sommet, distance)
        """
        return self.sommets[s]

    def get_sommets(self)->list:
        return list(self.sommets)

    def afficher(self, nom: str):
        """
        crée un image png du graphe

        Parameters
        ----------
        nom : str
            nom du fichier.
        """
        dot = Graph(format="png")
        sommets = self.get_sommets()
        for s in sommets:
            dot.node(str(s), str(s))

        deja_vus = set()
        for s in sommets:
            # pour ne pas avoir double arête
            deja_vus.add(s)
            for adj in self.get_adjacents(s):
                if adj[0] not in deja_vus:
                    dot.edge(str(s), str(adj[0]), str(adj[1]))

        dot.render(filename=nom, view=True)

    def arbre_couvrant_mini(self):
        """
        implémentation de l'algorithme de Prim
        """
        sommets = self.get_sommets()
        deja_vus = set()
        en_cours = sommets.pop()
        deja_vus.add(en_cours)
        aretes = set()
        solution = set()
        while not(len(deja_vus) == len(sommets)+1):
            # ajoute tous les voisins (non visités) de en_cours
            for voisin in self.get_adjacents(en_cours):
                if voisin[0] not in deja_vus:
                    aretes.add(voisin)

            # recherche l'arête minimale
            mini = aretes.pop()
            for a in aretes:
                if not(a[0] in deja_vus) and  a[1] < mini[1]:
                        mini = a

            solution.add((en_cours, mini[0], mini[1]))
            en_cours = mini[0]
            deja_vus.add(en_cours)

        return solution




    def __str__(self):
        chaine = ""
        for s in self.sommets:
            if len(self.sommets[s]) == 0:
                # pour afficher {} au lieu de set()
                chaine += s + " " + "{}"
            else:
                chaine += s + " " + str(self.sommets[s]) + "\n"
        return chaine

if __name__ == "__main__":
    g = Graphe()
    g.ajouter_arete("A", "B", 2)
    g.ajouter_arete("A", "C", 3)
    g.ajouter_arete("A", "D", 10)
    g.ajouter_arete("D", "B", 8)
    g.ajouter_arete("D", "E", 4)
    g.ajouter_arete("C", "E", 2)
    g.ajouter_sommet("F")
    print(g)
    print(g.get_adjacents("A"))