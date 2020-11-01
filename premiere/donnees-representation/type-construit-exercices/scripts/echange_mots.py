#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Oct 29 15:06:05 2020

@auteur: Christophe Viroulaud
"""


mots = ["chien","vache","chat","oiseau","crayon","plume","téléphone","lit"]
# split coupe la chaîne de caractère chaque fois qu'elle rencontre un espace
# map applique la fonction int à chaque sous-chaîne
i, j = map(int, input("Entrez deux indices séparés par un espace: ").split(" "))
mots[i], mots[j] = mots[j], mots[i]
print(mots)