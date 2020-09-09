#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Aug 21 10:10:53 2020

@auteur: Christophe Viroulaud
"""


class Loto:

    def __init__(self, num: list, c: int):
        self.numeros = num
        self.complementaire = c

    def __contains__(self, n):
        # implémente l'opérateur in pour cet objet
        return n in self.numeros

    def __str__(self):
        #e st appelé quand on veut afficher l'objet
        return str(self.complementaire)

tirage = Loto([31,32,53,17,45,36],7)
print(tirage) # __str__ est appelée
print(5 in tirage) # __contains__ a redéfini in