#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Sep  9 13:51:00 2020

@auteur: Christophe Viroulaud
"""


class Rectangle:

    def __init__(self, L: float, l: float):
        self.longueur = L
        self.largeur = l

    def get_longueur(self) -> float:
        return self.longueur

    def get_largeur(self) -> float:
        return self.largeur

    def perimetre(self) -> float:
        return (self.longueur + self.largeur)*2

    def aire(self) -> float:
        return round(self.longueur * self.largeur, 2)

    def est_carre(self) -> bool:
        return self.longueur == self.largeur

rect = Rectangle(5.3, 2.8)
print(rect.aire())
print(rect.est_carre())