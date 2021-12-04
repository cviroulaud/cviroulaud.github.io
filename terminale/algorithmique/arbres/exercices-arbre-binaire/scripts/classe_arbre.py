#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 04 Décembre 2021 10:53
"""


class Arbre_binaire:
    def __init__(self, h: int):
        self.hauteur = h
        self.arbre = [None for i in range(2**(h+1)-1)]
        self.arbre[0] = "r"

    def get_taille(self) -> int:
        """
        taille de l'arbre

        Returns:
            int: nombre de noeuds dans l'arbre
        """
        taille = 0
        for elt in self.arbre:
            if elt is not None:
                taille += 1
        return taille

    def get_indice(self, chaine: str) -> int:
        """
        renvoie la position de la chaîne dans le tableau

        Args:
            chaine (str): la chaîne cherchée

        Returns:
            int: l'indice
        """
        i = 0
        while self.arbre[i] != chaine:
            i = i+1
        return i

    def inserer(self, pere: str, gauche: str, droit: str) -> None:
        """
        insère les fils gauche et droit de père

        Args:
            pere (str): noeud père
            gauche (str): noeud fils gauche
            droit (str): noeud fils droit
        """
        i_pere = self.get_indice(pere)
        #assert 2*i_pere+2 < len(self.arbre)
        assert 2*i_pere+2 < 2**(self.hauteur+1)-1, "dépassement de taille"
        self.arbre[2*i_pere+1] = gauche
        self.arbre[2*i_pere+2] = droit

    def prefixe(self, position: int, parcours: list) -> None:
        if position < len(self.arbre) and \
                self.arbre[position] is not None:
            parcours.append(self.arbre[position])
            self.prefixe(2*position+1, parcours)
            self.prefixe(2*position+2, parcours)

    def infixe(self, position: int, parcours: list) -> None:
        if position < len(self.arbre) and self.arbre[position] is not None:
            self.infixe(2*position+1, parcours)
            parcours.append(self.arbre[position])
            self.infixe(2*position+2, parcours)

    def postfixe(self, position: int, parcours: list) -> None:
        if position < len(self.arbre) and self.arbre[position] is not None:
            self.postfixe(2*position+1, parcours)
            self.postfixe(2*position+2, parcours)
            parcours.append(self.arbre[position])

    def prefixe_2(self, position: int) -> list:
        if position < len(self.arbre) and self.arbre[position] is not None:
            return [self.arbre[position]] + \
                self.prefixe_2(2*position+1) + \
                self.prefixe_2(2*position+2)
        else:  # cas limite
            return []


if __name__ == "__main__":
    arbre = Arbre_binaire(4)
    arbre.inserer("r", "a", "b")
    arbre.inserer("a", "c", "d")
    arbre.inserer("b", "e", "f")
    arbre.inserer("c", "g", "h")
    arbre.inserer("d", "i", "j")
    arbre.inserer("e", "k", None)
    arbre.inserer("j", "l", None)
    print(arbre.arbre)
    parcours_prefixe = []
    parcours_infixe = []
    parcours_postfixe = []

    arbre.prefixe(0, parcours_prefixe)
    print("préfixe", parcours_prefixe)
    arbre.infixe(0, parcours_infixe)
    print("infixe", parcours_infixe)
    arbre.postfixe(0, parcours_postfixe)
    print("postfixe", parcours_postfixe)

    print("préfixe ", arbre.prefixe_2(0))
