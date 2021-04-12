#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Oct 16 13:13:49 2020

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

    def __str__(self):
        affiche = ""
        last = self.dernier
        while last is not None:
            affiche += str(last.donnees) +"\n"
            last = last.successeur
        return affiche

class File:
    def __init__(self):
        self.gauche = Pile()
        self.droite = Pile()

    def enfiler(self, e: int)->None:
        self.gauche.empiler(e)

    def defiler(self)->int:
        if self.droite.est_vide():
            while not self.gauche.est_vide():
                self.droite.empiler(self.gauche.depiler())
        return self.droite.depiler()

file = File()
for i in range(4):
    file.enfiler(i)

print(file.defiler())