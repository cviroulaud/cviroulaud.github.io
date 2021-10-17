#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 17 Octobre 2021 00:44
"""
from liste import Liste, Maillon


def concatener(l1: Liste, l2: Liste) -> Liste:
    def concatener_rec(tete1: Maillon, tete2: Maillon) -> Maillon:
        """
        fonction interne pour additionner 2 listes
        """
        if tete1 is None:
            return tete2
        else:
            return Maillon(tete1.valeur, concatener_rec(tete1.suivant, tete2))

    res = Liste()
    res.tete = concatener_rec(l1.tete, l2.tete)
    return res


l1 = Liste()
l1.ajoute(8)
l1.ajoute(5)
l1.ajoute(3)
l1.ajoute(9)
l1.ajoute(10)

l2 = Liste()
l2.ajoute(4)
l2.ajoute(0)
l2.ajoute(2)

l = concatener(l1, l2)
print(l)
