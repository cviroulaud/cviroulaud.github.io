#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Jan 18 13:01:42 2021

@auteur: Christophe Viroulaud
"""


from structures import File

class Noeud:
    def __init__(self, v: str, f: list)->None:
        self.valeur = v
        self.fils = f

arbre = Noeud(None, [Noeud("recette", [Noeud("Fondant au chocolat", [])]),
                     Noeud("difficulté", [Noeud("facile", [])]),
                     Noeud("temps", [Noeud("préparation", [Noeud("unite", [Noeud("min", [])]),
                                                           Noeud("valeur", [Noeud("15", [])])]),
                                     Noeud("cuisson", [Noeud("unite", [Noeud("min", [])]),
                                                       Noeud("valeur", [Noeud("17", [])]),
                                                       Noeud("temperature", [Noeud("180", [])])])]),
                     Noeud("ingrédients", [Noeud("chocolat noir", [Noeud("unite", [Noeud("g", [])]),
                                                                   Noeud("quantite", [Noeud("200", [])])]),
                                           Noeud("beurre", [Noeud("unite", [Noeud("g", [])]),
                                                            Noeud("quantite", [Noeud("100", [])])]),
                                           Noeud("sucre", [Noeud("unite", [Noeud("g", [])]),
                                                           Noeud("quantite", [Noeud("100", [])])]),
                                           Noeud("oeufs", [Noeud("unite", [Noeud("", [])]),
                                                           Noeud("quantite", [Noeud("5", [])])]),
                                           Noeud("farine", [Noeud("unite", [Noeud("g", [])]),
                                                            Noeud("quantite", [Noeud("20", [])])])]),
                     Noeud("étapes",[Noeud("Faire fondre le chocolat et le beurre au micro-onde", []),
                                     Noeud("Ajouter les jaunes d'oeufs et battre le tout", []),
                                     Noeud("Ajouter le sucre et la farine", []),
                                     Noeud("Incorporer les oeufs battus en neige ferme", []),
                                     Noeud("Faire cuire au four à 180°C pendant 17 minutes", [])])])

