#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Oct 29 15:31:52 2020

@auteur: Christophe Viroulaud
"""


from random import randint

tab = [0] * randint(10, 100)
for i in range(len(tab)):
    tab[i] = randint(0, 100)
print(tab)

copie = [0] * len(tab)
for i in range(len(tab)):
    copie[i] = tab[i]
print(copie)