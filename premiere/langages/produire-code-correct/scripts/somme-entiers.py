#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Jan  4 16:52:15 2021

@auteur: Christophe Viroulaud
"""


def somme_des_entiers(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

print(somme_des_entiers(-2))