#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Aug 21 10:10:53 2020

@auteur: Christophe Viroulaud
"""


class Date:

    # on définit une variable interne à la classe
    nom_mois = ["janvier", "février", "mars", "avril", "mai", "juin",
                "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

    def __init__(self, j: int, m: int, a: int):
        self.jour = j
        self.mois = m
        self.annee = a

    def afficher(self) -> str:
        return f"{self.jour} / {Date.nom_mois[self.mois - 1]} / {self.annee}"

    def est_avant(self, d) -> bool:
        # Le \ permet d'écrire sur plusieurs lignes
        # and est prioritaire devant or
        return self.annee < d.annee or \
            self.annee == d.annee and (self.mois < d.mois or \
                                       self.mois == d.mois and self.jour < d.jour)


d = Date(8, 12, 1977)
print(d.afficher())
print(d.est_avant(Date(9, 12, 1977)))
