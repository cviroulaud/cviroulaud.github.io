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

    def renverser(self)->None:
        res = None
        maillon_en_cours = self.tete
        while maillon_en_cours is not None:
            res = Maillon(maillon_en_cours.valeur, res)
            maillon_en_cours = maillon_en_cours.suivant
        # la liste est retournée on récupère la tête
        self.tete = res

    def concatener_rec(self, tete1: object, tete2: object)->object:
        """
        méthode interne pour additionner 2 listes
        """
        if tete1 is None:
            return tete2
        else:
            return Maillon(tete1.valeur, self.concatener_rec(tete1.suivant, tete2))

    def concatener(self, l: object)->object:
        """
        appel principal de la méthode récursive pour additionner 2 listes
        """
        res = Liste()
        res.tete = self.concatener_rec(self.tete, l.tete)
        return res

    def afficher_rec(self, maillon: object)->str:
        """
        crée la chaîne d'affichage pour __str__
        """
        if maillon is None:
            return "\n" # renvoi à la ligne
        else:
            return str(maillon.valeur)+" "+self.afficher_rec(maillon.suivant)

    def __str__(self):
        return self.afficher_rec(self.tete)

    def inserer_rec(self, val: int, lst: object)->object:
        """
        méthode interne pour recréer la liste avec l'élément inséré
        """
        if lst is None or val <= lst.valeur:
            return Maillon(val, lst)
        else:
            return Maillon(lst.valeur, self.inserer_rec(val, lst.suivant))

    def inserer(self, val: int)->None:
        """
        appel principal pour l'insertion dans une liste triée
        """
        self.tete = self.inserer_rec(val, self.tete)


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

print(lst)

lst.renverser()

print(lst)

lst2 = Liste()
lst2.ajoute(11)
lst2.ajoute(14)
lst2.ajoute(13)

lst_add = lst.concatener(lst2)

print(lst_add)

lst_triee = Liste()
lst_triee.ajoute(10)
lst_triee.ajoute(9)
lst_triee.ajoute(7)
lst_triee.ajoute(3)
lst_triee.ajoute(1)

print(lst_triee)

lst_triee.inserer(4)

print(lst_triee)

lst_triee.inserer(12)

print(lst_triee)

lst_triee.inserer(0)

print(lst_triee)