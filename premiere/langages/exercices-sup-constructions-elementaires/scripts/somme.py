#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov 23 16:24:32 2020

@auteur: Christophe Viroulaud
"""


somme = 0
for i in range(1,101): # la dernière valeur n'est pas dans l'intervalle
    somme += i
print(somme)

somme_impair = 0
for i in range(1, 100, 2): # le 3° argument est le pas
    somme_impair += i
print(somme_impair)