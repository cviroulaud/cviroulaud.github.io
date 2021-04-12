#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Jan 19 14:23:27 2021

@auteur: Christophe Viroulaud
"""


import csv

def election_egalite(electeurs:list, somme:int = 0)->bool:
    """
    vérifie s'il est possible d'y avoir une égalité dans les élections US
    """
    if somme == 269:
        return True
    elif somme > 269:
        return False
    else:
        for i in range(len(electeurs)):
            if election_egalite(electeurs[:i]+electeurs[i+1:], somme+electeurs[i][1]):
                return True
    return False,

def election_egalite_etats(electeurs:list, etats:list, somme:int = 0)->list:
    """
    donne une liste qu'un candidat doit gagner pour avoir une égalité parfaite
    """
    if somme == 269:
        return True, etats
    elif somme > 269:
        return False,
    else:
        for i in range(len(electeurs)):
            ajout = election_egalite_etats(electeurs[:i]+electeurs[i+1:],
                            etats+[electeurs[i][0]],
                            somme+electeurs[i][1])
            if ajout[0]:
                return True, ajout[1]
    return False,

electeurs = []

with open("grands-electeurs.csv") as f:
    for etat in csv.reader(f):
        electeurs.append([etat[0], int(etat[1])])

print(election_egalite(electeurs))

print(election_egalite_etats(electeurs, [])[1])

