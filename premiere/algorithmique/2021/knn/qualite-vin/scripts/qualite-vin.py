#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/06/08 14:04:44
"""

import csv


def charger_donnees(f: str) -> list:
    fichier = open(f, encoding="utf8")
    data = csv.DictReader(fichier)

    vins = []
    for v in data:
        vin = {}
        for attribut, valeur in v.items():
            # qualité est le seul entier
            if attribut == "quality":
                vin[attribut] = int(valeur)
            else:
                vin[attribut] = float(valeur)
        vins.append(vin)
    return vins


def distance(connu: dict, inconnu: dict) -> float:
    """
    calcule (le carrée de) la distance euclidienne
    entre les vins connu et inconnu
    """
    dist = 0
    for attribut, valeur in connu.items():
        # inconnu n'a pas d'attribut "quality" (c'est ce qu'on veut déterminer)
        if not(attribut == "quality"):
            dist += (connu[attribut]-inconnu[attribut])**2
    return dist


def calculer_distances(vins: list, inconnu: dict) -> list:
    distances = []
    for v in vins:
        d = distance(v, inconnu)
        # stocke le tuple (qualité, distance)
        distances.append((v["quality"], d))

    # trie les vins en fonction de la distance
    distances.sort(key=lambda vin: vin[1])
    return distances


def trouver_qualite(k: int, distances: list) -> int:
    """
    détermine la qualité majoritaire parmi les k plus proches
    """
    compteur_qualites = {}
    for i in range(k):
        qualite = distances[i][0]
        if qualite in compteur_qualites:
            compteur_qualites[qualite] += 1
        else:
            compteur_qualites[qualite] = 1

    maxi = 0
    qualite_maxi = 0
    for qualite, valeur in compteur_qualites.items():
        if valeur > maxi:
            qualite_maxi = qualite
            maxi = valeur
    return qualite_maxi


k = 3
vin_inconnu = {'fixed acidity': 6.9, 'volatile acidity': 0.5, 'citric acid': 0.19,
               'residual sugar': 3.9, 'chlorides': 0.16, 'free sulfur dioxide': 31.0,
               'total sulfur dioxide': 50.0, 'density': 0.994, 'pH': 3.01,
               'sulphates': 0.61, 'alcohol': 9.3}

vins = charger_donnees("winequality-red.csv")
distances = calculer_distances(vins, vin_inconnu)
print(trouver_qualite(k, distances))
