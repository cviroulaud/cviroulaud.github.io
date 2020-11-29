#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov 23 16:24:32 2020

@auteur: Christophe Viroulaud
"""


somme = 0
# attention la dernière valeur n'est pas dans l'intervalle
for i in range(1,101):
    somme += i
print(somme)

somme_impair = 0
# le 3° argument est le pas
for i in range(1, 100, 2):
    somme_impair += i
print(somme_impair)