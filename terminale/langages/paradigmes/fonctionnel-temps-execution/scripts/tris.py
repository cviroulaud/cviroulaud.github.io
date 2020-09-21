#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sun Sep 20 15:44:50 2020

@auteur: Christophe Viroulaud
"""


def tri_selection(tab):
    taille = len(tab)
    for i in range(taille):
        rang_mini = i
        for j in range (i+1,taille):
            if tab[j] < tab[rang_mini]:
                rang_mini = j
        tab[i],tab[rang_mini] = tab[rang_mini],tab[i]
    return tab

def tri_bulles(tab):
    taille = len(tab)
    for passage in range(taille):
        for j in range(1,taille - passage):
            if tab[j] < tab[j-1]:
                tab[j],tab[j-1] = tab[j-1],tab[j]
    return tab

def tri_bulles_optimise(tab):
    taille = len(tab)
    permutation = True
    passage = 0
    while permutation == True:
        permutation = False
        for j in range(1, taille - passage):
            if tab[j] < tab[j-1]:
                permutation = True
                tab[j],tab[j-1] = tab[j-1],tab[j]
        passage = passage + 1
    return tab

def tri_insertion(tab):
    taille = len(tab)
    for i in range(1,taille):
        en_cours = tab[i]
        j = i-1
        while j >= 0 and tab[j] > en_cours:
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = en_cours
    return tab