#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Oct 29 13:28:13 2020

@auteur: Christophe Viroulaud
"""


from random import randint

tab1 = [0] * 10
tab2 = [0] * 10
"""
Construire un tableau avec une taille déjà fixée
est une meilleure pratique que de le rallonger
"""
for i in range(10):
    tab1[i] = randint(0,100)
    tab2[i] = randint(0,100)

# avec extend
tab = tab1.copy()
tab.extend(tab2)
print(tab)

# à la main
tab_bis = [0] * (len(tab1) + len(tab2))
for i in range(len(tab1)):
    tab_bis[i] = tab1[i]

for i in range(len(tab2)):
    # attention au décalage
    tab_bis[i + len(tab1)] = tab2[i]

print(tab_bis)