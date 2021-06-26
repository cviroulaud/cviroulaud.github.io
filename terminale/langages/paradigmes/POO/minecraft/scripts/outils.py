#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/06/22 23:52:14
"""

from constantes import *


class Pioche:
    def __init__(self, nom: str):
        self.nom = nom
        if nom == "wood_pickaxe":
            self.resistance = 30
            self.impact = 5
        elif nom == "diamond_pickaxe":
            self.resistance = 100
            self.impact = 100

    def piocher(self, bloc: object) -> bool:
        """
        donne un coup sur le bloc

        Args:
            bloc (object): le bloc miné

        Returns:
            bool: False si l'outil est complètement usé
        """
        bloc.durete -= self.impact
        self.resistance -= USURE
        if self.resistance <= 0:
            return False
        return True


class Pelle:
    def __init__(self):
        self.nom = "shovel"
        self.resistance = 50
        self.impact = 0

    def labourer(self, bloc: object) -> bool:
        """
        laboure un bloc terre (non déjà labourée), 
        ne fait rien sinon

        Args:
            bloc (object): le bloc en cours

        Returns:
            bool: False si l'outil est complètement usé
        """
        if bloc.nom == "dirt" and not bloc.est_labouree:
            bloc.est_labouree = True
            bloc.couleur = "#712712"
            self.resistance -= USURE
            if self.resistance <= 0:
                return False
        return True
