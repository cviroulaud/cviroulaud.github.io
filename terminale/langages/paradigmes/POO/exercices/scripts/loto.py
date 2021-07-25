#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Aug 21 10:10:53 2020

@auteur: Christophe Viroulaud
"""

from random import randint, seed


class Loto:

    def __init__(self, num: list, c: int):
        self.numeros = num
        self.complementaire = c

    def est_present(self, n: int) -> bool:
        """
        vérifie si n est présent dans le tirage
        (sauf le complémentaire)
        """
        return n in self.numeros

    def est_gagnant(self, mes_num: list, mon_compl: int) -> bool:
        if mon_compl != self.complementaire:
            return False
        i = 0
        while i < 6 and self.est_present(mes_num[i]):
            i += 1
        return i == 6

    def afficher(self) -> str:
        """
        affiche le tirage
        """
        res = ""
        for n in self.numeros:
            res += str(n)+" - "
        # supprime le dernier tiret (slice hors programme)
        res = res[:-2]
        res += "/ "+str(self.complementaire)
        return res


def creer_tirage() -> Loto:
    """
    crée un tirage avec des entiers distincts
    """
    numeros = []
    while len(numeros) < 6:
        n = randint(1, 49)
        if n not in numeros:
            numeros.append(n)

    complementaire = randint(1, 49)
    while complementaire in numeros:
        complementaire = randint(1, 49)

    return Loto(numeros, complementaire)


# Initialise (fixe ici) le générateur de nombres aléatoires.
seed(1)
tirage = creer_tirage()
print(tirage.afficher())
# gagnant
print(tirage.est_gagnant([37, 8, 9, 49, 5, 17], 32))
# perdant
print(tirage.est_gagnant([37, 12, 9, 49, 5, 17], 32))
