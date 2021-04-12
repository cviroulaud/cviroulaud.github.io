#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Nov 13 15:20:07 2020

@auteur: Christophe Viroulaud
"""


from mod_graphe import Graphe

def BFS_dico(graphe: Graphe, sommet: str)->dict:
    visites = {sommet: None}
    voisins = {sommet}
    prochains = set()
    while len(voisins) > 0:
        en_cours = voisins.pop()
        """
        get_adjacents renvoie un ensemble
        """
        for v in graphe.get_adjacents(en_cours):
            if v not in visites:
                # garde son origine
                visites[v] = en_cours
                # on l'ajoute aux prochains à visiter
                prochains.add(v)

        """
        si on a épuisé tous les voisins on prend
        les prochains
        """
        if len(voisins) == 0:
            voisins, prochains = prochains, set()

    return visites

def chemin(graphe: Graphe, depart: str, arrivee: str)->list:
    # parcours en largeur
    parcours = BFS_dico(g, "D")

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

print(BFS_dico(g, "D"))
print(chemin(g, "D", "E"))
