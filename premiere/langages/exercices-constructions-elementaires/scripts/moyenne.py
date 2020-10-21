#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sat Oct 17 16:43:54 2020

@auteur: Christophe Viroulaud
"""


somme = 0
for i in range(10):
    """
    Il faut noter ici l'ordre dans lequel l'interprète
    lit cette ligne:
        - il lit la valeur du input
        - il la convertit en entier
        - il additionne cette valeur à somme
    """
    somme += int(input("note: "))
"""
la fonction round() permet d'arrondir
ici à 2 chiffres après la virgule
"""
moyenne = round(somme/2, 2)
if moyenne >= 15:
    print("{}/20, félicitations!".format(moyenne))
elif moyenne >= 10:
    # il est inutile ici de vérifier si moyenne < 15
    print("{}/20, bon travail!".format(moyenne))
else:
    print("{}/20, doit fournir des efforts!".format(moyenne))