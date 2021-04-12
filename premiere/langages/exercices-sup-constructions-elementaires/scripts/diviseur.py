#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov 23 16:35:23 2020

@auteur: Christophe Viroulaud
"""


nb = int(input("nombre: "))
diviseur = 1
while diviseur < nb:
    # si le reste est nul c'est un diviseur
    if nb%diviseur == 0:
        print(diviseur)
    # passe au diviseur suivant
    diviseur += 1