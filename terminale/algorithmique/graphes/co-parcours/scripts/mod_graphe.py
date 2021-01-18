#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Oct 28 14:40:05 2020

@auteur: Christophe Viroulaud
"""

from structures import Pile, File

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

    def DFS(self,depart: str)->list:
        p = Pile()
        p.empiler(depart)
        visites = []
        while not(p.est_vide()):
            en_cours = p.depiler()
            if not(en_cours in visites):
                visites.append(en_cours)
                for voisin in self.sommets[en_cours]:
                    p.empiler(voisin)
        return visites

    def DFS_rec(self, depart: str, visites: list = [])->list:
        # !!!attention effet de bord avec 'visites'
        # faire une fonction interne et un appel principal
        if not(depart in visites):
            visites.append(depart)
            for voisin in self.sommets[depart]:
                self.DFS_rec(voisin, visites)
        return visites

    def est_connexe(self)->bool:
        list_sommets = self.get_sommets()
        return len(self.DFS(list_sommets[0])) == len(list_sommets)

    def BFS(self,depart: str)->list:
        f = File()
        f.enfiler(depart)
        visites = []
        while not(f.est_vide()):
            en_cours = f.defiler()
            if not(en_cours in visites):
                visites.append(en_cours)
                for voisin in self.sommets[en_cours]:
                    f.enfiler(voisin)
        return visites

    def plus_court_chemin(self, depart: str, arrivee: str)->int:
        f = File()
        f.enfiler(depart)
        visites = []
        distances = {depart: 0}
        while not(f.est_vide()):
            en_cours = f.defiler()
            if not(en_cours in visites):
                visites.append(en_cours)
                for voisin in self.sommets[en_cours]:
                    f.enfiler(voisin)
                    # on remplit le tableau des distances
                    if voisin not in distances:
                        distances[voisin] = distances[en_cours]+1
        return distances[arrivee]

    def plus_court_chemin_detail(self, depart: str, arrivee: str)->list:
        f = File()
        f.enfiler(depart)
        visites = []
        predecesseur = {depart: None}
        while not(f.est_vide()):
            en_cours = f.defiler()
            if not(en_cours in visites):
                visites.append(en_cours)
                for voisin in self.sommets[en_cours]:
                    f.enfiler(voisin)
                    # on remplit le tableau des prédecesseurs
                    if voisin not in predecesseur:
                        predecesseur[voisin] = en_cours

        # L'arrivée est-elle atteignable?
        if not(arrivee in predecesseur):
            return None

        # reconstruction du chemin en partant de l'arrivée
        chemin = []
        position = arrivee
        while position is not None:
            chemin.append(position)
            position = predecesseur[position]
        # le chemin a été construit à l'envers
        chemin.reverse()
        return chemin
