#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/03 15:55:38
"""

import matplotlib.pyplot as plt

def fibo(n: int, indice: int)->int:
    """
    calcule le terme de rang n
    de la suite de Fibonacci
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        compteur[i] += 1
        return fibo(n-1, i) + fibo(n-2, i)


compteur = [0 for _ in range(25)]
for i in range(25):
    fibo(i,i)

plt.plot(compteur)
plt.title("nombre d'appels")

plt.grid()
plt.show()