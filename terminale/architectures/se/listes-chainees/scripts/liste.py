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

    def est_vide(self) -> bool:
        return self.tete is None

    def ajoute(self, val: int) -> None:
        self.tete = Maillon(val, self.tete)

    def __len__(self) -> int:
        maillon = self.tete
        taille = 0
        while maillon is not None:
            maillon = maillon.suivant
            taille += 1
        return taille

    def taille_rec(self, m: Maillon) -> int:
        """
        méthode interne pour calculer la taille de la chaîne
        """
        if m is None:
            return 0
        else:
            return 1 + self.taille_rec(m.suivant)

    def taille(self) -> int:
        """
        appel principal de la méthode récursive pour mesurer
        la taille de la chaîne
        """
        return self.taille_rec(self.tete)

    def __getitem__(self, n: int) -> int:
        """
        renvoie l'élément de rang n. Les indices commencent à 0.
        """
        maillon = self.tete
        i = 0
        while i < n and maillon is not None:
            maillon = maillon.suivant
            i += 1

        if maillon is None:
            raise IndexError("indice invalide")

        return maillon.valeur

    def get_element_rec(self, n: int, m: Maillon) -> int:
        """
        méthode interne pour renvoyer le n-ième élément.
        """
        # n est plus grand que la taille de la liste
        if m is None:
            raise IndexError("indice invalide")
        if n == 0:
            return m.valeur
        else:
            return self.get_element_rec(n-1, m.suivant)

    def get_element(self, n: int) -> int:
        """
        appel principal de la méthode récursive pour renvoyer le n-ième élément
        """
        return self.get_element_rec(n, self.tete)

    def inserer_rec(self, val: int, n: int, m: object) -> None:
        """
        méthode interne pour placer val au rang n
        si n est trop grand, place l'élément en fin de liste
        """
        if m.suivant is None or n == 0:
            nouveau = Maillon(val, m.suivant)
            m.suivant = nouveau
        else:
            self.inserer_rec(val, n-1, m.suivant)

    def inserer(self, val: int, n: int) -> None:
        """
        appel principal de l'insertion pour placer val en n
        """
        # gestion du cas particulier où l'insertion est en début
        if n == 0:
            nouveau = Maillon(val, self.tete)
            self.tete = nouveau
        else:
            self.inserer_rec(val, n-1, self.tete)

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
print(lst)
print(len(lst))
print(lst.taille())
print(lst[3])
print(lst.get_element(3))
# insérer 6 au début
lst.inserer(6, 0)
print(lst)
# insérer 4 au rang 2
lst.inserer(4, 2)
print(lst)
# insérer 17 en fin
lst.inserer(17, 10)
print(lst)
