#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/13 08:47:18
"""

import csv


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
    # Pour chaque ligne de données
    for iris in data_iris:
        # Stocke la longueur et la largeur sous forme de tuple de flottants
        dico_varietes[iris["species"]].append((................, ..............))
    fichier.close()
    return dico_varietes


def distance(connu: tuple, inconnu: tuple) -> float:
    """
    calcule (le carré de) la distance euclidienne
    entre les fleurs connue et inconnue
    """
    return .........................


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
            # calcule la distance entre l'iris et l'inconnu
            d = ......................
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
    # compte le nombre d'occurences de chaque variété
    compteur_voisins = {}
    for i in range(k):
        nom = distances[i][0]
        # si le nom est déjà référencé dans compteur_voisins
        if nom in ....................:
            compteur_voisins[nom] ..........
        else:
            ...................

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
