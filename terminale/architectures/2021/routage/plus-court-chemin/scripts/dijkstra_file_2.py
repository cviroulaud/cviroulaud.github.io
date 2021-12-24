#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/09/05 20:27:34
"""


from file_priorite import File_priorite
import tkinter as tk


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

    dico contient des ensembles de tuples (voisin, distance (arête))
    la file contient des tuples (noeud, distance calculée (de 'distances'))
    """
    distances = {noeud: {"precedant": "",
                         "distance": float("inf")} for noeud in dico.keys()}
    visites = set()
    distances[depart]["distance"] = 0

    f = File_priorite()
    f.enfiler((depart, 0))
    # visites.add(depart)

    # tant que la file n'est pas vide
    while not f.est_vide():
        # récupère le tuple (nom, distance calculée) de 'distances' avec la plus courte distance
        en_cours = f.defiler()
        visites.add(en_cours[0])
        for voisin in dico[en_cours[0]]:
            """
            ATTENTION: ne pas mettre 'visites' --> FAUX (vérifié avec dico2 dans dijkstra_file_3)
            """
            if voisin[0] not in visites:
                # maj distance
                dist_calc = distances[en_cours[0]]["distance"] + voisin[1]
                # si cette distance est plus petite que celle actuellement en mémoire
                if dist_calc < distances[voisin[0]]["distance"]:
                    distances[voisin[0]]["distance"] = dist_calc
                    distances[voisin[0]]["precedant"] = en_cours[0]
                # maj file de priorité
                f.enfiler((voisin[0], distances[voisin[0]]["distance"]))

    print(distances)
    # reconstruction du chemin
    chemin = []
    noeud = arrivee
    while not(noeud == depart):
        chemin.append(noeud)
        noeud = distances[noeud]["precedant"]
    chemin.append(depart)
    chemin.reverse()
    return chemin


def dijkstra2(dico: dict, depart: str, arrivee: str) -> list:
    """
    version sans 'visites': le calcul de la distance 'filtre' automatiquement
    """
    distances = {noeud: {"precedant": "",
                         "distance": float("inf")} for noeud in dico.keys()}
    distances[depart]["distance"] = 0

    f = File_priorite()
    f.enfiler((depart, 0))
    
    # tant que la file n'est pas vide
    while not f.est_vide():
        # récupère le tuple (nom, distance calculée) de 'distances' avec la plus courte distance
        en_cours = f.defiler()
        # visites.add(en_cours[0])
        print(en_cours)
        for voisin in dico[en_cours[0]]:
            # maj distance
            dist_calc = distances[en_cours[0]]["distance"] + voisin[1]
            # si cette distance est plus petite que celle actuellement en mémoire
            if dist_calc < distances[voisin[0]]["distance"]:
                distances[voisin[0]]["distance"] = dist_calc
                distances[voisin[0]]["precedant"] = en_cours[0]
                # maj file de priorité
                # doit être dans le if (cf v1)
                f.enfiler((voisin[0], distances[voisin[0]]["distance"]))

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
chemin = dijkstra(dico, "A", "J")
print(chemin)
print("v2")
dijkstra2(dico, "A", "J")

fenetre = tk.Tk()
canevas = tk.Canvas(fenetre, width=400, height=400)
canevas.pack()

# place les noeuds
pos_lettre = {}
pos_lettre["A"] = (50, 50)
pos_lettre["B"] = (150, 50)
pos_lettre["E"] = (250, 50)
pos_lettre["C"] = (50, 150)
pos_lettre["D"] = (150, 150)
pos_lettre["F"] = (250, 150)
pos_lettre["I"] = (350, 150)
pos_lettre["G"] = (150, 250)
pos_lettre["H"] = (50, 350)
pos_lettre["J"] = (150, 350)

for i in range(10):
    canevas.create_text(pos_lettre[chr(65+i)][0],
                        pos_lettre[chr(65+i)][1],
                        text=chr(65+i))

# trace les arêtes
for depart, voisins in dico.items():
    for v in voisins:
        canevas.create_line(pos_lettre[depart][0],
                            pos_lettre[depart][1],
                            pos_lettre[v[0]][0],
                            pos_lettre[v[0]][1])

# trace plus court chemin
for i in range(len(chemin)-1):
    canevas.create_line(pos_lettre[chemin[i]][0],
                        pos_lettre[chemin[i]][1],
                        pos_lettre[chemin[i+1]][0],
                        pos_lettre[chemin[i+1]][1],
                        fill="#FF0000",
                        width=3)
fenetre.mainloop()
