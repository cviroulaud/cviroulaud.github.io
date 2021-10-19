#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 18 Octobre 2021 23:11
"""


class Element():
    def __init__(self, d: int, s: object):
        self.donnees = d
        self.successeur = s


class File():
    def __init__(self):
        self.premier = None
        self.dernier = None

    def est_vide(self) -> bool:
        return self.premier == None

    def enfiler(self, e: int) -> None:
        nouveau = Element(e, None)

        if self.est_vide():
            # 1 seul élément: le premier est le dernier
            self.premier = nouveau
        else:
            # le dernier devient avant-dernier
            self.dernier.successeur = nouveau

        # le nouveau devient dernier
        self.dernier = nouveau

    def defiler(self) -> int:
        if not self.est_vide():
            res = self.premier.donnees
            self.premier = self.premier.successeur
            return res

    def __str__(self):
        c = self.premier
        s = ""
        while not c is None:
            s = s + str(c.donnees)+"|"
            c = c.successeur
        return "\u2BA4|" + s[:] + "\u2BA0"


if __name__ == "__main__":
    from random import randint

    a = File()
    for i in range(6):
        a.enfiler(randint(1, 20))
        print(a)

    for i in range(6):
        a.defiler()
        print(a)
