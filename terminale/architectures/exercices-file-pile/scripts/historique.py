#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Oct 13 08:28:20 2020

@auteur: Christophe Viroulaud
"""


import csv
from datetime import datetime

class Noeud:
    def __init__(self,e,s):
        self.donnees = e
        self.successeur = s

class Historique:
    def __init__(self):
        self.dernier = None

    def est_vide(self):
        return self.dernier is None

    def empiler(self,e):
        self.dernier = Noeud(e,self.dernier)

    def depiler(self):
        if not self.est_vide():
            res = self.dernier.donnees
            self.dernier = self.dernier.successeur
            return res

    def retour(self)->str:
        res = self.depiler()
        if res is not None:
            return res["site"]
        else:
            return "Pas d'historique"

    def nouvelle_adresse(self, lien: str)->None:
        self.empiler({"date":datetime.now().strftime("%Y-%m-%d %H:%M"),
                      "site": lien})

    def __str__(self):
        affiche = ""
        last = self.dernier
        while last is not None:
            affiche += str(last.donnees) +"\n"
            last = last.successeur
        return affiche

historique = Historique()
fichier_histo = open("historique.csv")

for lien in csv.DictReader(fichier_histo, delimiter=";"):
    # le noeud sera un dictionnaire
    historique.empiler(lien)

print(historique.retour())
historique.nouvelle_adresse("https://docs.python.org/fr/3/")
print(historique.retour())

fichier_histo.close()