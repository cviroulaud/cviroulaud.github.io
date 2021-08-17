#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/08/06 15:27:17

pas fini: vers ligne 100
"""
ROUGE = 0
NOIR = 1


class Noeud:
    def __init__(self, val: int, p, g=None, d=None) -> None:
        self.valeur = val
        self.gauche = g
        self.droite = d
        self.pere = p  # None <-> ce noeud est racine
        self.couleur = ROUGE


def get_oncle(n: Noeud) -> Noeud:
    """
    retourne l'oncle de n
    en remontant vers le grand-père
    """
    grandpere = n.pere.pere
    # si le père de n est le fils gauche de grandpere
    if n.pere == grandpere.gauche:
        return grandpere.droite
    else:
        return grandpere.gauche


def get_pere(n: Noeud) -> Noeud:
    return n.pere


def get_grandpere(n: Noeud) -> Noeud:
    return n.pere.pere


def rotation_gauche(n: Noeud) -> None:
    filsdroit = n.droite
    # le 'futur fils gauche' récupère le fils gauche de son fils droit
    n.droite = filsdroit.gauche
    # rétablit nouveau père dans l'ancien fils gauche du fils droit
    n.droite.pere = n

    filsdroit.pere = n.pere
    # rétablit le nouveau fils (gauche ou droite) pour l'ancien père de n
    if n.pere is not None:  # on n'est pas à la racine
        if n.pere.gauche == n:
            n.pere.gauche = filsdroit
        else:
            n.pere.droit = filsdroit

    filsdroit.gauche = n
    n.pere = filsdroit


def rotation_droite(n: Noeud) -> None:
    filsgauche = n.gauche
    n.gauche = filsgauche.droite
    n.gauche.pere = n

    filsgauche.pere = n.pere
    if n.pere is not None:
        if n.pere.gauche == n:
            n.pere.gauche = filsgauche
        else:
            n.pere.droite = filsgauche

    filsgauche.droite = n
    n.pere = filsgauche


def retablir_rouge_noir(nouveau: Noeud, abr: Noeud):
    pere = get_pere(nouveau)
    grandpere = get_grandpere(nouveau)
    oncle = get_oncle(nouveau)

    if pere is None:  # noeud racine
        nouveau.couleur = NOIR
    # si le père est NOIR on n'a rien à faire
    elif pere.couleur==NOIR:
        pass
    elif pere.couleur == ROUGE:
        # si l'oncle est rouge
        if oncle.couleur == ROUGE:
            # changements de couleur
            pere.couleur = NOIR
            oncle.couleur = NOIR
            grandpere = ROUGE
            retablir_rouge_noir(grandpere, abr)
        else:  # oncle noir
            # À FINIR

def inserer_rec(nouveau: Noeud, pere: Noeud) -> None:
    if nouveau.valeur < pere.valeur:
        if pere.gauche is None:
            pere.gauche = nouveau
            nouveau.pere = pere
        else:
            inserer_rec(nouveau, pere.gauche)
    else:
        if pere.droite is None:
            pere.droite = nouveau
            nouveau.pere = pere
        else:
            inserer_rec(nouveau, pere.droite)


def inserer(val: int, abr: Noeud) -> Noeud:
    nouveau = Noeud(val, None)
    # insertion
    if abr is None:  # arbre vide
        abr = nouveau
    else:
        inserer_rec(nouveau, abr)

    # rétablir alternance rouge-noir
    retablir_rouge_noir(nouveau, abr)

    return abr


if __name__ == "__main__":
    abr = None
    inserer(10, abr)
