#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/13 08:47:18
"""

import csv


def charger_donnees(nom_fichier: str) -> list:
    """
    charge et formate les informations des mesures des iris

    Args:
        nom_fichier (str): nom du fichier de données

    Returns:
        list: tableau de dictionnaires des échantillons
    """
    fichier = open(nom_fichier, encoding="utf8")
    data_iris = csv.DictReader(fichier, delimiter=",")
    tab_iris = []
    # Pour chaque ligne de données
    for iris in data_iris:
        tab_iris.append(
            {"espece": iris["species"],
             "longueur": float(iris["petal_length"]),
             "largeur": float(iris["petal_width"])})

    fichier.close()
    return tab_iris


def distance(connu: dict, inconnu: dict) -> float:
    """
    calcule (le carré de) la distance euclidienne
    entre la fleur connue et la fleur inconnue

    Args:
        connu (dict): information de l'espèce connue
        inconnu (dict): information de l'espèce inconnue

    Returns:
        float: carré de la distance
    """
    return (connu["longueur"]-inconnu["longueur"])**2 + \
        (connu["largeur"]-inconnu["largeur"])**2


def calculer_distances(donnees: list, inconnu: dict) -> list:
    """
    calcule les distances entre 'inconnu' et 
    tous les autres points

    Args:
        donnees (list): tableau des iris
        inconnu (dict): iris inconnu

    Returns:
        list: tableau ordonné de tuples (variété, distance)
    """
    distances = []
    for iris in donnees:
        # mesure la distance en 'iris' et l'inconnu
        d = distance(iris, inconnu)
        # stocke la distance pour cet iris
        distances.append((iris["espece"], d))

    # trie les iris en fonction de la distance
    distances.sort(key=lambda fleur: fleur[1])
    return distances


def trouver_variete(k: int, distances: list) -> str:
    """
    détermine la variété la plus présente parmi
    les k premiers voisins dans 'distances'

    Args:
        k (int): nombre de voisins regardés
        distances (list): distances ordonées entre la cible et les iris

    Returns:
        str: variété sélectionnée
    """
    # compte le nombre d'occurences de chaque variété
    compteur_voisins = {}
    for i in range(k):
        # espèce de l'iris de rang i
        nom = distances[i][0]
        # vérifie si l'espèce a déjà été référencée
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
inconnu = {"espece": "inconnu", "longueur": 5.1, "largeur": 1.55}

varietes = charger_donnees("data-iris.csv")
distances_cible = calculer_distances(varietes, inconnu)
variete = trouver_variete(k, distances_cible)

print("La variété est", variete)
