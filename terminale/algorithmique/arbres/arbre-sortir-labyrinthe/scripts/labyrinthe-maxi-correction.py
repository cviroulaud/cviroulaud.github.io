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
        for y in range(self.dimension):
            for x in range(self.dimension):
                self.graphe.ajouter_sommet((x,y))

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
            if (en_cours[0] + dx >= 0) and \
                (en_cours[0] + dx < self.dimension) and \
                (en_cours[1] + dy >= 0) and \
                (en_cours[1] + dy < self.dimension):
                v.append((en_cours[0]+dx, en_cours[1]+dy))
        return v

    def creer_dfs(self)->None:
        """
        crée le labyrinthe avec un dfs
        """
        # création des sommets
        self.creer_sommets()

        p = Pile()
        # démarre d'une cellule au hasard
        p.empiler((randint(0, self.dimension-1), randint(0, self.dimension-1)))

        visites = set()

        while not p.est_vide():
            en_cours = p.depiler()
            if en_cours not in visites:
                visites.add(en_cours)

                # ajout des voisins (mélangés) dans la pile
                voisins = self.get_voisins(en_cours)
                shuffle(voisins) # mélange pour ajouter de l'aléatoire
                for v in voisins:
                    p.empiler(v)

                # recherche un des voisins qui est déjà dans le labyrinthe
                for v in voisins:
                    if v in visites:
                        self.graphe.ajouter_arete(en_cours, v)
                        break

    def chemin_sortie(self)->list:
        """
        renvoie le chemin entre (0,0) et (dim-1,dim-1)
        """
        return self.graphe.plus_court_chemin_detail((0,0), (self.dimension-1,self.dimension-1))

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

