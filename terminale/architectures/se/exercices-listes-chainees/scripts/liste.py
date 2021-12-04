#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mercredi 06 Octobre 2021 23:01
"""


class Maillon:
    """
    Crée un maillon de la liste chaînée
    """

    def __init__(self, val: int, suiv: object) -> None:
        self.valeur = val
        self.suivant = suiv


class Liste:
    """
    Crée une liste chaînée
    """

    def __init__(self):
        self.tete: Maillon = None

    def ajoute(self, val: int) -> None:
        self.tete = Maillon(val, self.tete)

    def dernier(self) -> int:
        # gestion d'erreur
        if self.tete is None:
            return -1

        en_cours = self.tete
        while en_cours.suivant is not None:
            en_cours = en_cours.suivant
        return en_cours.valeur

    def dernier_aux(self, en_cours: Maillon) -> int:
        if en_cours.suivant is None:
            return en_cours.valeur
        else:
            return self.dernier_aux(en_cours.suivant)

    def dernier_rec(self) -> int:
        # gestion d'erreur
        if self.tete is None:
            return -1

        return self.dernier_aux(self.tete)

    def renverser(self) -> None:
        res = None
        en_cours = self.tete
        while en_cours is not None:
            # crée maillon et l'attache au précédant
            res = Maillon(en_cours.valeur, res)
            # va voir le maillon suivant
            en_cours = en_cours.suivant
        self.tete = res

    def dupliquer(self):
        en_cours = self.tete
        while en_cours is not None:
            doublon = Maillon(en_cours.valeur, en_cours.suivant)
            en_cours.suivant = doublon
            en_cours = doublon.suivant

    def __str__(self):
        m = self.tete
        s = ""
        while m is not None:
            s += str(m.valeur)+" - "
            m = m.suivant
        else:
            s += "fin"
        return s


lst = Liste()
lst.ajoute(8)
lst.ajoute(5)
lst.ajoute(3)
lst.ajoute(9)
lst.ajoute(10)
print(lst)
print("dernier", lst.dernier())
print("dernier_rec", lst.dernier_rec())

lst.renverser()
print(lst)
lst.dupliquer()
print(lst)
