#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Sunday 13 February 2022 21:11
"""


def dfs(mat: list, dep: int, vis: list) -> None:
    if not vis[dep]:
        # marque le sommet visités
        vis[dep] = True
        print(dep)
        for i in range(len(mat[dep])):
            # c'est un successeur
            if mat[dep][i] == 1:
                dfs(mat, i, vis)


def parcours(mat: list) -> None:
    visites = [False for _ in range(len(mat))]
    for i in range(len(mat)):
        # lance un parcours depuis chaque sommet
        dfs(mat, i, visites)


graphe = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

parcours(graphe)
