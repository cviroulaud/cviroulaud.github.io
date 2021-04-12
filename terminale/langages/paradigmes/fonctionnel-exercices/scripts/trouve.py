#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sun Sep 20 16:27:50 2020

@auteur: Christophe Viroulaud
"""

#Question 1
def trouve(p,t: tuple)->object:
    for x in t:
        if p(x):
            return x
    return None

#Question 2
def est_positif(x: int)->bool:
    if x > 0:
        return True
    return False

#Question 3
l = (-6,-5,12,4,8)
print(trouve(est_positif, l))

#Question 4
from math import sqrt

def est_premier(n: int)->bool:
    if n ==1:
        return False
    if n == 2:
        return True
    if n%2 == 0: #nombre pair; solution avec bitwise operator: n & 1 == 0
        return False

    k = 3
    racine = int(sqrt(n)) #renvoie racine entière (int)
    while k <= racine:
        if n % k == 0:
            return False
        k += 2
    return True

#Question 5
l1 = (4, 8, 22, 35, 47, 87)
print(trouve(est_premier, l1))