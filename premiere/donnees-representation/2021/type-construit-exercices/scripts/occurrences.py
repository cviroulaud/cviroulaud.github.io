#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Oct 28 20:38:02 2020

@auteur: Christophe Viroulaud
"""


# on reprend le principe du tableau de l'exercice précédent
from random import randint

nombres = []
# boucle qui crée le tableau
for i in range(randint(10, 1000)):
    nombres.append(randint(0, 20))

# boucle qui compte le nombre de 10
nb_10 = 0
for nb in nombres:
    if nb == 10:
        nb_10 = nb_10 + 1

print(f"Il y a {nb_10} fois le nombre 10 dans le tableau")

# boucle qui compte le nombre d'occurrences de chaque valeur
# Il faut 21 cellules!!!
occurrences = [0] * 21
for nb in nombres:
    occurrences[nb] = occurrences[nb] + 1

print(occurrences)
