#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov 23 16:12:45 2020

@auteur: Christophe Viroulaud
"""


entier = int(input("nombre: "))
nb_div = 0
while entier%2 == 0:
    entier = entier//2  # ou directement entier //= 2
    nb_div += 1
print(nb_div)