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

    def rechercher(self, v: int) -> bool:
        """
        recherche v dans l'ABR
        en appelant la méthode rechercher de Noeud
        """
        if self.est_vide():
            return False
        else:
            return self.racine.rechercher(v)


if __name__ == "__main__":
    tab = [33, 25, 56, 20, 28, 40, 60, 8, 21, 26, 35, 58, 65]
    arbre = ABR()
    for e in tab:
        arbre.inserer(e)
    print(arbre.rechercher(21))
    print(arbre.rechercher(61))
