#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/15 21:57:26
"""

import csv


def trouver_app(mot_cle: str, tab: list) -> list:
    """
    renvoie les applications contenant le 'mot_cle'

    chaque mot commence par une majuscule dans la table
    """
    res = []
    for app in tab:
        if mot_cle in app["Name"]:
            res.append(app)
    return res


def trouver_app2(mot_cle: str, tab: list) -> list:
    """
    renvoie les applications contenant tous les 'mot_cle'
    """
    res = []
    # sépare les mots-clés et les stocke dans une liste
    mots = mot_cle.lower().split()

    for app in tab:
        i = 0
        while i < len(mots) and mots[i] in app["Name"].lower():
            i += 1
        if i == len(mots):
            res.append(app)
    return res


def meilleur_app_notee(tab: list) -> dict:
    """
    renvoie l'application avec la meilleure note de tab
    """
    note_maxi = 0
    meilleure_app = None
    for app in tab:
        if app["Rating"] > note_maxi:
            note_maxi = app["Rating"]
            meilleure_app = app
    return meilleure_app


def moyenne_note(tab: list) -> float:
    """
    renvoie la note moyenne des apps de tab
    """
    somme = 0
    nb = 0
    for app in tab:
        # Si l'app a déjà été notée
        if app["Rating"] >= 0:
            somme += app["Rating"]
            nb += 1
    return round(somme/nb, 2)


def parametres_tri_1(app: dict) -> float:
    """
    renvoie le Rating de l'app
    """
    return app["Rating"]


def parametres_tri_2(app: dict) -> tuple:
    """
    renvoie le tuple (Rating, Reviews) de l'app
    """
    return (app["Rating"], app["Reviews"])


def tri_insertion(tab: list) -> None:
    """
    tri le tableau dans l'ordre croissant des notes
    """
    for i in range(len(tab)):
        # mémoriser
        en_cours = tab[i]
        pos = i
        # décaler
        while pos > 0 and en_cours["Rating"] < tab[pos-1]["Rating"]:
            tab[pos] = tab[pos-1]
            pos = pos-1
        # insérer
        tab[pos] = en_cours


# charge le fichier dans le programme
fichier = open("googleplaystore.csv", encoding="utf8")
# crée un itérateur sur les données
lecteur_donnees = csv.DictReader(fichier)

# validation des données
table = []
for ligne in lecteur_donnees:
    dico = {}
    for nom, val in ligne.items():
        if nom == "Rating":
            if val == "NaN":
                val = -1.0
            else:
                val = float(val)
        if nom == "Installs" or nom == "Reviews":
            if val == "NaN":
                val = 0
            else:
                val = int(val)
        dico[nom] = val
    table.append(dico)
# libère le fichier externe
fichier.close()

applications = trouver_app("Photo", table)
print(meilleur_app_notee(applications))
moyenne = moyenne_note(applications)
print(moyenne)
meilleur_app = [app for app in applications if app["Rating"] > moyenne]
print(len(meilleur_app))
print(len(applications))

applications2 = trouver_app2("Photo easy", table)
print(applications2)

apps_triees = sorted(applications, key=parametres_tri_1)
for i in (range(5)):
    print(f"Top {i+1}:", apps_triees[i]["Name"])
#print(sorted(applications, key=parametres_tri_2))

tri_insertion(applications)
for i in (range(5)):
    print(f"Top {i+1}:", applications[i]["Name"])
