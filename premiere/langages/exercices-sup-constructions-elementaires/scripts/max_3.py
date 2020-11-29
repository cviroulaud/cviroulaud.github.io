#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Nov 23 16:16:33 2020

@auteur: Christophe Viroulaud
"""


x = int(input("nombre 1: "))
y = int(input("nombre 2: "))
z = int(input("nombre 3: "))
mini = x
if y > mini:
    mini = y
if z > mini:
    mini = z
print(mini)