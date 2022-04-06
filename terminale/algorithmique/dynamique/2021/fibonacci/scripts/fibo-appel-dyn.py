#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/03 15:55:38
"""

import matplotlib.pyplot as plt

def fibo(n: int, track: list, i: int)->int:
    """
    calcule le terme de rang n
    de la suite de Fibonacci
    """
    if track[n] > 0:
        return track[n]
    if n == 0:
        track[0] = 0 
        return track[0]
    elif n == 1:
        track[1] = 1
        return track[1]
    else:
        compteur[i] += 1
        track[n] = fibo(n-1, track, i) + fibo(n-2, track, i)
        return track[n]


compteur = [0 for _ in range(25)]
for i in range(25):
    track = [-1 for _ in range(i+1)]
    fibo(i, track, i)

plt.plot(compteur)
plt.title("nombre d'appels")

plt.grid()
plt.show()