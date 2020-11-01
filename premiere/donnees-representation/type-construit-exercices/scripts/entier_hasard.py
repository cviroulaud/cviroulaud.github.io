#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Oct 28 20:54:45 2020

@auteur: Christophe Viroulaud
"""


from random import randint

tab = []
for i in range(20):
    tab.append(randint(0, 100))

print(tab)

# seconde possibilité
tab2 = [0] * 20
for i in range(20):
    tab2[i] = randint(0, 100)

print(tab2)