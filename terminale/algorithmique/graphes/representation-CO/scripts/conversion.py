#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mercredi 26 Janvier 2022 23:27
"""


def mat_to_dic(mat: list) -> dict:
    dico = {}
    for i in range(len(mat)):  # chaque ligne
        # nom du noeud
        noeud = chr(65+i)
        dico[noeud] = []
        for j in range(len(mat[i])):  # chaque colonne
            if mat[i][j] == 1:
                # noeud adjacent
                adj = chr(65+j)
                dico[noeud].append(adj)
    return dico


def dic_to_mat(dic: dict) -> list:
    # taille de la matrice connue
    mat = [[0 for _ in range(len(dic))] for _ in range(len(dic))]
    for noeud, adjacents in dic.items():
        # indice de la ligne
        ind_noeud = ord(noeud)-65

        for adj in adjacents:
            # indice de la colonne
            ind_adj = ord(adj)-65
            mat[ind_noeud][ind_adj] = 1
    return mat


mat = [[0, 1, 1, 0, 0, 1],
       [1, 0, 0, 0, 0, 0],
       [1, 0, 0, 1, 1, 0],
       [0, 0, 1, 0, 0, 1],
       [0, 0, 1, 0, 0, 0],
       [1, 0, 0, 1, 0, 0]]

dico = mat_to_dic(mat)
print(dico)
print(dic_to_mat(dico))
