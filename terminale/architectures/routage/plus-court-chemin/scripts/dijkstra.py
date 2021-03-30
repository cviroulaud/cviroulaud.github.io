#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/29 10:40:26
"""

def lettre(i: int) -> str:
    """
    retourne la lettre correspondant
    à l'indice
    """
    return chr(65+i)


def mat_to_dict(matrice: list) -> dict:
    """
    transforme la matrice
    en dictionnaire de successeurs
    chaque successeur est représenté par un tuple
    (noeud, distance)
    """
    dico = {lettre(i): set() for i in range(len(matrice))}
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] > 0:
                dico[lettre(i)].add((lettre(j), matrice[i][j]))
    return dico

def get_mini(distances: dict, visites: set)->str:
    """
    renvoie le noeud non encore visité
    avec la distance la plus petite
    
    cette fonction joue un rôle central dans la complexité de l'algo
    """
    mini = float("inf")
    noeud_mini = ""
    for noeud, info in distances.items():
        if noeud not in visites:
            if info["distance"] < mini:
                mini = info["distance"]
                noeud_mini = noeud
    return noeud_mini

def dijkstra(dico: dict, depart: str, arrivee: str)->list:
    """
    renvoie le plus court chemin entre départ et arrivée
    NB: le dictionnaire distances contient les plus courtes distances 
    entre départ et chaque noeud
    """
    distances = {noeud: {"precedant": "", 
                         "distance": float("inf")} for noeud in dico.keys()}
    visites = set()
    distances[depart]["distance"] = 0
    
    # tant qu'on n'a pas visité tous les noeuds
    while len(visites) < len(dico.keys()):
        # récupère le noeud (non visité) avec la plus courte distance
        en_cours = get_mini(distances, visites)
        visites.add(en_cours)
        for voisin in dico[en_cours]:
            """
            La distance calculée pour atteindre voisin est:
                la distance du noeud en cours
                + l'arc entre ce noeud et le voisin
            """
            dist_calc = distances[en_cours]["distance"] + voisin[1]
            # si cette distance est plus petite que celle actuellement en mémoire
            if dist_calc < distances[voisin[0]]["distance"]:
                distances[voisin[0]]["distance"] = dist_calc
                distances[voisin[0]]["precedant"] = en_cours
    
    # reconstruction du chemin
    chemin = []
    noeud = arrivee
    while not(noeud == depart):
        chemin.append(noeud)
        noeud = distances[noeud]["precedant"]
    chemin.append(depart)
    chemin.reverse()
    return chemin
                
    
# http://graphonline.ru/fr/?graph=tVEgQyZcJcCaUBCy
reseau = [[0, 6, 10, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 11, 14, 0, 0, 0, 0, 0],
          [0, 12, 0, 12, 0, 0, 8, 16, 0, 0],
          [0, 0, 0, 0, 0, 6, 3, 0, 0, 0],
          [0, 0, 0, 0, 0, 4, 0, 0, 6, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 12, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 16, 6],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
          ]

dico = mat_to_dict(reseau)
print(dico)
print(dijkstra(dico, "A", "I"))