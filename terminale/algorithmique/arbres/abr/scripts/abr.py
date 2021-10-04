#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/08/06 11:01:49
"""


class Noeud:
    def __init__(self,val: int, d=None, g=None) -> None:
        self.valeur = val
        self.gauche = g
        self.droite = d


class Abr:
    def __init__(self):
        self.racine = None

    def inserer_rec(self, val: int, pere: Noeud) -> None:
        if val < pere.valeur:
            if pere.gauche is None:
                pere.gauche = Noeud(val)
            else:
                self.inserer_rec(val, pere.gauche)
        else:
            if pere.droite is None:
                pere.droite = Noeud(val)
            else:
                self.inserer_rec(val, pere.droite)

    def inserer(self, val: int) -> None:
        if self.racine is None:
            self.racine = Noeud(val)
        else:
            self.inserer_rec(val, self.racine)

    def rechercher_rec(self, val: int, pere: Noeud) -> bool:
        if pere is None:
            return False
        elif pere.valeur == val:
            return True
        elif val < pere.valeur:
            return self.rechercher_rec(val, pere.gauche)
        else:
            return self.rechercher_rec(val, pere.droite)

    def rechercher(self, val: int) -> bool:
        return self.rechercher_rec(val, self.racine)


if __name__ == "__main__":
    tab = [33, 25, 56, 20, 28, 40, 60, 8, 21, 26, 35, 58, 65]
    arbre = Abr()
    for e in tab:
        arbre.inserer(e)
    print(arbre.rechercher(21))
    print(arbre.rechercher(61))
