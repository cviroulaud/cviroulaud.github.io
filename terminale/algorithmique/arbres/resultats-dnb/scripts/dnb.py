#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 13 Décembre 2021 12:52
"""

import csv


class College:
    def __init__(self, data: dict):
        self.id = data["num_etab"]
        self.nom = data["patronyme"]
        self.ville = data["lib_commune"]
        self.departement = data["lib_dep"]
        self.taux = float(data["taux"])
        self.gauche = None
        self.droite = None

    def insere_fils(self, data: dict) -> None:
        """
        ajoute un fils au noeud en cours

        Args:
            data (dict): données du fils
        """
        id_fils = data["num_etab"]
        if id_fils < self.id:  # gauche
            if self.gauche is None:
                self.gauche = College(data)
            else:
                self.gauche.insere_fils(data)
        else:  # droite
            if self.droite is None:
                self.droite = College(data)
            else:
                self.droite.insere_fils(data)

    def recherche_fils(self, id_fils: str) -> float:
        """
        taux de réussite du collège

        Args:
            id_fils (str): identifiant du collège

        Returns:
            float: taux de réussite ou -1 si pas trouvé
        """
        if id_fils == self.id:  # collège trouvé
            return self.taux
        elif id_fils < self.id:  # gauche
            if self.gauche is None:
                return -1
            else:
                return self.gauche.recherche_fils(id_fils)
        else:  # droite
            if self.droite is None:
                return -1
            else:
                return self.droite.recherche_fils(id_fils)


class Arbre:
    def __init__(self):
        self.racine = None

    def insere_college(self, data: dict) -> None:
        """
        ajoute un collège dans l'arbre

        Args:
            data (dict): info du collège
        """
        if self.racine is None:
            self.racine = College(data)
        else:
            self.racine.insere_fils(data)

    def recherche_college(self, id: str) -> float:
        """
        cherche le taux de réussite d'un collège

        Args:
            id (str): identifiant du collège

        Returns:
            float: taux de réussite
        """
        if self.racine.id is None:
            return -1
        else:
            return self.racine.recherche_fils(id)


f = open("dnb2018.csv")
dico = csv.DictReader(f)
arbre = Arbre()
for ligne in dico:
    arbre.insere_college(ligne)
f.close()

print(arbre.recherche_college("0241042C"), "%")
print(arbre.recherche_college("000"), "%")
