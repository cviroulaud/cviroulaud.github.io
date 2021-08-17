#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov 23 17:03:15 2020

@auteur: Christophe Viroulaud
"""


from random import randint

# définit aléatoirement la position de la bombe
bombe_x = randint(0, 100)
bombe_y = randint(0, 100)
x = int(input("x: "))
y = int(input("y: "))
distance_carree = (bombe_x - x)**2 + (bombe_y - y)**2
# inutile (et risqué) de calculer la racine carrée
while distance_carree > 10**2:
    x = int(input("x: "))
    y = int(input("y: "))
    # redéfinit la distance
    distance_carree = (bombe_x - x)**2 + (bombe_y - y)**2

print("Bravo!")