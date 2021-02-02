#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Feb  2 08:25:21 2021

@auteur: Christophe Viroulaud
"""


class Arbre_binaire:

    def __init__(self, h: int)->None:
        """
        Initialise un tableau correspondant à la hauteur 'h' de l'arbre
        Le premier noeud est 'r'
        """
        self.hauteur = h
        self.arbre= [None for _ in range(2**h - 1)]
        self.arbre[0] = "r"

    def inserer(self, pere: str, fils_g: str, fils_d: str)->None:
        """
        insère les fils gauche et droit du noeud père
        """
        i_pere = self.arbre.index(pere)
        #vérification de sortie de l'arbre
        assert 2*i_pere < len(self.arbre), "Ce nœud n'a pas de fils"
        self.arbre[2*i_pere + 1] = fils_g
        self.arbre[2*i_pere + 2] = fils_d

    def prefixe(self, parcours: list, i: int = 0)->list:
        if i >= len(self.arbre) or self.arbre[i] is None:
            return
        else:
            parcours.append(self.arbre[i])
            self.prefixe(parcours, 2*i+1)
            self.prefixe(parcours, 2*i+2)
        return parcours

    def prefixe2(self, i: int = 0)->list:
        """ création de la liste au fur et à mesure des appels"""
        if i >= len(self.arbre) or self.arbre[i] is None:
            return []
        else:
            return [self.arbre[i]] + self.prefixe2(2*i+1) + self.prefixe2(2*i+2)

    def infixe(self, parcours: list, i: int = 0)->list:
        if i >= len(self.arbre) or self.arbre[i] is None:
            return
        else:
            self.infixe(parcours, 2*i+1)
            parcours.append(self.arbre[i])
            self.infixe(parcours, 2*i+2)
        return parcours

    def infixe2(self, i: int = 0)->list:
        """ création de la liste au fur et à mesure des appels"""
        if i >= len(self.arbre) or self.arbre[i] is None:
            return []
        else:
            return self.infixe2(2*i+1) + [self.arbre[i]] + self.infixe2(2*i+2)

    def postfixe(self, parcours: list, i: int = 0)->list:
        if i >= len(self.arbre) or self.arbre[i] is None:
            return
        else:
            self.postfixe(parcours, 2*i+1)
            self.postfixe(parcours, 2*i+2)
            parcours.append(self.arbre[i])
        return parcours

    def postfixe2(self, i: int = 0)->list:
        """ création de la liste au fur et à mesure des appels"""
        if i >= len(self.arbre) or self.arbre[i] is None:
            return []
        else:
            return self.postfixe2(2*i+1) + self.postfixe2(2*i+2) + [self.arbre[i]]


arbre_car = Arbre_binaire(5)
arbre_car.inserer("r", "a", "b")
arbre_car.inserer("a", "c", "d")
arbre_car.inserer("c", "g", "h")
arbre_car.inserer("d", "i", "j")
arbre_car.inserer("j", "l", None)
arbre_car.inserer("b", "e", "f")
arbre_car.inserer("e", "k", None)

print(arbre_car.arbre)
print(arbre_car.prefixe([]))
print(arbre_car.prefixe2())
print(arbre_car.infixe([]))
print(arbre_car.infixe2())
print(arbre_car.postfixe([]))
print(arbre_car.postfixe2())

