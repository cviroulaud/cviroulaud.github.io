#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov 23 16:55:58 2020

@auteur: Christophe Viroulaud
"""


# Cette méthode fonctionne mais peut s'avérer très lente.
nb = int(input("nombre: "))
diviseur = 2
# si le reste est nul, c'est que nous avons un diviseur
while diviseur < nb and not(nb%diviseur == 0):
    diviseur += 1
# On a divisé par tous les nombres < nb
if diviseur == nb:
    print(f"{nb} est premier.")
else: # on s'est arrêté avant
    print(f"{nb} n'est pas premier.")