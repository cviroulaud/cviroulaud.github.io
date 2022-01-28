#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Apr  2 00:16:06 2020

@auteur: Christophe Viroulaud
"""
import numpy as np
correction=np.array([[0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
               [0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,0,0,0],
               [1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0],
               [0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
               [1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
               [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0],
               [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
               [0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
               [0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1],
               [1,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1],
               [0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
               [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0],
               [0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,0]])

correction_graphe={
    7:{17,19,45},
    10:{18,21,43},
    12:{26,32},
    14:{25,30,32,34,49},
    17:{7,30,34,45},
    18:{10,19,34},
    19:{7,18,43,45},
    21:{10,43},
    25:{14,45,49,75},
    26:{12,71},
    30:{14,17,34,49},
    32:{12,14,49},
    34:{14,17,18,30},
    43:{10,19,21,45,75},
    45:{7,17,19,25,43,75},
    49:{14,25,30,32,65},
    65:{49,70,71,75},
    70:{65,71,75},
    71:{26,65,70},
    75:{25,43,45,65,70}}

def verifier(graphe):
    """
    Vérifie la matrice ou le dictionnaire d'adjacence
    et affiche les coordonnées de l'erreur ou le message 'pas d'erreur'

    Parameters
    ----------
    graphe : list ou dict
        matrice d'adjacence ou dictionnaire d'adjacence

    Returns
    -------
    None

    """
    if type(graphe) == list: # matrice d'adjacence
        print(verifier_mat(graphe))
    else: # dictionnaire d'adjacence
        print(verifier_dic(graphe))

def verifier_mat(matrice,matrice_correcte=correction):
    """
    Parameters
    ----------
    matrice : tableau de tableau

    Returns
    -------
    les coordonnées de l'erreur ou le message 'pas d'erreur'

    """
    i=0
    lignes=len(matrice_correcte[0])
    colonnes=len(matrice_correcte)
    while i < lignes:
        j=0
        while j < colonnes:
            if matrice[i][j]==matrice_correcte[i][j]:
                j+=1
            else:
                return "Erreur ligne "+str(i)+" colonne "+str(j)
        i+=1
    return "Pas d'erreur"

def verifier_dic(graphe,graphe_correct=correction_graphe):
    """
    Parameters
    ----------
    graphe : dictionnaire de Graphe

    Returns
    -------
    le noeud de l'erreur ou le message 'pas d'erreur'

    """
    for noeud,voisins in graphe.items():
        if not(graphe_correct[noeud]==set(voisins)):
            return "Erreur pour le noeud "+str(noeud)

    return "Pas d'erreur"