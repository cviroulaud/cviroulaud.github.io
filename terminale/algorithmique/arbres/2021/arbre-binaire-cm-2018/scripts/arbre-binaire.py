#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Thu Jan 21 22:50:12 2021

@auteur: Christophe Viroulaud
"""

from structures import File

class Noeud:

    def __init__(self, v, g, d):
        self.valeur = v
        self.gauche = g
        self.droite = d

def BFS(arbre: Noeud)->list:
    visites = []
    f = File()
    f.enfiler(arbre)
    while not f.est_vide():
        en_cours = f.defiler()
        visites.append(en_cours.valeur)
        if en_cours.gauche is not None:
            f.enfiler(en_cours.gauche)
        if en_cours.droite is not None:
            f.enfiler(en_cours.droite)
    return visites

cdm_arbre = Noeud("France",
              Noeud("France",
                    Noeud("France",
                          Noeud("France",
                                Noeud("France", None, None),
                                Noeud("Argentine", None, None)),
                          Noeud("Uruguay",
                                Noeud("Uruguay", None, None),
                                Noeud("Portugal", None, None))),
                    Noeud("Belgique",
                          Noeud("Brésil",
                                Noeud("Brésil", None, None),
                                Noeud("Mexique", None, None)),
                          Noeud("Belgique",
                                Noeud("Belgique", None, None),
                                Noeud("Japon", None, None)))),
              Noeud("Croatie",
                    Noeud("Croatie",
                          Noeud("Russie",
                                Noeud("Espagne", None, None),
                                Noeud("Russie", None, None)),
                          Noeud("Croatie",
                                Noeud("Croatie", None, None),
                                Noeud("Danemark", None, None))),
                    Noeud("Angleterre",
                          Noeud("Suède",
                                Noeud("Suède", None, None),
                                Noeud("Suisse", None, None)),
                          Noeud("Angleterre",
                                Noeud("Colombie", None, None),
                                Noeud("Angleterre", None, None)))))

cdm_tab = BFS(cdm_arbre)
