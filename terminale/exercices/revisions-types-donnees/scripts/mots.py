#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 17 Octobre 2021 14:51
"""

tab = ["qui", "que", "quoi", "dont", "où", "comment"]

i1 = int(input("indice 1: "))
i2 = int(input("indice 2: "))

temp = tab[i1]
tab[i1] = tab[i2]
tab[i2] = temp

print(tab)