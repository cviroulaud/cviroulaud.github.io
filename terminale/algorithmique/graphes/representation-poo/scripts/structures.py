#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 18 Février 2022 20:25
"""


class Noeud:
    def __init__(self, nom: str, suivant: object):
        self.nom = nom
        self.suivant = suivant

    def get_nom(self) -> int:
        return self.nom

    def set_nom(self, n: int) -> None:
        self.nom = n

    def get_suivant(self) -> object:
        return self.suivant

    def set_suivant(self, s: object) -> None:
        self.suivant = s


class Pile:
    def __init__(self):
        self.sommet = None

    def est_vide(self) -> bool:
        return self.sommet is None

    def empiler(self, n: int) -> None:
        self.sommet = Noeud(n, self.sommet)

    def depiler(self) -> int:
        res = -1
        if not self.est_vide():
            res = self.sommet.get_nom()
            self.sommet = self.sommet.get_suivant()
        return res


class File:
    def __init__(self):
        self.premier = None
        self.dernier = None

    def est_vide(self) -> bool:
        return self.premier is None

    def enfiler(self, n: int) -> None:
        nouveau = Noeud(n, None)
        if self.est_vide():
            self.premier = nouveau
        else:
            self.dernier.set_suivant(nouveau)
        self.dernier = nouveau

    def defiler(self) -> int:
        res = -1
        if not self.est_vide():
            res = self.premier.get_nom()
            self.premier = self.premier.get_suivant()
        return res


if __name__ == "__main__":
    p = Pile()
    p.empiler(1)
    p.empiler(2)
    p.empiler(3)
    print(p.depiler())
    print(p.depiler())

    f = File()
    f.enfiler(1)
    f.enfiler(2)
    f.enfiler(3)
    print(f.defiler())
    print(f.defiler())
