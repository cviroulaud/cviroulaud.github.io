#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Oct  6 18:17:31 2020

@auteur: Christophe Viroulaud
"""


import matplotlib.pyplot as plt
from random import randint
from temps_fusion import tri_fusion,duree_tri
from temps_insertion import tri_insertion

def evolution_duree(fonction,cadre):
    nb_elements=[10,100,250,500,750,1000,1500,2000,3000,3500,5000,7500,10000,13000,16000,24000]
    temps = []
    #calculs des durées
    for nb in nb_elements:
        tab = [randint(0,100) for _ in range(nb)]
        temps.append(duree_tri(fonction,tab)[1])

    #création du graphe
    p = plt.subplot(1,2,cadre)
    plt.plot(nb_elements,temps)

    #habillage
    plt.title(fonction.__name__)
    p.xaxis.set_tick_params(labelsize=16)
    p.yaxis.set_tick_params(labelsize=16)
    plt.grid()

def affichage():
    plt.figure(figsize=(20,10))
    evolution_duree(tri_insertion,1)
    evolution_duree(tri_fusion,2)
    plt.show()

affichage()