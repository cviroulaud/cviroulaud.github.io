#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Sep 16 15:09:33 2020

@auteur: Christophe Viroulaud
"""


def nombre_chiffres(n: int)->int:
    if n <= 9:
        return 1
    else:
        return 1 + nombre_chiffres(n//10)

print(nombre_chiffres(123))