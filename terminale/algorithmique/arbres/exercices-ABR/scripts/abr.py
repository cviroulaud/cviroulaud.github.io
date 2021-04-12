#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Feb 22 10:28:12 2021

@auteur: Christophe Viroulaud
"""


class Noeud:

    def __init__(self, v, g=None, d=None):
        self.valeur = v
        self.gauche = g
        self.droite = d

    def inserer(self, v: int) -> None:
        """
        crée un Noeud dans le sous-arbre gauche ou droit
        """
        if v < self.valeur:
            if self.gauche is None:
                self.gauche = Noeud(v)
            else:
                self.gauche.inserer(v)
        elif v > self.valeur:  # permet de ne pas ajouter une valeur déjà présente
            if self.droite is None:
                self.droite = Noeud(v)
            else:
                self.droite.inserer(v)

    def rechercher(self, v: int) -> bool:
        """
        recherche v dans les sous-arbre gauche ou droit
        """
        if v == self.valeur:
            return True
        elif v < self.valeur:
            if self.gauche is None:
                return False
            else:
                return self.gauche.rechercher(v)
        elif v > self.valeur:
            if self.droite is None:
                return False
            else:
                return self.droite.rechercher(v)


class ABR:

    def __init__(self):
        self.racine = None

    def est_vide(self) -> bool:
        return self.racine is None

    def inserer(self, v: int) -> None:
        """
        insère v dans l'ABR
        en appelant la méthode inserer de Noeud
        """
        if self.est_vide():
            # création de la racine
            self.racine = Noeud(v)
        else:
            # appel de la méthode inserer de Noeud
            self.racine.inserer(v)

    #DODO ABR faire méthode supprimer en s'aidant de ABRpourNSI.py
    
    def rechercher(self, v: int) -> bool:
        """
        recherche v dans l'ABR
        en appelant la méthode rechercher de Noeud
        """
        if self.est_vide():
            return False
        else:
            return self.racine.rechercher(v)
    
    def minimum(self)->int:
        """
        Returns:
            int: la valeur minimum de l'ABR
        """
        if self.est_vide():
            return None
        else:
            en_cours = self.racine
            while en_cours.gauche is not None:
                en_cours = en_cours.gauche
            return en_cours.valeur
    
    def maximum_rec(self, n: Noeud)->int:
        """
        méthode interne récursive de recherche du max
        """
        if n is None:
            return None
        else:
            if n.droite is None:
                return n.valeur
            else:
                return self.maximum_rec(n.droite)
    
    def maximum(self)->int:
        """
        Returns:
            int: la valeur maximum de l'ABR
        """
        return self.maximum_rec(self.racine)

    def infixe_rec(self, n: Noeud, parcours: list) -> list:
        """
        méthode interne du parcours infixe
        """
        if n is None:
            return
        self.infixe_rec(n.gauche, parcours)
        parcours.append(n.valeur)
        self.infixe_rec(n.droite, parcours)
        return parcours

    def infixe(self) -> list:
        return self.infixe_rec(self.racine, [])

    def infixe2(self) -> list:
        """
        avec une fonction interne
        """
        def infixe_rec(n: Noeud, parcours: list) -> list:
            """
            méthode interne du parcours infixe
            """
            if n is None:
                return
            infixe_rec(n.gauche, parcours)
            parcours.append(n.valeur)
            infixe_rec(n.droite, parcours)
            return parcours

        return infixe_rec(self.racine, [])


if __name__ == "__main__":
    tab = [33, 25, 56, 20, 28, 40, 60, 8, 21, 26, 35, 58, 65]
    arbre = ABR()
    for e in tab:
        arbre.inserer(e)
    print(arbre.infixe())
    print(arbre.minimum())
    print(arbre.maximum())
