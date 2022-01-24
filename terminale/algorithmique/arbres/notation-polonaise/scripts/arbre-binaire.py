#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Jan 21 22:50:12 2021

@auteur: Christophe Viroulaud
"""


class Noeud:

    def __init__(self, v, g, d):
        self.valeur = v
        self.gauche = g
        self.droite = d


def taille(a: Noeud) -> int:
    """
    renvoie le nombre de noeuds de l'arbre a
    """
    if a is None:
        return 0
    else:
        return 1 + taille(a.gauche) + taille(a.droite)


def hauteur(a: Noeud) -> int:
    """
    hauteur max de l'arbre a
    """
    if a is None:
        # on compte les arcs et pas les nœuds
        return -1
    else:
        return 1 + max(hauteur(a.gauche), hauteur(a.droite))


def prefixe(a: Noeud) -> None:
    if a is not None:
        print(a.valeur, end=" ")
        prefixe(a.gauche)
        prefixe(a.droite)


def infixe(a: Noeud) -> None:
    if a is not None:
        infixe(a.gauche)
        print(a.valeur, end=" ")
        infixe(a.droite)


def postfixe(a: Noeud) -> None:
    if a is not None:
        postfixe(a.gauche)
        postfixe(a.droite)
        print(a.valeur, end=" ")


def prefixe_tab(a: Noeud, parcours: list) -> None:
    if a is not None:
        parcours.append(a.valeur)
        prefixe_tab(a.gauche, parcours)
        prefixe_tab(a.droite, parcours)

def infixe_tab(a: Noeud, parcours: list) -> None:
    if a is not None:
        infixe_tab(a.gauche, parcours)        
        parcours.append(a.valeur)
        infixe_tab(a.droite, parcours)
        return parcours

def postfixe_tab(a: Noeud, parcours: list) -> None:
    if a is not None:
        postfixe_tab(a.gauche, parcours)        
        postfixe_tab(a.droite, parcours)
        parcours.append(a.valeur)
        return parcours
    
def prefixe_tab2(a: Noeud) -> list:
    if a is not None:
        return [a.valeur] + \
                    prefixe_tab2(a.gauche) + \
                    prefixe_tab2(a.droite)
    else:
        return []
        
arbre = Noeud("×",
              Noeud(2, None, None),
              Noeud("+",
                    Noeud(3, None, None),
                    Noeud(4, None, None)))

print(taille(arbre))
print(hauteur(arbre))
prefixe(arbre)
print()
infixe(arbre)
print()
postfixe(arbre)
print()

tab_prefixe = []
prefixe_tab(arbre, tab_prefixe)
print("préfixe ", tab_prefixe)

tab_infixe = []
infixe_tab(arbre, tab_infixe)
print("infixe ", tab_infixe)

tab_postfixe = []
postfixe_tab(arbre, tab_postfixe)
print("postfixe ", tab_postfixe)

print("préfixe v2", prefixe_tab2(arbre))