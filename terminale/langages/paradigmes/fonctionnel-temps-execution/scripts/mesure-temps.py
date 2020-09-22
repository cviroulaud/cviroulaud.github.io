#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Sep  7 17:48:28 2020

@auteur: Christophe Viroulaud
"""


from random import randint
from time import time
import matplotlib.pyplot as plt

def duree_tri(fonction, tab: list)->tuple:
    deb = time()
    tab = fonction(tab)
    fin = time()
    return (fonction.__name__, fin-deb)

def duree_tri_fonctionnel(fonction, tab: tuple)->tuple:
    deb = time()
    tab = fonction(list(tab))
    fin = time()
    return (fonction.__name__, fin-deb, tuple(tab))

def tri_selection(tab):
    taille = len(tab)
    for i in range(taille):
        rang_mini = i
        for j in range (i+1,taille):
            if tab[j] < tab[rang_mini]:
                rang_mini = j
        tab[i],tab[rang_mini] = tab[rang_mini],tab[i]
    return tab

l = [randint(0,100) for _ in range(10000)]
print(duree_tri(tri_selection, l.copy()))

l1 = tuple(randint(0,100) for _ in range(10))
print(l1)

#représentation graphique
def evolution_duree(fonction):
    nb_elements=[10,100,250,500,750,1000,1500,2000,3000,4000,5000] #[10**i for i in range(1,5)]
    temps = []
    for nb in nb_elements:
        tab = [randint(0,100) for _ in range(nb)]
        temps.append(duree_tri(fonction,tab)[1])

    plt.plot(nb_elements,temps)
    plt.title(fonction.__name__)

    plt.grid()
    plt.show()

evolution_duree(tri_selection)