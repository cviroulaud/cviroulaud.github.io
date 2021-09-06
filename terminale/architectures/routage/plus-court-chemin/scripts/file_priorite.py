#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/09/05 21:43:21
"""


class File_priorite:
    def __init__(self):
        self.tas = []

    def est_vide(self):
        return len(self.tas) == 0

    def enfiler(self, noeud: tuple) -> None:
        """
        Args:
            noeud (tuple): (nom,distance calculée)
        """
        # ajoute à la fin
        self.tas.append(noeud)
        # remonte
        i_fils = len(self.tas)-1
        i_pere = (i_fils-1)//2
        # s'arrête tout seul à 0 (i_fils = i_pere = 0) <-- Non: voir Prim
        while i_fils == 0 or self.tas[i_fils][1] < self.tas[i_pere][1]:
            # inversion = remonte
            self.tas[i_fils], self.tas[i_pere] = self.tas[i_pere], self.tas[i_fils]
            # cas suivant
            i_fils = i_pere
            i_pere = (i_fils-1)//2

    def get_fils_mini(self, i_pere: int) -> int:
        """
        retourne l'indice du fils mini
        """
        i_fils = 2*i_pere+1
        if i_fils >= len(self.tas):
            return -1  # pas de fils
        if i_fils == len(self.tas)-1:
            return i_fils  # un seul fils gauche
        if self.tas[i_fils][1] > self.tas[i_fils+1][1]:
            i_fils += 1  # le fils droit est plus petit
        return i_fils

    def defiler(self) -> tuple:
        # retourne la racine
        res = self.tas[0]
        # remonte le dernier à la racine
        self.tas[0] = self.tas[len(self.tas)-1]
        self.tas.pop()
        # redescend sur le plus petit fils
        i_pere = 0
        i_fils = self.get_fils_mini(i_pere)
        while i_fils > 0 and self.tas[i_pere][1] > self.tas[i_fils][1]:
            # inversion = descend
            self.tas[i_fils], self.tas[i_pere] = self.tas[i_pere], self.tas[i_fils]
            # cas suivant
            i_pere = i_fils
            i_fils = self.get_fils_mini(i_pere)
        return res
