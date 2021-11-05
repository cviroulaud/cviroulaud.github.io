#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Oct 16 11:33:15 2020

@auteur: Christophe Viroulaud
"""


class Pile:
    def __init__(self):
        self.donnees = []

    def est_vide(self):
        return self.donnees == []

    def empiler(self, e):
        self.donnees.append(e)

    def depiler(self):
        if not self.est_vide():
            return self.donnees.pop()

    def __str__(self):
        affiche =""
        for x in self.donnees:
            affiche = str(x)+"\n"+affiche
        return affiche

class File:
    def __init__(self):
        self.donnees = []

    def est_vide(self):
        return self.donnees == []

    def enfiler(self, e):
        self.donnees.append(e)

    def defiler(self):
        if not self.donnees == []:
            return self.donnees.pop(0)

    def __str__(self):
        affiche = ""
        for x in self.donnees:
            affiche += str(x) + " "
        return affiche

from collections import deque

class File2:
    def __init__(self):
        self.donnees = deque()

    def est_vide(self):
        return len(self.donnees) == 0

    def enfiler(self, e):
        self.donnees.append(e)

    def defiler(self):
        if not self.est_vide():
            return self.donnees.popleft()

    def __str__(self):
        affiche = ""
        for x in self.donnees:
            affiche += str(x) + " "
        return affiche

from time import time

NB = 100000

p = Pile()
deb = time()
for i in range(NB):
    p.empiler(i)
fin = time()
print("empiler ",fin-deb)

deb = time()
for i in range(NB):
    p.depiler()
fin = time()
print("dépiler ",fin-deb)

f = File()
deb = time()
for i in range(NB):
    f.enfiler(i)
fin = time()
print("enfiler ",fin-deb)

deb = time()
for i in range(NB):
    f.defiler()
fin = time()
print("défiler ",fin-deb)

f = File2()
deb = time()
for i in range(NB):
    f.enfiler(i)
fin = time()
print("enfiler ",fin-deb)

deb = time()
for i in range(NB):
    f.defiler()
fin = time()
print("défiler ",fin-deb)
