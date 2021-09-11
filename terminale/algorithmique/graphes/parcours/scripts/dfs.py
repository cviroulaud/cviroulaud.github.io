#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/09/09 13:51:49
"""


BLANC = 0
GRIS = 1
NOIR = 2


class Noeud:
    def __init__(self):
        self.couleur = BLANC
        self.dist = float("inf")
        self.pred = None


# non orienté
mat = [[0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0]]

# orienté
mat_o = [[0, 6, 10, 0, 0, 0, 0, 0, 0, 0],
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


def dfs(m: list, dep: int):
    suivi = []
    for i in range(len(mat)):
        suivi.append(Noeud())
    suivi[dep].dist = 0

    p = []
    p.append(dep)
    while p:
        en_cours = p.pop()
        print(en_cours, end=" ")
        for i in range(len(mat[en_cours])):
            if mat[en_cours][i] == 1:
                if suivi[i].couleur == BLANC:
                    suivi[i].couleur = GRIS
                    suivi[i].dist = suivi[en_cours].dist+1
                    suivi[i].pred = en_cours
                    p.append(i)
        suivi[en_cours].couleur = NOIR


def dfs_rec(m: list, dep: int, suivi: list):
    suivi[dep].couleur = GRIS
    print(dep,end=" ")
    for i in range(len(mat[dep])):
        if mat[dep][i] == 1:
            if suivi[i].couleur == BLANC:
                dfs_rec(m, i, suivi)
    suivi[dep].couleur = NOIR


dfs(mat, 0)
print()
suivi = []
for i in range(len(mat)):
    suivi.append(Noeud())
dfs_rec(mat,0,suivi)