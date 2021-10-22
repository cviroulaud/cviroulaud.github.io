#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 22 Octobre 2021 14:39
"""

from time import time

NB = 100000


class Pile:
    def __init__(self):
        self.donnees = []

    def est_vide(self) -> bool:
        return self.donnees == []

    def empiler(self, e: int) -> None:
        self.donnees.append(e)

    def depiler(self) -> int:
        if not self.est_vide():
            return self.donnees.pop()

    def __str__(self) -> str:
        affiche = ""
        for x in self.donnees:
            affiche = str(x)+"\n"+affiche
        return affiche


class File:
    def __init__(self):
        self.donnees = []

    def est_vide(self) -> bool:
        return self.donnees == []

    def enfiler(self, e: int) -> None:
        self.donnees.append(e)

    def defiler(self) -> int:
        if not self.donnees == []:
            return self.donnees.pop(0)

    def __str__(self) -> str:
        affiche = ""
        for x in self.donnees:
            affiche += str(x) + " "
        return affiche


p = Pile()
deb = time()
for i in range(NB):
    p.empiler(i)
fin = time()
print("empiler ", fin-deb)

deb = time()
for i in range(NB):
    p.depiler()
fin = time()
print("dépiler ", fin-deb)

f = File()
deb = time()
for i in range(NB):
    f.enfiler(i)
fin = time()
print("enfiler ", fin-deb)

deb = time()
for i in range(NB):
    f.defiler()
fin = time()
print("défiler ", fin-deb)
