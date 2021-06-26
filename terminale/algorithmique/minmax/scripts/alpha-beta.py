#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/06/10 13:20:19

d'après https://www.youtube.com/watch?v=f30Ry1WOe_Q
notamment les évaluations
"""

COMPTEUR = 0


def maxi(prof: int, evals: list) -> int:
    global COMPTEUR

    if prof == 0:
        return evals.pop(0)

    score_maxi = 0
    for _ in range(2):
        COMPTEUR += 1
        score_maxi = max(score_maxi, mini(prof-1, evals))
    return score_maxi


def mini(prof: int, evals: list) -> int:
    global COMPTEUR

    if prof == 0:
        return evals.pop(0)

    score_mini = 100
    for _ in range(2):
        COMPTEUR += 1
        score_mini = min(score_mini, maxi(prof-1, evals))
    return score_mini


def maxi_alpha_beta(prof: int, evals: list, alpha: int, beta: int) -> int:
    global COMPTEUR

    if prof == 0:
        return evals.pop(0)

    score_maxi = 0
    for _ in range(2):
        COMPTEUR += 1
        score_maxi = max(score_maxi, mini_alpha_beta(
            prof-1, evals, alpha, beta))

        if score_maxi >= beta:
            return score_maxi

        if score_maxi > alpha:
            alpha = score_maxi

    return score_maxi


def mini_alpha_beta(prof: int, evals: list, alpha: int, beta: int) -> int:
    global COMPTEUR

    if prof == 0:
        return evals.pop(0)

    score_mini = 100
    for _ in range(2):
        COMPTEUR += 1
        score_mini = min(score_mini, maxi_alpha_beta(
            prof-1, evals, alpha, beta))

        if score_mini <= alpha:
            return score_mini

        if score_mini < beta:
            beta = score_mini
    return score_mini


evaluations = [50, 60, 61, 58, 30, 55, 20, 50, 70, 63, 71, 70, 65, 61,
               64, 63, 50, 57, 51, 53, 30, 51, 80, 50, 70, 60, 60, 58, 63, 61, 64, 63]
profondeur = 5

print(maxi(profondeur, evaluations))
print(COMPTEUR)

COMPTEUR = 0
evaluations = [50, 60, 61, 58, 30, 55, 20, 50, 70, 63, 71, 70, 65, 61,
               64, 63, 50, 57, 51, 53, 30, 51, 80, 50, 70, 60, 60, 58, 63, 61, 64, 63]
"""
Il est normal de ne pas obtenir la même chose que dans la vidéo:
qd on élague on ne 'pop' plus la bonne valeur de l'arbre de la vidéo
"""
print(maxi_alpha_beta(profondeur, evaluations, 0, 100))
print(COMPTEUR)
