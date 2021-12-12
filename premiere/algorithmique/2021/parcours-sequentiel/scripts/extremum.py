#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/14 01:12:33
"""
from random import randint

les_notes = [randint(0, 20) for _ in range(30)]


def maxi(tab: list) -> int:
    """
    Renvoie la valeur maximale de tab
    """
    note_max = 0
    for note in tab:
        if note > note_max:
            note_max = note
    return note_max


def extrema(tab: list) -> tuple:
    """
    Renvoie le mini et le maxi de tab

    Args:
        tab (list): 
    Returns:
        tuple: (mini, maxi)
    """
    mini = 20
    maxi = 0
    for note in tab:
        if note < mini:
            mini = note
        if note > maxi:
            maxi = note
    return (mini, maxi)


def maxi_position(tab: list) -> tuple:
    """
    renvoie le max et sa première position dans le tableau
    """
    # On peut affecter plusieurs variables sur 1 ligne
    indice, note_max = 0, 0
    for i in range(len(tab)):
        if tab[i] > note_max:
            note_max = tab[i]
            indice = i
    return (indice, note_max)


def maxi_position_dernier(tab: list) -> tuple:
    """
    renvoie le max et sa dernière position dans le tableau
    """
    # On peut affecter plusieurs variables sur 1 ligne
    indice, note_max = 0, 0
    for i in range(len(tab)):
        # il suffit juste de modifier la comparaison
        if tab[i] >= note_max:
            note_max = tab[i]
            indice = i
    return (indice, note_max)


def maxi_nb(tab: list) -> int:
    """
    renvoie le nombre d'occurences du maximum
    """
    nb, note_max = 0, 0
    for note in tab:
        if note > note_max:
            # réinitialisation du max
            note_max = note
            nb = 1
        elif note == note_max:
            nb += 1
    return nb


print(les_notes)
print(maxi.__name__, maxi(les_notes))
print(extrema.__name__, extrema(les_notes))
print(maxi_position.__name__, maxi_position(les_notes))
print(maxi_position_dernier.__name__, maxi_position_dernier(les_notes))
print(maxi_nb.__name__, maxi_nb(les_notes))