#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/29 14:51:55
"""

import tkinter
from tkinter import ttk
import csv


def callback_combo(event):
    """
    fonction de rappel quand on change de pokemon
    dans la combobox
    """
    num = event.widget.current()
    remplir_carte(num)


def remplir_carte(num_pok: int) -> None:
    """
    complète la carte d'affichage du pokemon
    NB: la photo est notée comme une variable globale
    pour qu'elle ne soit pas effacée par le ramasse-miettes
    à la sortie de la fonction
    """
    global photo
    pok = pokedex[num_pok]

    photo = tkinter.PhotoImage(file=pok["img"])
    label_photo["image"] = photo
    label_nom["text"] = pok["name"]
    label_poids["text"] = str(pok["weight"])+"kg"
    label_taille["text"] = str(pok["height"])+"m"


"""
récupération des données
"""
fichier = open("pokedex.csv")
data = csv.DictReader(fichier)
pokedex = []
for pokemon in data:
    dico = {}
    for cle, val in pokemon.items():
        if cle == "height" or cle == "weight":
            val = float(val)
        dico[cle] = val
    pokedex.append(dico)
fichier.close()

"""
création de l'interface
"""
fenetre = tkinter.Tk()
fenetre.title("Pokemon Go")

"""
boite de sélection
"""
noms_affiches = [pokemon["name"] for pokemon in pokedex]
combo_pok = ttk.Combobox(fenetre, values=noms_affiches)
combo_pok.current(0)
combo_pok.pack()
combo_pok.bind("<<ComboboxSelected>>", callback_combo)

"""
carte du pokemon
"""
bloc_carte = tkinter.Frame(fenetre)
label_nom = tkinter.Label(bloc_carte)
label_nom.grid(column=0, row=0)
label_photo = tkinter.Label(bloc_carte)
label_photo.grid(column=1, row=0)
label_poids = tkinter.Label(bloc_carte)
label_poids.grid(column=0, row=1)
label_taille = tkinter.Label(bloc_carte)
label_taille.grid(column=1, row=1)
bloc_carte.pack()

remplir_carte(0)
fenetre.mainloop()
