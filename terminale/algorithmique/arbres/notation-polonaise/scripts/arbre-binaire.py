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
        return 0
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


def prefixe_tab(a: Noeud, parcours: list) -> list:
    if a is not None:
        parcours.append(a.valeur)
        prefixe_tab(a.gauche, parcours)
        prefixe_tab(a.droite, parcours)
        return parcours

def infixe_tab(a: Noeud, parcours: list) -> list:
    if a is not None:
        infixe_tab(a.gauche, parcours)        
        parcours.append(a.valeur)
        infixe_tab(a.droite, parcours)
        return parcours

def postfixe_tab(a: Noeud, parcours: list) -> list:
    if a is not None:
        postfixe_tab(a.gauche, parcours)        
        postfixe_tab(a.droite, parcours)
        parcours.append(a.valeur)
        return parcours
    
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
print("préfixe ",prefixe_tab(arbre, []))
print("infixe ", infixe_tab(arbre, []))
print("postfixe ", postfixe_tab(arbre, []))
