#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 12 Mars 2022 09:19
"""
import csv


def salaire_max(donnees: list) -> int:
    maxi = 0
    for individu in donnees:
        if individu["salaire"] > maxi:
            maxi = individu["salaire"]
    return maxi


def age_moyen(donnees: list) -> float:
    somme = 0
    for individu in donnees:
        somme = somme+individu["age"]
    return somme/len(donnees)


def dernier(donnees: list) -> str:
    nom = ""
    for individu in donnees:
        if individu["nom"] > nom:
            nom = individu["nom"]
    return nom


f = open("sondage.csv", "r", encoding="utf8")
reader = csv.DictReader(f)
donnees = []
for ligne in reader:
    individu = {}
    # formatage des données
    for cle, val in ligne.items():
        if cle == "age" or cle == "salaire":
            val = int(val)
        individu[cle] = val
    # ajout dans le tableau
    donnees.append(individu)
f.close()
print(salaire_max(donnees))
print(age_moyen(donnees))
print(dernier(donnees))