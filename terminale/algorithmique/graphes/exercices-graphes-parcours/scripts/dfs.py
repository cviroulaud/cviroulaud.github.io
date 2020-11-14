#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Nov 13 14:20:31 2020

@auteur: Christophe Viroulaud
"""


from mod_graphe import Graphe

def DFS_rec(graphe: Graphe, sommet: str, visites: list = [])->list:
    if not(sommet in visites):
        visites.append(sommet)
        for voisin in graphe.get_adjacents(sommet):
            DFS_rec(graphe, voisin, visites)
    return visites

def est_connexe(graphe: Graphe)->bool:
    sommets = graphe.get_sommets()
    return len(sommets) == len(DFS_rec(graphe, sommets[0]))

def DFS_rec_dico(graphe: Graphe, sommet: str, origine: str = None, visites: dict = {})->dict:
    if not(sommet in visites):
        visites[sommet] = origine
        for voisin in graphe.get_adjacents(sommet):
            DFS_rec_dico(graphe, voisin, sommet, visites)
    return visites

def chemin(graphe: Graphe, depart: str, arrivee: str)->list:
    # parcours en profondeur
    parcours = DFS_rec_dico(g, "D")

    # si arrivee n'est pas atteignable
    if arrivee not in parcours:
        return None

    # un chemin
    chemin = [arrivee]
    en_cours = arrivee
    while not(en_cours == depart):
        # ajouter l'origine de en_cours
        origine = parcours[en_cours]
        chemin.append(origine)
        en_cours = origine
    # le chemin a été construit à l'envers
    chemin.reverse()
    return chemin

g = Graphe()
g.ajouter_arete("G", "D")
g.ajouter_arete("D", "B")
g.ajouter_arete("D", "A")
g.ajouter_arete("D", "C")
g.ajouter_arete("A", "C")
g.ajouter_arete("B", "A")
g.ajouter_arete("B", "E")
g.ajouter_arete("F", "C")
g.ajouter_arete("C", "H")
g.ajouter_arete("E", "F")

print(DFS_rec(g, "D"))
print(est_connexe(g))
print(chemin(g, "D", "E"))
