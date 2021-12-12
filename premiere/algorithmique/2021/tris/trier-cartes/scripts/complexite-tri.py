#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/11 22:52:36
"""

from random import randint
import matplotlib.pyplot as plt

def tri_selection(tab: list)->int:
    """
    renvoie nb d'itérations
    """
    nb = 0
    for i in range(len(tab)):
        i_mini = i
        for j in range(i+1, len(tab)):
            nb += 1
            if tab[j] < tab[i_mini]:
                i_mini = j
        tab[i], tab[i_mini] = tab[i_mini], tab[i]
    return nb

pas = [0, 10, 100, 500, 1000, 2000, 3000, 5000, 7000, 8500, 10000, 15000]
iterations = []
for nb in pas:
    tab = [randint(0, 1000) for i in range(nb)]
    iterations.append(tri_selection(tab))

figure = plt.figure()
axes = figure.add_subplot(111)
axes.set_xlabel("nombre d'éléments")
axes.set_ylabel("nombre d'itérations")
plt.ticklabel_format(style='plain', axis='y')
plt.plot(pas, iterations)
plt.show()