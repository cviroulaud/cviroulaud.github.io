#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Oct 29 15:49:01 2020

@auteur: Christophe Viroulaud
"""


from random import randint

tab = [0] * 10
for i in range(len(tab)):
    tab[i] = randint(0, 20)

somme = 0
for i in range(len(tab)):
    somme = somme + tab[i]
print("La somme est {}.".format(somme))

moyenne = somme / len(tab)
print("La moyenne est {}.".format(moyenne))