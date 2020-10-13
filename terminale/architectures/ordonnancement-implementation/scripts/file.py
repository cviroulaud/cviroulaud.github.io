#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Oct 13 08:50:49 2020

@auteur: Christophe Viroulaud
"""


class Noeud():
    def __init__(self,e,succ):
        self.e=e
        self.succ=succ

    def __str__(self):
        return str(self.e) + '|'

class File2():
    """
    avec liste simplement chainéé
    """
    def __init__(self):
        self.premier=None
        self.dernier=None

    def est_vide(self):
        return self.premier==None

    def enfiler(self,e):
        if self.est_vide():
            self.premier=Noeud(e,None)
            self.dernier=self.premier
        else:
            nouveau=Noeud(e,None)
            self.dernier.succ=nouveau
            self.dernier=nouveau

    def defiler(self):
        if not self.est_vide():
            res=self.premier.e
            self.premier=self.premier.succ
            return res

    def __str__(self):
        c = self.premier
        s = ''
        while not c is None:
            s = s + c.__str__()
            c = c.succ
        return '\u2BA4|' + s[:] + '\u2BA0'

from random import randint

a = File2()
for i in range(6):
    a.enfiler(randint(1, 6))
    print(a)

for i in range(6):
    a.defiler()
    print(a)
