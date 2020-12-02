#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov 30 11:28:59 2020

@auteur: Christophe Viroulaud
"""


lignes = int(input("Nombre de lignes: "))
# il y a 2n-1 caractères par ligne
colonnes = 2*lignes - 1
for nb_espaces in range(lignes,-1,-1):
    nb_etoiles = colonnes - 2*nb_espaces
    print(nb_espaces*" " + nb_etoiles*"*" + nb_espaces*" ")