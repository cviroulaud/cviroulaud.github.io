#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/29 10:40:26
"""

from collections import deque


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


def dijkstra(dico: dict, depart: str, arrivee: str) -> list:
    """
    renvoie le plus court chemin entre départ et arrivée
    NB: le dictionnaire distances contient les plus courtes distances 
    entre départ et chaque noeud
    """
    distances = {noeud: {"precedant": "",
                         "distance": float("inf")} for noeud in dico.keys()}
    visites = set()
    distances[depart]["distance"] = 0
    """
    file pour donner prochain noeud
    elle contiendra les noeuds non visités dans l'ordre de distance
    """
    f = deque()
    f.appendleft(depart)

    # tant que la file n'est pas vide
    while f:
        # récupère le noeud (non visité) avec la plus courte distance
        en_cours = f.pop()
        visites.add(en_cours)
        for voisin in dico[en_cours]:
            """
            ERREUR: on ne calcule la distance que si le voisin
            n'a pas déjà été visité (s'il a été visité sa distance
            est déjà optimale)
            if voisin[0] not in visites: devrait être avant dist_calc
            """
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
                """
                maj de la file
                on place le noeud 'voisin' au bon endroit
                dans la file (en fonction distance mini)
                """
                if voisin[0] not in visites:
                    indice = 0
                    insertion = False
                    for noeud in f:
                        if distances[noeud]["distance"] < dist_calc:
                            f.insert(indice, voisin[0])
                            insertion = True
                            break
                        indice += 1
                    # insertion en première place si pas déjà inséré
                    if not insertion:
                        f.append(voisin[0])

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
