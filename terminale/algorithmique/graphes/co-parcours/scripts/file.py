#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Oct 13 08:50:49 2020

@auteur: Christophe Viroulaud
"""


class Noeud():
    def __init__(self,e,s):
        self.donnees = e
        self.successeur = s

    def __str__(self):
        return str(self.donnees) + '|'

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

    def __str__(self):
        c = self.premier
        s = ''
        while not c is None:
            s = s + c.__str__()
            c = c.successeur
        return '\u2BA4|' + s[:] + '\u2BA0'

if __name__ == "__main__":
    from random import randint

    a = File()
    for i in range(6):
        a.enfiler(randint(1, 6))
        print(a)

    for i in range(6):
        a.defiler()
        print(a)
