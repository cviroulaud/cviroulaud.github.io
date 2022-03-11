#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 11 Mars 2022 09:33
"""


class Graphe:
    """
    Crée un graphe sous forme de dictionnaire d'adjacence
    """

    def __init__(self, oriente: bool):
        self.sommets = {}
        self.oriente = oriente

    def ajouter_sommet(self, s: str) -> None:
        """
        crée un nouveau sommet
        """
        if not(s in self.sommets):
            self.sommets[s] = set()

    def ajouter_arete(self, s1: str, s2: str, d: int = 1) -> None:
        """
        crée une arête de s1 vers s2 sous la forme d'un tuple
        (voisin, distance)
        crée les sommets s'ils n'existent pas déjà
        """
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.sommets[s1].add((s2, d))
        if not self.oriente:
            self.sommets[s2].add((s1, d))

    def affiche_voisins(self, s: str) -> None:
        for v in self.sommets[s]:
            print(f"{s} --> {v[0]} : {v[1]}")

    def sont_relies(self, s1, s2) -> bool:
        return s1 in self.sommets[s2]

    def get_adjacents(self, s) -> set:
        return self.sommets[s]

    def get_sommets(self) -> list:
        return list(self.sommets)


if __name__ == "__main__":
    exemple = Graphe(True)
    exemple.ajouter_arete("A", "D")
    exemple.ajouter_arete("D", "C")
    exemple.ajouter_arete("B", "A")
    exemple.ajouter_arete("B", "C")
    exemple.affiche_voisins("B")
