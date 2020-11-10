#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Oct 13 08:39:55 2020

@auteur: Christophe Viroulaud
"""


class Noeud:
    def __init__(self,e,s):
        self.donnees = e
        self.successeur = s


class Pile:
    def __init__(self):
        self.dernier = None

    def est_vide(self):
        return self.dernier is None

    def empiler(self,e):
        self.dernier = Noeud(e,self.dernier)

    def depiler(self):
        if not self.est_vide():
            res = self.dernier.donnees
            self.dernier = self.dernier.successeur
            return res

class File():
    def __init__(self):
        self.premier = None
        self.dernier = None

    def est_vide(self):
        return self.premier == None

    def enfiler(self,e):
        if self.est_vide():
            # 1 seul élément: le premier est le dernier également
            self.premier = Noeud(e,None)
            self.dernier = self.premier
        else:
            nouveau = Noeud(e,None)
            # le dernier devient avant-dernier
            self.dernier.successeur = nouveau
            # le nouveau devient dernier
            self.dernier = nouveau

    def defiler(self):
        if not self.est_vide():
            res = self.premier.donnees
            self.premier = self.premier.successeur
            return res