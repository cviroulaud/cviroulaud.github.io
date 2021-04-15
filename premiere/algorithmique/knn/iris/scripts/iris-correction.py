#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/13 08:47:18
"""

import csv


def charger_donnees(nom_fichier: str) -> dict:
    fichier = open(nom_fichier)
    data_iris = csv.DictReader(fichier, delimiter=",")
    dico_varietes = {"setosa": [], "versicolor": [], "virginica": []}
    # Pour chaque ligne de données
    for iris in data_iris:
        # Stocke la longueur et la largeur sous forme de tuple de flottants
        dico_varietes[iris["species"]].append(
            (float(iris["petal_length"]), float(iris["petal_width"])))
    fichier.close()
    return dico_varietes


def distance(connu: tuple, inconnu: tuple) -> float:
    return (connu[0]-inconnu[0])**2+(connu[1]-inconnu[1])**2


def calculer_distances(donnees: dict, inconnu: tuple) -> list:
    distances = []
    for nom, mesures in donnees.items():
        for iris in mesures:
            d = distance(iris, inconnu)
            distances.append((nom, d))

    # trie les iris en fonction de la distance
    distances.sort(key=lambda fleur: fleur[1])
    return distances


def trouver_variete(k: int, distances: list) -> str:
    # compte le nombre d'occurences de chaque variété
    compteur_voisins = {}
    for i in range(k):
        nom = distances[i][0]
        if nom in compteur_voisins:
            compteur_voisins[nom] += 1
        else:
            compteur_voisins[nom] = 1

    # recherche la variété avec la plus grande valeur dans compteur_voisins
    maxi = 0
    nom_maxi = 0
    for nom, quantite in compteur_voisins.items():
        if quantite > maxi:
            maxi = quantite
            nom_maxi = nom
    return nom_maxi


"""
Programme principal
"""

k = 3
cible = (5.1, 1.55)

varietes = charger_donnees("data-iris.csv")
distances_cible = calculer_distances(varietes, cible)
variete = trouver_variete(k, distances_cible)

print("La variété est ", variete)

"""
test de 10 iris avec ajout dans les connaissances
"""
k = 3
cibles = [(1,0.5),(6,2.5),(5.1, 1.55),(2.5,0.85),(3,2),
          (6,1.2),(2.1,1),(3.2,1.5),(3.5,2.5),(4,1)]

varietes = charger_donnees("data-iris.csv")
for iris_inconnu in cibles:
    # trouve la variété
    distances_cible = calculer_distances(varietes, iris_inconnu)
    variete = trouver_variete(k, distances_cible)
    print(f"La variété de {iris_inconnu} est {variete}.")
    # ajout de cible au dictionnaire des données
    varietes[variete].append(iris_inconnu)