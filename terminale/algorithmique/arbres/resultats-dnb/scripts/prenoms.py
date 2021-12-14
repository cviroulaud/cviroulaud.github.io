#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 13 Décembre 2021 12:52
"""

import csv


class Prenom:
    def __init__(self, p: str):
        self.prenom = p
        self.annees = {}
        self.gauche = None
        self.droite = None

    def get_prenom(self) -> str:
        return self.prenom

    def ajoute_annee(self, a: str, nb: str) -> None:
        """
        ajoute l'année dans le dict
        converti le nb en entier

        Args:
            a (str): année (peut être "XXXX")
            nb (str): nb de naissance 
        """
        self.annees[a] = int(nb)

    def get_total(self) -> int:
        """
        nombre total d'occurrences du prénom

        Returns:
            int: total
        """
        tot = 0
        for an, val in self.annees.items():
            tot = tot + val
        return tot

    def insere_fils(self, data: dict) -> None:
        prenom = data["preusuel"]
        if prenom == self.get_prenom():
            self.ajoute_annee(data["annais"], data["nombre"])
        elif prenom < self.get_prenom():
            if self.gauche is None:
                self.gauche = Prenom(prenom)
                self.gauche.ajoute_annee(data["annais"], data["nombre"])
            else:
                self.gauche.insere_fils(data)
        else:
            if self.droite is None:
                self.droite = Prenom(prenom)
                self.droite.ajoute_annee(data["annais"], data["nombre"])
            else:
                self.droite.insere_fils(data)


class Arbre:
    def __init__(self):
        self.racine = None

    def insere_prenom(self, data: dict) -> None:
        prenom = data["preusuel"]
        if self.racine is None:
            self.racine = Prenom(prenom)
            self.racine.ajoute_annee(data["annais"], data["nombre"])
        else:
            self.racine.insere_fils(data)


f = open("nat2020.csv")
dico = csv.DictReader(f, delimiter=";")
arbre = Arbre()
for ligne in dico:
    arbre.insere_prenom(ligne)
f.close()

print(arbre.racine.get_prenom())
