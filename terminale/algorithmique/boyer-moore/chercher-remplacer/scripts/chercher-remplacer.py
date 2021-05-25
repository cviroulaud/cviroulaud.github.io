#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/05/14 15:04:06
"""


def en_minuscule(lettre: str) -> str:
    """
    renvoie la minuscule de lettre
    ou le caractère inchangé si ce n'est pas une lettre
    """
    dec = 32  # ord("a") - ord("A")
    if ord(lettre) >= ord("A") and ord(lettre) <= ord("Z"):
        return chr(ord(lettre)+dec)
    else:
        return lettre


def recherche_naive(texte: str, motif: str) -> list:
    """
    renvoie les positions du motif dans le texte
    """
    global NB_COMPARAISONS
    res = []
    # dernière position = taille(texte) - taille(motif)
    for i in range(len(texte)-len(motif)+1):
        j = 0
        # comparaison de la première lettre
        NB_COMPARAISONS += 1
        while (j < len(motif)) and (en_minuscule(motif[j]) == en_minuscule(texte[i+j])):
            j += 1
            # comparaisons dans la fenêtre
            NB_COMPARAISONS += 1
        if j == len(motif):  # correspondance sur toute la fenêtre
            res.append(i)
    return res


def pretraitement_decalages(motif: str) -> dict:
    """
    renvoie le dictionnaire des décalages à appliquer
    pour chaque lettre du motif (sauf dernière)
    """
    decalages = dict()
    # on s'arrête à l'avant dernière lettre du motif
    for i in range(len(motif)-1):
        # len(motif)-1 est la position de la dernière lettre
        decalages[en_minuscule(motif[i])] = len(motif)-1-i
    return decalages


def decalage_fenetre(decalages: dict, taille: int, lettre: str) -> int:
    """
    renvoie la valeur du décalage à appliquer.
    si la lettre n'est pas dans le tableau
    c'est la taille du motif qui est appliqué

    Args:
        decalages (dict): dico des décalages
        taille (int): taille du motif (= décalage max)
        lettre (str): dernière lettre de la fenêtre

    Returns:
        int: décalage à appliquer
    """
    lettre = en_minuscule(lettre)
    for cle, val in decalages.items():
        if cle == lettre:
            return val
    # si la lettre n'est pas dans le dico (= le motif)
    return taille


def compare(texte: str, position: int, motif: str) -> bool:
    """
    compare le morceau du texte 
    (en partant de position + taille(motif)) 
    avec le motif

    Returns:
        bool: True si on a trouvé le motif
    """
    global NB_COMPARAISONS
    # position de la dernière lettre de la fenêtre
    en_cours = position+len(motif)-1
    # parcours de la fenêtre à l'envers
    for i in range(len(motif)-1, -1, -1):
        # compare au moins la dernère lettre de la fenêtre
        NB_COMPARAISONS += 1
        if not(en_minuscule(texte[en_cours]) == en_minuscule(motif[i])):
            return False
        else:
            en_cours -= 1
    return True


def boyer_moore(texte: str, motif: str) -> list:
    """
    Returns:
        list: les positions du motif dans le texte.
    """
    res = []
    decalages = pretraitement_decalages(motif)
    i = 0
    while i <= len(texte)-len(motif):
        # si on trouve le motif
        if compare(texte, i, motif):
            res.append(i)
            # on recommence à la fin du motif trouvé
            i += len(motif)
        else:
            # sinon on décale (en fonction de la dernière lettre de la fenêtre)
            decale = decalage_fenetre(decalages,
                                      len(motif),
                                      texte[i+len(motif)-1])
            i += decale
    # si on sort de la boucle, on n'a rien trouvé
    return res


def remplacer(livre: str, motif: str, remplacement: str) -> str:
    """
    remplace 'motif' par 'remplacement' dans 'livre'

    Returns:
        str: livre modifié
    """
    positions = boyer_moore(livre, motif)
    livre_modifie = ""
    debut = 0
    for fin in positions:
        livre_modifie += livre[debut: fin] + remplacement
        # recommence à la fin du motif dans livre
        debut = fin + len(motif)
    return livre_modifie


with open("la-guerre-des-mondes-wells.txt", encoding="utf8") as f:
    livre = f.read()
print(len(livre))

NB_COMPARAISONS = 0
print(recherche_naive(livre, "guerre"))
print(NB_COMPARAISONS)

NB_COMPARAISONS = 0
print(boyer_moore(livre, "guerre"))
print(NB_COMPARAISONS)

modifie = remplacer(livre, "guerre", "paix")
fichier = open("la-paix-des-mondes.txt", "w", encoding="utf8")
fichier.write(modifie)
fichier.close()
