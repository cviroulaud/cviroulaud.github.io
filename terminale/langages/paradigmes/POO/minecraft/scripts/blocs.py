#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/06/22 23:42:38
"""


class Terre:
    def __init__(self):
        self.nom = "dirt"
        self.durete = 10
        self.couleur = "#a94800"
        self.est_labouree = False


class Roche:
    def __init__(self):
        self.nom = "stone"
        self.durete = 100
        self.couleur = "#6f6f6f"
        self.est_gravat = False


class Obsidienne:
    def __init__(self):
        self.nom = "obsidian"
        self.durete = 1000
        self.couleur = "#090909"
