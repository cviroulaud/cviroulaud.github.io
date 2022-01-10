#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/14 13:40:04
"""

def est_voyelle(lettre:str)->bool:
    """
    vérifie si lettre est une voyelle
    """    
    voyelles = ["a", "e", "i", "o", "u", "y"]
    for v in voyelles:
        if lettre == v:
            return True
    return False

def compter_voyelles(mot: str) -> dict:
    """
    compte le nombre de chaque voyelles de mot
    """
    voyelles = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "y": 0}
    for lettre in mot:
        if est_voyelle(lettre):
            voyelles[lettre] += 1
    return voyelles
            
        
def compter_voyelles3(mot: str) -> dict:
    """
    compte le nombre de chaque voyelles de mot
    """
    voyelles = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "y": 0}
    for lettre in mot:
        # la méthode keys renvoie un itérateur
        # en première approche itérateur = list
        if lettre in voyelles.keys():
            voyelles[lettre] += 1
    return voyelles


def compter_voyelles2(mot: str) -> dict:
    """
    compte le nombre de chaque voyelles de mot
    """
    voyelles = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "y": 0}
    list_voyelles = ["a", "e", "i", "o", "u", "y"]
    for lettre in mot:
        if lettre in list_voyelles:
            voyelles[lettre] += 1
    return voyelles


def max_voyelles(voyelles: dict) -> list:
    """
    parcourt le dict voyelles et renvoie
    celle qui a la plus grande valeur
    """
    maxi = 0
    lettres_maxi = []
    for lettre, nb in voyelles.items():
        if nb > maxi:
            maxi = nb
            # on réinitialise le tableau avec la nouvelle lettre max
            lettres_maxi = [lettre]
        elif nb == maxi:
            lettres_maxi.append(lettre)
    return lettres_maxi


voyelles = compter_voyelles("orangeade")
print(voyelles)

for lettre, nb in voyelles.items():
    print(f"{lettre}: {nb}")

print(compter_voyelles2("orangeade"))
print(max_voyelles(voyelles))
