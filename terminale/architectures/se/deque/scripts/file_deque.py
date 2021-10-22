#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Oct 16 11:33:15 2020

@auteur: Christophe Viroulaud
"""


from collections import deque
from time import time

NB = 100000


class File2:
    def __init__(self):
        self.donnees = deque()

    def est_vide(self) -> bool:
        return len(self.donnees) == 0

    def enfiler(self, e: int) -> None:
        self.donnees.append(e)

    def defiler(self) -> int:
        if not self.est_vide():
            return self.donnees.popleft()

    def __str__(self) -> str:
        affiche = ""
        for x in self.donnees:
            affiche += str(x) + " "
        return affiche


f = File2()
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
