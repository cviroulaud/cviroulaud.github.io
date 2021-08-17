#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Jan 13 13:52:30 2021

@auteur: Christophe Viroulaud
"""


class ArbreBinaire:
    def __init__(self, valeur=None):
        if valeur is None:
            self.racine = None #arbre vide
        else:
            self.racine = valeur #une racine et deux sous-arbres
            self.gauche = ArbreBinaire()
            self.droit = ArbreBinaire()

    def insere(self, valeur):
        from random import randrange #insertion au hasard à gauche ou à droite
        if self.racine is None:
            self.racine = valeur
            self.gauche = ArbreBinaire()
            self.droit = ArbreBinaire()
        else:
            choix = randrange(0, 2)
            if choix == 0: #insertion à gauche
                if self.gauche.racine is None:
                    self.gauche = ArbreBinaire(valeur)
                else:
                    self.gauche.insere(valeur)
            else: #insertion à droite
                if self.droit.racine is None:
                    self.droit = ArbreBinaire(valeur)
                else:
                    self.droit.insere(valeur)

    def __contains__(self, x): # <==> x in arbre
        if self.racine == None:
            return False
        elif self.racine == x:
            return True
        else:
            return self.gauche.__contains__(x) or self.droit.__contains__(x)

    def est_vide(self):
        return self.racine is None

    def taille(self):
        if self.racine is None:
            return 0
        else:
            return 1 + self.gauche.taille() + self.droit.taille()

    def hauteur(self):
        if self.racine is None:
            return -1
        else:
            return 1 + max(self.gauche.hauteur(), self.droit.hauteur())

    def __repr__(self):
        return str(self.racine)

def test(n=200):
    """n : nombre de tests"""
    from random import randrange
    from math import log2
    moyenne = 0 #moyenne des rapports hauteur / (log2(taille)+1)
    for i in range(n):
        a = ArbreBinaire()
        taille = randrange(1, 512) #taille au hasard
        for i in range(taille):
            a.insere(i)
        moyenne = moyenne + a.hauteur() / (log2(taille)+1)
    moyenne = moyenne / n
    return moyenne

if __name__ == "__main__":
    print("moyenne des rapports hauteur / (log2(taille)+1):", test())