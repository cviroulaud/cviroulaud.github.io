#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/13 08:47:18
"""

import csv
import matplotlib.pyplot as plt


def charger_donnees(nom_fichier: str) -> dict:
    """
    charge et formate les informations des mesures des iris

    Args:
        nom_fichier (str): nom du fichier de données

    Returns:
        dict: dictionnaire (nom: liste des mesures) 
                stockant les mesures de chaque variété
    """
    fichier = open(nom_fichier)
    data_iris = csv.DictReader(fichier, delimiter=",")
    dico_varietes = {"setosa": [], "versicolor": [], "virginica": []}
    for iris in data_iris:
        dico_varietes[iris["species"]].append(
            (float(iris["petal_length"]), float(iris["petal_width"])))
    fichier.close()
    return dico_varietes

def creer_coord(variete: list) -> list:
    """
    renvoie un tuple de deux tableaux:
        x: abscisses
        y: ordonnées
    """
    x, y = [], []
    for fleur in variete:
        x.append(fleur[0])
        y.append(fleur[1])
    return (x, y)


def distance(connu: tuple, inconnu: tuple) -> float:
    """
    calcule (le carré de) la distance euclidienne
    entre les fleurs connue et inconnue
    """
    return (connu[0]-inconnu[0])**2+(connu[1]-inconnu[1])**2


def calculer_distances(donnees: dict, inconnu: tuple) -> list:
    """
    calcule les distances entre 'inconnu' et 
    tous les autres points

    Args:
        donnees (dict): dictionnaire des iris
        inconnu (tuple): mesures de l'iris inconnu

    Returns:
        list: tableau ordonné de tuples (variété, distance)
    """
    distances = []
    for nom, mesures in donnees.items():
        for iris in mesures:
            d = distance(iris, inconnu)
            distances.append((nom, d))
    # trie les iris en fonction de la distance
    distances.sort(key=lambda fleur: fleur[1])
    return distances


def trouver_variete(k: int, distances: list) -> str:
    """
    détermine la variété en fonction des k voisins

    Args:
        k (int): nombre de voisins regardés
        distances (list): distances ordonées entre la cible et les iris

    Returns:
        str: variété sélectionnée
    """
    compteur_voisins = {}
    for i in range(k):
        nom = distances[i][0]
        if nom in compteur_voisins:
            compteur_voisins[nom] += 1
        else:
            compteur_voisins[nom] = 1

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

# crée un nuage de point pour chaque variété
info_graphe = {"setosa": ("b", "x"), "versicolor": ("r", "o"), "virginica": ("g", "+")}

for nom, mesures in varietes.items():
    x, y = creer_coord(mesures)
    plt.scatter(
        x, y, label=nom, color=info_graphe[nom][0], marker=info_graphe[nom][1])
plt.scatter(cible[0], cible[1], color="k", marker="X")
plt.xlabel("Longueur des pétales")
plt.ylabel("Largeur des pétales")
plt.legend()
plt.show()
