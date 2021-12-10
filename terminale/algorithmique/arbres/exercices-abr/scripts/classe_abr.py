#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Jeudi 09 Décembre 2021 22:06
"""


class Noeud:
    def __init__(self, v: int):
        self.valeur = v
        self.gauche = None
        self.droit = None

    def inserer(self, v: int) -> None:
        """
        insertion dans l'ABR
        on considère que chaque valeur n'apparait qu'une fois

        Args:
            v (int): valeur ajoutée
        """
        if v < self.valeur:  # gauche
            if self.gauche is None:  # feuille
                self.gauche = Noeud(v)
            else:  # descente récursive
                self.gauche.inserer(v)
        else:  # droite
            if self.droit is None:  # feuille
                self.droit = Noeud(v)
            else:  # descente récursive
                self.droit.inserer(v)

    def rechercher(self, v: int) -> None:
        if v == self.valeur:
            return True
        elif v < self.valeur:  # gauche
            if self.gauche is None:  # feuille
                return False
            else:  # descente récursive
                return self.gauche.rechercher(v)
        else:  # droite
            if self.droit is None:  # feuille
                return False
            else:  # descente récursive
                return self.droit.rechercher(v)

    def minimum(self) -> int:
        g = self.gauche
        while g.gauche is not None:
            g = g.gauche
        return g.valeur

    def minimum_rec(self) -> int:
        """
        trouve minimum = feuille gauche

        Returns:
            int: valeur mini de l'ABR
        """
        if self.gauche is None:
            return self.valeur
        else:
            return self.gauche.minimum_rec()

    def infixe(self, noeud: object, parcours: list) -> None:
        if n is not None:
            self.infixe(noeud.gauche, parcours)
            parcours.append(n.valeur)
            self.infixe(noeud.droit, parcours)


arbre = Noeud(13)
arbre.inserer(29)
arbre.inserer(2)
arbre.inserer(49)
arbre.inserer(8)
arbre.inserer(12)
arbre.inserer(16)
arbre.inserer(30)
arbre.inserer(27)
arbre.inserer(10)
arbre.inserer(9)

print(arbre.rechercher(16))  # True
print(arbre.rechercher(17))  # False
print(arbre.minimum())
print(arbre.minimum_rec())

parcours = []
arbre.infixe(arbre, parcours)
print(parcours)
