#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Oct 28 20:38:02 2020

@auteur: Christophe Viroulaud
"""


# on reprend le tableau de l'exercice précédent
from random import randint

tab = []
# boucle qui crée le tableau
for i in range(randint(10, 100)):
    tab.append(randint(0, 1000))

# boucle qui compte le nombre d'éléments
nb = 0
