#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sun Oct 18 17:10:59 2020

@auteur: Christophe Viroulaud
"""


n = int(input("Entrez une valeur de n: "))
u_n = 3
for _ in range(1, n+1):
    u_n = 5*u_n + 4

print(u_n)