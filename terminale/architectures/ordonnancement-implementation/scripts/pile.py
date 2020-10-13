#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Oct 13 08:39:55 2020

@auteur: Christophe Viroulaud
"""


class Noeud:
    def __init__(self,e,p):
        self.donnees = e
        self.precedant = p


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
            self.dernier = self.dernier.precedant
            return res

    def __str__(self):
        affiche = ""
        last = self.dernier
        while last is not None:
            affiche += str(last.donnees) +"\n"
            last = last.precedant
        return affiche

if __name__ == "__main__":
    p = Pile()
    p.empiler(3)
    p.empiler(9)
    p.empiler(4)
    print(p)
    print("dépile:",p.depiler())
    print(p)
