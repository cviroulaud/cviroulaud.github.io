#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 11 Mars 2022 09:33
"""

from structures import Pile, File


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

    def dfs_it(self, s: str) -> list:
        """
        parcours en profondeur depuis un sommet s

        Args:
            s (str): départ

        Returns:
            list: sommets parcours
        """
        parcours = []
        p = Pile()
        p.empiler(s)
        while not p.est_vide():
            en_cours = p.depiler()
            if en_cours not in parcours:
                parcours.append(en_cours)

                for voisin in self.sommets[en_cours]:
                    p.empiler(voisin[0])

        return parcours

    def dfs_rec(self, s: str, parcours: list) -> None:
        """
        version récursive du parcours en profondeur

        Args:
            s (str): départ
            parcours (list): sommets traversés
        """
        if s not in parcours:
            parcours.append(s)
            for voisin in self.sommets[s]:
                self.dfs_rec(voisin[0], parcours)

    def bfs(self, s: str) -> list:
        """
        parcours en largeur partant de s
        """
        parcours = []
        f = File()
        f.enfiler(s)
        while not f.est_vide():
            en_cours = f.defiler()
            if en_cours not in parcours:
                parcours.append(en_cours)

                for voisin in self.sommets[en_cours]:
                    f.enfiler(voisin[0])

        return parcours

    def predecesseurs(self, dep: str) -> dict:
        """
        détermine le prédécesseur de chaque sommet
        pour avoir le plus court chemin partant de dep

        Args:
            dep (str): départ

        Returns:
            dict: les prédécesseurs
        """
        pred = {dep: None}
        f = File()
        f.enfiler(dep)
        while not f.est_vide():
            en_cours = f.defiler()
            for voisin in self.sommets[en_cours]:
                if voisin[0] not in pred:
                    # affecte le sommet de rang n au voisin de rang (n+1)
                    pred[voisin[0]] = en_cours
                    f.enfiler(voisin[0])

        return pred

    def plus_court(self, dep: str, arr: str) -> list:
        pred = self.predecesseurs(dep)
        en_cours = arr
        chemin = []
        while en_cours != None:
            chemin.append(en_cours)
            en_cours = pred[en_cours]
        return chemin


if __name__ == "__main__":
    exemple = Graphe(True)
    exemple.ajouter_arete("A", "D")
    exemple.ajouter_arete("D", "C")
    exemple.ajouter_arete("B", "A")
    exemple.ajouter_arete("B", "C")
    exemple.affiche_voisins("B")
    print(exemple.dfs_it("A"))
    parcours_rec = []
    exemple.dfs_rec("A", parcours_rec)
    print(parcours_rec)
    print(exemple.bfs("A"))
