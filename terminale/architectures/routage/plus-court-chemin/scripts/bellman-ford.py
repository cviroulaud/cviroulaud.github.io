#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/27 14:41:52
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
    en dictionnaire de prédécesseurs
    chaque prédécesseur est représenté par un tuple
    (noeud, distance)
    """
    dico = {lettre(i): set() for i in range(len(matrice))}
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] > 0:
                dico[lettre(j)].add((lettre(i), matrice[i][j]))
    return dico


def bellman_ford(dico: dict, depart: str, arrivee: str) -> list:
    """
    renvoie le plus court chemin entre départ et arrivée
    NB: le dictionnaire distances contient les plus courtes distances 
    entre départ et chaque noeud
    """
    """
    initialise les distances (à départ) à l'infini
    on note les noeuds précédants qu'il faut traverser
    dans le même dictionnaire
    """
    distances = {noeud: {"precedant": " ",
                         "distance": float("inf")} for noeud in dico.keys()}
    distances[depart]["distance"] = 0
    modification = True

    """
    exécute tant qu'il y a une modification
    = amélioration qui évite de boucler inutilement
    si le tableau n'est plus modifié
    dans la version non améliorée on effectue n itérations
    n = nb de noeuds -1 (-> - départ)
    """
    while modification:
        modification = False
        """
        on regarde chaque arc (= les 2 boucles suivantes)
        https://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford#Pseudo-code
        """
        # pour chaque noeud on va regarder ses prédécesseurs
        for noeud, predecesseurs in dico.items():
            # pour chaque prédécesseur
            for prede, dist_prede in predecesseurs:
                """
                pour chaque prédécesseur on compare:
                    la distance actuelle du noeud
                    la distance du prédécesseur + la distance noeud/prédécesseur
                """
                if dist_prede+distances[prede]["distance"] < distances[noeud]["distance"]:
                    distances[noeud]["precedant"] = prede
                    distances[noeud]["distance"] = dist_prede + \
                        distances[prede]["distance"]
                    modification = True

    # reconstruction du chemin
    chemin = []
    noeud = arrivee
    while not(noeud == depart):
        chemin.append(noeud)
        noeud = distances[noeud]["precedant"]
    chemin.append(depart)
    chemin.reverse()
    return chemin

#DODO manque "une boucle" qui fait les n itérations (ou le nb max de sauts)
def bellman_ford_rec(dico: dict, depart: str, arrivee: str) -> int:
    """
    version récursive
    attention ici on remonte (car on a le dico des prédécesseurs):
    départ est le noeud de fin
    https://haltode.fr/algo/structure/graphe/plus_court_chemin/bellman_ford.html
    ressemble bcp aux algo "dynamique" (voir découpe barre)
    """
    if depart == arrivee:
        return 0

    chemin_mini = float("inf")
    for prede, dist_prede in dico[depart]:
        chemin = dist_prede + bellman_ford_rec(dico, prede, arrivee)
        if chemin < chemin_mini:
            chemin_mini = chemin
    return chemin_mini


def bellman_ford_rec_TD(dico: dict, depart: str, arrivee: str, track: dict) -> int:
    """
    version récursive Top Down
    attention ici on remonte (car on a le dico des prédécesseurs):
    départ est le noeud de fin
    """
    if track[depart] > 0:
        return track[depart]

    if depart == arrivee:
        return 0

    chemin_mini = float("inf")
    for prede, dist_prede in dico[depart]:
        chemin = dist_prede + bellman_ford_rec_TD(dico, prede, arrivee, track)
        if chemin < chemin_mini:
            chemin_mini = chemin
    track[depart] = chemin_mini
    return track[depart]


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
print(bellman_ford(dico, "A", "I"))
print(bellman_ford_rec(dico, "I", "A"))

track = {lettre(i): -1 for i in range(len(reseau))}
print(bellman_ford_rec_TD(dico, "I", "A", track))
