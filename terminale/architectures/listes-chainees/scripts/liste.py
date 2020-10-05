#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Oct  2 14:02:05 2020

@auteur: Christophe Viroulaud
"""


class Maillon:
    """
    Crée un maillon de la liste chaînée
    """
    def __init__(self, val: int, suiv: object)->None:
        self.valeur = val
        self.suivant = suiv

class Liste:
    """
    Crée une liste chaînée
    """
    def __init__(self):
        self.tete: object = None

    def est_vide(self)->bool:
        return self.tete is None

    def ajoute(self, val: int)->None:
        self.tete = Maillon(val, self.tete)

    def __len__(self)->int:
        maillon = self.tete
        taille = 0
        while not(maillon == None):
            maillon = maillon.suivant
            taille += 1
        return taille

    def taille_rec(self, maillon: object)->int:
        """
        méthode interne pour calculer la taille de la chaîne
        """
        if maillon is None:
            return 0
        else:
            return 1 + self.taille_rec(maillon.suivant)

    def taille(self)->int:
        """
        appel principal de la méthode récursive pour mesurer
        la taille de la chaîne
        """
        return self.taille_rec(self.tete)

    def __getitem__(self, n: int)->object:
        """
        renvoie l'élément de rang n. Les indices commencent à 0.
        """
        maillon = self.tete
        i = 0
        while i < n and maillon is not None:
            maillon = maillon.suivant
            i += 1

        if maillon is None or n < 0:
                raise IndexError("indice invalide")

        return maillon.valeur

    def get_element_rec(self, n: int, maillon: object)->int:
        """
        méthode interne pour renvoyer le n-ième élément.
        """
        if maillon is None or n < 0:
            raise IndexError("indice invalide")
        if n == 0:
            return maillon.valeur
        else:
            return self.get_element_rec(n-1, maillon.suivant)

    def get_element(self, n: int)->int:
        """
        appel principal de la méthode récursive pour renvoyer le n-ième élément
        """
        return self.get_element_rec(n, self.tete)

lst = Liste()
lst.ajoute(8)
lst.ajoute(5)
lst.ajoute(3)
lst.ajoute(9)
print(len(lst))
print(lst.taille())
print(lst[3])
print(lst.get_element(3))