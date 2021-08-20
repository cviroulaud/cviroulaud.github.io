#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sun Oct 18 11:50:04 2020

@auteur: Christophe Viroulaud
"""


"""
input renvoie une chaîne de caractère (string)
Il faut la convertir en entier (int)
"""
age = int(input("Quel est votre âge? "))
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")