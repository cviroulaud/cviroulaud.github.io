#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 18 Octobre 2021 13:46
"""


class Element:
    def __init__(self, d: int, s: object):
        self.donnees = d
        self.successeur = s


class Pile:
    def __init__(self):
        self.sommet = None

    def est_vide(self) -> bool:
        return self.sommet is None

    def empiler(self, e: int) -> None:
        self.sommet = Element(e, self.sommet)

    def depiler(self) -> int:
        # gestion d'erreur
        if not self.est_vide():
            # récupère la valeur du haut de la pile
            res = self.sommet.donnees
            # retire le sommet
            self.sommet = self.sommet.successeur
            return res

    def __str__(self):
        affiche = ""
        last = self.sommet
        while last is not None:
            affiche += str(last.donnees) + "\n"
            last = last.successeur
        return affiche


if __name__ == "__main__":
    p = Pile()
    p.empiler(3)
    p.empiler(9)
    p.empiler(4)
    print(p)
    print("dépile:", p.depiler())
    print(p)
