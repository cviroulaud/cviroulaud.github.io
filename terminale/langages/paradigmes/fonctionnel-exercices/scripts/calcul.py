#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Sep 21 10:25:07 2020

@auteur: Christophe Viroulaud
"""

#Question 1
def calcul(operation, l: tuple)->int:
    res = l[0]
    for i in range(1, len(l)):
        res = operation(res, l[i])
    return res

#Question 2
addition = lambda x,y: x+y

#Question 3
l = (2,3,6,8,1,9)
print(calcul(addition, l))

#Question 4
print(calcul(lambda x,y: x-y, l))
print(calcul(lambda x,y: max(x,y), l))