#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/29 10:40:26
"""

from constantes import largeur, hauteur, delta
from collections import deque


def get_mini(distances: list, visites: deque) -> tuple:
    """
    renvoie le noeud non encore visité
    avec la distance la plus petite
    """
    mini = float("inf")
    noeud_mini = ""
    for y in range(hauteur):
        for x in range(largeur):
            if (x, y) not in visites:
                if distances[y][x]["distance"] < mini:
                    mini = distances[y][x]["distance"]
                    noeud_mini = (x, y)
    return noeud_mini


def dijkstra(grille: list, depart: tuple, arrivee: tuple) -> tuple:
    """
    renvoie le plus court chemin entre départ et arrivée
    NB: le dictionnaire distances contient les plus courtes distances 
    entre départ et chaque noeud

    Returns:
        tuple: (chemin optimal, ordre des visites)
    """
    distances = [[{"precedant": "",
                   "distance": float("inf")} for i in range(largeur)]
                 for j in range(hauteur)]
    # une liste chainée pour avoir l'ordre de visite (pour affichage)
    visites = deque()
    distances[depart[1]][depart[0]]["distance"] = 0

    # tant qu'on n'a pas visité tous les noeuds
    nb_noeuds = largeur*hauteur
    est_arrive = False
    while len(visites) < nb_noeuds and not est_arrive:
        # récupère le noeud (non visité) avec la plus courte distance
        en_cours = get_mini(distances, visites)
        visites.append(en_cours)

        if en_cours == arrivee:
            est_arrive = True
        else:
            # parcours N E S O
            for dir_voisin in range(len(delta)):
                # il n'y a pas de mur dans cette direction
                if not grille[en_cours[1]][en_cours[0]].direction[dir_voisin]:
                    """
                    La distance calculée pour atteindre voisin est:
                        la distance du noeud en cours + 1
                    """
                    # coord du voisin étudié
                    voisin = (en_cours[0]+delta[dir_voisin][0],
                            en_cours[1]+delta[dir_voisin][1])

                    dist_calc = distances[en_cours[1]][en_cours[0]]["distance"] + 1
                    # si cette distance est plus petite que celle actuellement en mémoire
                    if dist_calc < distances[voisin[1]][voisin[0]]["distance"]:
                        distances[voisin[1]][voisin[0]]["distance"] = dist_calc
                        distances[voisin[1]][voisin[0]]["precedant"] = en_cours

    # reconstruction du chemin
    chemin = []
    noeud = arrivee
    while not(noeud == depart):
        chemin.append(noeud)
        noeud = distances[noeud[1]][noeud[0]]["precedant"]
    chemin.append(depart)
    #chemin.reverse()
    return (chemin, visites)


def a_star(grille: list, depart: tuple, arrivee: tuple) -> tuple:
    """
    algo A*

    Returns:
        tuple: (chemin optimal, ordre des visites)
    """
    distances = [[{"precedant": "",
                   "distance": float("inf")} for i in range(largeur)]
                 for j in range(hauteur)]
    # une liste chainée pour avoir l'ordre de visite (pour affichage)
    visites = deque()
    distances[depart[1]][depart[0]]["distance"] = 0

    # tant qu'on n'a pas visité tous les noeuds
    nb_noeuds = largeur*hauteur
    est_arrive = False
    #DODO manque gestion "arrivée non atteignable"
    while len(visites) < nb_noeuds and not est_arrive:
        # récupère le noeud (non visité) avec la plus courte distance
        en_cours = get_mini(distances, visites)
        visites.append(en_cours)
        
        if en_cours == arrivee:
            est_arrive = True
        else:
            # parcours N E S O
            for dir_voisin in range(len(delta)):
                # il n'y a pas de mur dans cette direction
                if not grille[en_cours[1]][en_cours[0]].direction[dir_voisin]:
                    # coord du voisin étudié
                    voisin = (en_cours[0]+delta[dir_voisin][0],
                            en_cours[1]+delta[dir_voisin][1])

                    # distance de Manhattan du voisin
                    dist_man = abs(voisin[0]-arrivee[0])+abs(voisin[1]-arrivee[1])
                    
                    # distance de euclidienne du voisin
                    dist_eucl = (voisin[0]-arrivee[0])**2+(voisin[1]-arrivee[1])**2
                    
                    dist_calc = dist_man
                    # si cette distance est plus petite que celle actuellement en mémoire
                    if dist_calc < distances[voisin[1]][voisin[0]]["distance"]:
                        distances[voisin[1]][voisin[0]]["distance"] = dist_calc
                        distances[voisin[1]][voisin[0]]["precedant"] = en_cours
                
                

    # reconstruction du chemin
    chemin = []
    noeud = arrivee
    while not(noeud == depart):
        chemin.append(noeud)
        noeud = distances[noeud[1]][noeud[0]]["precedant"]
    chemin.append(depart)
    #chemin.reverse()
    return (chemin, visites)
