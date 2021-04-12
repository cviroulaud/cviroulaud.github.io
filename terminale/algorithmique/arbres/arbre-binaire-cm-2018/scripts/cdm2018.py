#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Jan 27 11:11:30 2021

@auteur: Christophe Viroulaud
"""


import json
from structures import File

f = open("cdm2018.json")
tab_cdm = json.load(f)
f.close()

def affichage_BFS(tab: list)->None:
    """
    affiche l'arbre avec un parcours en largeur
    """
    f = File()
    f.enfiler(0)
    niveau = 0
    while not f.est_vide():
        en_cours = f.defiler()
        if en_cours < len(tab):
            #crée le décalage entre les différentes phases
            if en_cours == 2**niveau-1:
                niveau += 1
                print()
            print(tab[en_cours], end=" ")
            f.enfiler(2*en_cours+1)
            f.enfiler(2*en_cours+2)


affichage_BFS(tab_cdm)