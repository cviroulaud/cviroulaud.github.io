#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov 23 16:40:19 2020

@auteur: Christophe Viroulaud
"""


mot = input("mot: ")
voyelles = ["a","e","i","o","u","y"]
nb_voyelles = 0
for c in mot:
    if c in voyelles:
        nb_voyelles += 1
print(nb_voyelles)