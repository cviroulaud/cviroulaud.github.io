#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mardi 21 Septembre 2021 12:50
"""
from random import randint


class Maillon:
    def __init__(self, v: int):
        self.val = v
        self.prec = None


class Liste:
    """
    construit une liste d'entiers aléatoires
    """

    def __init__(self):
        self.premier = None

    def initialisation(self, t: int) -> None:
        for _ in range(t):
            self.add_elt(randint(1, 100))

    def add_elt(self, n: int) -> None:
        m = Maillon(n)
        m.prec = self.premier
        self.premier = m

    def get_liste(self, m: Maillon) -> str:
        if m is not None:
            return str(m.val) + " - " + self.get_liste(m.prec)
        return "fin"

    def __str__(self):
        return self.get_liste(self.premier)


if __name__ == "__main__":
    l = Liste()
    l.initialisation(5)
    print(l)
