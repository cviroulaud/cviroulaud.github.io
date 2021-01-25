#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sun Nov 22 11:35:01 2020

@auteur: Christophe Viroulaud
"""


from mod_graphe import Graphe
from structures import Pile
from random import randint, shuffle
import networkx as nx
import matplotlib.pyplot as plt

class Labyrinthe:
    delta = ((-1,0), (0,1), (1,0), (0,-1))

    def __init__(self, dim: int):
        """
        crée un labyrinthe carré de côté 'dimension'
        """
        self.dimension = dim
        self.graphe = Graphe()
        self.creer_dfs()

    def creer_sommets(self)->None:
        pass

    def get_voisins(self, en_cours: object)->list:
        """
        renvoie les voisins de en_cours

        Parameters
        ----------
        en_cours : object
            la cellule en cours.

        Returns
        -------
        set
            les voisins de en_cours.

        """
        v = []
        # regarde les 4 côtés de en_cours
        for dx, dy in Labyrinthe.delta:
            # la cellule voisine est-elle dans les limites?
            pass
        return v

    def creer_dfs(self)->None:
        """
        crée le labyrinthe avec un dfs
        """
        # création des sommets
        self.creer_sommets()
        visites = set()
        pass

    def chemin_sortie(self)->list:
        """
        renvoie le chemin entre (0,0) et (dim-1,dim-1)
        """
        pass

    def affiche_chemins(self):
        """
        affiche l'arbre
        """
        g = nx.Graph()
        for s in self.graphe.get_sommets():
            g.add_node(s)

        for s in self.graphe.get_sommets():
            for a in self.graphe.get_adjacents(s):
                g.add_edge(s, a)

        plt.figure(figsize=(15,15))
        nx.draw(g,node_size=1000, node_color='gray', with_labels=True)
        plt.savefig("labyrinthe.png", format="PNG")



laby = Labyrinthe(5)
print(laby.chemin_sortie())
laby.affiche_chemins()

