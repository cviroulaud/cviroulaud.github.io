#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/09/08 10:47:14
"""

import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


def affichage(mat: list):
    g = nx.Graph()
    for i in range(len(mat)):
        g.add_node(i)

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 1:
                g.add_edge(i, j)

    nx.draw(g, with_labels=True)
    plt.savefig("Graph.png", format="PNG")


def bfs(mat: list) -> list:
    """
    plutôt celui ci
    équivalent à blanc gris dans bfs.py
    """
    f = deque()
    f.appendleft(0)
    pred = [-1]*len(mat)
    visites = set()
    visites.add(0)
    while f:
        n = f.pop()
        print(n,end=" ")
        for i in range(len(mat[n])):
            if mat[n][i] == 1:
                if i not in visites:
                    f.appendleft(i)
                    visites.add(i)
                    pred[i] = n
    return pred

def bfs2(mat: list) -> list:
    f = deque()
    f.appendleft(0)
    pred = [-1]*len(mat)
    visites = set()
    #visites.add(0)
    while f:
        n = f.pop()
        visites.add(n)
        print(n,end=" ")
        for i in range(len(mat[n])):
            if mat[n][i] == 1:
                if i not in visites:
                    f.appendleft(i)
                    #visites.add(i)
                    pred[i] = n
    return pred

def dfs(mat: list):
    """
    "INCORRECT" car ne va pas à la profondeur max
    même si parcourt bien tout le graphe
    "NON" en fait juste: équivalent à la version itérative
    dans dfs.py
    """
    p = []
    p.append(0)
    visites = set()
    visites.add(0)
    while len(p) > 0:
        n = p.pop()
        print(n, end=" ")
        for i in range(len(mat[n])):
            if mat[n][i] == 1:
                if i not in visites:
                    p.append(i)
                    # c'est ça qui est différent de la version rec
                    visites.add(i)


def dfs_rec(mat: list, s: int, visites: list):
    """
    ok avec premier sommet déjà ds 'visites'
    ne pas faire celui là!!!
    """
    print(s, end=" ")
    for i in range(len(mat[s])):
        if mat[s][i] == 1:
            if i not in visites:
                visites.add(i)
                dfs_rec(mat, i, visites)


def dfs2(mat: list):
    p = []
    p.append(0)
    visites = set()
    while len(p) > 0:
        n = p.pop()
        print(n, end=" ")
        if n not in visites:
            visites.add(n)
            for i in range(len(mat[n])):
                if mat[n][i] == 1:
                    p.append(i)


def dfs_rec2(mat: list, s: int, visites: list):
    """
    ok
    """
    print(s, end=" ")
    if s not in visites:
        visites.add(s)
        for i in range(len(mat[s])):
            if mat[s][i] == 1:
                dfs_rec2(mat, i, visites)


def dfs3(mat: list):
    p = []
    p.append(0)
    visites = set()
    while len(p) > 0:
        n = p.pop()
        print(n, end=" ")
        visites.add(n)
        for i in range(len(mat[n])):
            if mat[n][i] == 1:
                if i not in visites:
                    p.append(i)


def dfs_rec3(mat: list, s: int, visites: list):
    """
    ok
    """
    print(s, end=" ")
    visites.add(s)
    for i in range(len(mat[s])):
        if mat[s][i] == 1:
            if i not in visites:
                dfs_rec3(mat, i, visites)


"""
mat = [[0, 1, 0, 0, 1],
       [1, 0, 0, 0, 0],
       [1, 0, 0, 1, 1],
       [0, 0, 1, 0, 1],
       [1, 0, 1, 1, 0]]
"""
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

# affichage(mat)
# print(bfs(mat))
print("bfs")
bfs(mat)
print("\nbfs2")
bfs2(mat)
print("\ndfs")
dfs(mat)
print("\ndfs_rec")
dfs_rec(mat, 0, {0})
print("\ndfs2")
dfs2(mat)
print("\ndfs_rec2")
dfs_rec2(mat, 0, set())
print("\ndsf3")
dfs3(mat)
print("\ndfs_rec3")
dfs_rec3(mat, 0, set())
print()
