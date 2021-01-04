#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Jan  1 15:44:52 2021

@auteur: Christophe Viroulaud
"""


def bissextile(annee):
    """
    vérifie si l'année est bissextile
    """
    # le and est évalué avant le or
    return annee%4 == 0 and not annee%100 == 0 or annee%400 == 0

def nb_jours(annee):
    """
    renvoie le nombre de jours dans annee
    """
    if bissextile(annee):
        return 366
    else:
        return 365

def nb_jours_mois(annee, mois):
    """
    renvoie le nombre de jours dans mois
    (en fonction de l'année)
    """
    if mois == 2: #février
        if bissextile(annee):
            return 29
        else:
            return 28
    # astuce avec la prise en compte de juillet et août
    elif mois <= 7:
        return 30 + mois%2
    else:
        return 31 - mois%2

print(nb_jours_mois(2020, 2))