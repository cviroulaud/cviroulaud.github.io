#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/03 15:55:38
"""

def fibo(n: int)->int:
    """
    calcule le terme de rang n
    de la suite de Fibonacci
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
compteur = 0
def fibo_compteur(n: int)->int:
    """
    calcule le terme de rang n
    de la suite de Fibonacci
    """
    global compteur    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        compteur += 1
        return fibo_compteur(n-1) + fibo_compteur(n-2)


print(fibo_compteur(16))
print(compteur)