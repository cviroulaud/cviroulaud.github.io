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

    def afficher(self)->str:
        chaine = ""
        for sommet, voisins in self.sommets.items():
            chaine += sommet + " { "
            for voisin in voisins:
                chaine += voisin + " "
            chaine += "}\n"
        return chaine

    # seconde possibilité
    def __str__(self):
        chaine = ""
        for s in self.sommets:
            if len(self.sommets[s]) == 0:
                # pour afficher {} au lieu de set()
                chaine += s + " " + "{}"
            else:
                chaine += s + " " + str(self.sommets[s]) + "\n"
        return chaine

    def nb_sommets(self)->int:
        return len(self.sommets)

    def degre(self, sommet: str)->int:
        return len(self.sommets[sommet])

    def nb_aretes(self)->int:
        nb = 0
        for s in self.sommets:
            nb += self.degre(s)
        return nb//2

    def supprimer(self, sommet: str)->None:
        for voisin in self.sommets[sommet]:
            # on supprime sommet dans tous ses voisins
            self.sommets[voisin].remove(sommet)
        # on supprime sommet
        del self.sommets[sommet]


if __name__ == "__main__":
    g = Graphe()
    g.ajouter_arete("A", "B")
    g.ajouter_arete("A", "C")
    g.ajouter_arete("A", "D")
    g.ajouter_arete("D", "B")
    g.ajouter_arete("D", "E")
    g.ajouter_arete("C", "E")
    g.ajouter_sommet("F")
    print(g.afficher())
    print(g)
    print("nombre de sommets:",g.nb_sommets())
    print("Le degré de A est:",g.degre("A"))
    print("nombre d'arêtes: ", g.nb_aretes())
    g.supprimer("A")
    print(g)

