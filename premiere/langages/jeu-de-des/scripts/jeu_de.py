#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/08/17 01:40:29
"""

de1 = 3
proposition = 0
compteur = 0
while de1 != proposition:
    compteur = compteur + 1
    proposition = int(input("Choisir: "))
print(compteur)