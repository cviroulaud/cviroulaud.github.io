#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sun Sep 20 17:05:29 2020

@auteur: Christophe Viroulaud
"""

#Question 1
def applique(f, t: tuple)->tuple:
    return tuple(f(x) for x in t)

#Question 2
def double(x: int)->int:
    return x*2

#Question 3
l = (2,4,5,8,10)
print(applique(double,l))