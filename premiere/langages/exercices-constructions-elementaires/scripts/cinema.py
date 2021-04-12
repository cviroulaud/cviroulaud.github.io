#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sun Oct 18 11:50:04 2020

@auteur: Christophe Viroulaud
"""


age = int(input("Quel est votre âge? "))
if age < 16:
    print("Le prix de la carte est 10€.")
elif age <= 25:
    """
    inutile de vérifier si age >= 16, c'est
    forcément le cas ici.
    """
    print("Le prix de la carte est 15€.")
elif age <= 59:
    print("Le prix de la carte est 25€.")
else:
    print("Le prix de la carte est 15€.")