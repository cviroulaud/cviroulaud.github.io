#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Oct 20 18:04:50 2020

@auteur: Christophe Viroulaud
"""

"""
Donne la représentation IEE 754 sur 32 bits d'un nombre réel
Le nombre devra être compris entre -10^-38 et 10^38
"""
entier,fraction = map(str, input("Entrez un nombre réel: ").split("."))
entier = int(entier)
nb_chiffres = len(fraction)
fraction = int(fraction)

"""
Conversion de la partie entière
"""
#variable pour ne pas dépasser 32 bits
nb_bits = 0

entier_bin = ""
while entier > 0:
    entier_bin = str(entier%2) + entier_bin
    entier = entier//2
    nb_bits = nb_bits + 1


"""
Conversion de la partie fractionnaire
"""
fraction_bin = ""
while fraction > 0 and nb_bits < 33:
    fraction = fraction*2
    fraction_bin = fraction_bin + str(fraction//10**nb_chiffres)
    if fraction >= 10**nb_chiffres:
        fraction = fraction - 10**nb_chiffres
    nb_bits = nb_bits + 1

"""
Détermination de la mantisse et de l'exposant
"""


print(entier_bin, fraction_bin)