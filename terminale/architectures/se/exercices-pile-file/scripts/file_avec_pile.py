#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mardi 19 Octobre 2021 09:15
"""

from pile import Pile
from random import randint


class File2:
    def __init__(self):
        self.gauche = Pile()
        self.droite = Pile()

    def est_vide(self) -> bool:
        return self.gauche.est_vide() and self.droite.est_vide()

    def enfiler(self, e: int) -> None:
        self.gauche.empiler(e)

    def defiler(self) -> int:
        if self.droite.est_vide():
            while not self.gauche.est_vide():
                self.droite.empiler(self.gauche.depiler())

        return self.droite.depiler()

    def __str__(self):
        affiche = "gauche:\n"
        affiche += str(self.gauche)
        affiche += "\ndroite:\n"
        affiche += str(self.droite)
        return affiche


f = File2()
for i in range(5):
    f.enfiler(i)

print(f)
print("-----")

print("defiler", f.defiler())
print(f)
print("-----")

print("enfiler 5")
f.enfiler(5)
print(f)
print("-----")

while not f.est_vide():
    print("defiler", f.defiler())
