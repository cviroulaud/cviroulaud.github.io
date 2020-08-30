#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sun Aug 30 10:34:54 2020

@auteur: Christophe Viroulaud
"""


def puissance_star(x:int,n:int)->int:
    return x**n

def puissance_builtin(x:int,n:int)->int:
    return pow(x,n)

def puissance_perso(x:int,n:int)->int:
    """
    >>> puissance_perso(2,8)
    256
    >>> puissance_perso(2,9)
    512
    """
    res = 1
    for i in range(n):
        res*=x
    return res

def puissance_recursif(x:int,n:int)->int:
    if n==0:
        return 1
    else:
        return x*puissance_recursif(x,n-1)

def puissance_recursif_rapide(x,n):
    if n==0:
        return 1
    elif n%2==0:
        return puissance_recursif_rapide(x*x,n//2)
    else:
        return x*puissance_recursif_rapide(x*x,n//2)

def puissance_iteratif_rapide(x,n):
    res=1
    while n>0:
        if n % 2 == 0:
            x = x**2
            n = n // 2
        else:
            res = res * x
            n = n -1
    return res

from time import time

debut=time()
puissance_star(2701,19406)
fin=time()
print("opérande **",fin-debut)

debut=time()
puissance_builtin(2701,19406)
fin=time()
print("fonction pow()",fin-debut)

debut=time()
puissance_perso(2701,19406)
fin=time()
print("fonction personnelle",fin-debut)

import sys
sys.setrecursionlimit(20000)

debut=time()
puissance_recursif(2701,19406)
fin=time()
print("fonction récursive",fin-debut)

debut=time()
puissance_recursif_rapide(2701,19406)
fin=time()
print("fonction récursive rapide",fin-debut)

debut=time()
puissance_iteratif_rapide(2701,19406)
fin=time()
print("fonction itérative rapide",fin-debut)