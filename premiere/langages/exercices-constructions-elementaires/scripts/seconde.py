#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sat Oct 17 15:27:44 2020

@auteur: Christophe Viroulaud
"""


secondes = int(input("Donnez le nombre de secondes: "))
heures = secondes // 3600
minutes = (secondes % 3600) // 60
secondes = (secondes % 3600) % 60
"""
Il faut noter que ci-dessous les variables sont des entiers
et deviennent des chaînes de caractères (string). Python
permet de changer le type d'une variable. Ce n'est pas le
cas de tous les langages.
"""
if heures < 10:
    heures = "0"+str(heures)
if minutes < 10:
    minutes = "0"+str(minutes)
if secondes < 10:
    secondes = "0"+str(secondes)
print("{}h {}min {}s".format(heures, minutes, secondes))