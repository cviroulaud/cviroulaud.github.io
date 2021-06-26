#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/06/24 17:38:16
"""

from constantes import *
from outils import *


class Joueur:
    def __init__(self, n: str):
        self.nom = n
        self.x = 0
        self.y = 0
        self.outils = []  # 5 maxi
        self.blocs = {"dirt": 0, "stone": 0, "obsidian": 0}
        self.en_main = 0  # outil en main

    def miner(self, bloc: object) -> bool:
        """
        donne un coup sur le bloc avec l'outil en cours
        ou la main

        Args:
            bloc (object): le bloc miné

        Returns:
            bool: True si le bloc est complètement miné
        """
        # initialise l'impact du coup
        if self.en_main >= len(self.outils):  # pas d'outil
            impact = 1
        else:
            # récupère l'impact de l'objet en cours
            impact = ......
            # l'outil s'use
            ...... -= USURE
        # donne un coup
        bloc.durete -= impact
        
        # récupération éventuelle du bloc
        if bloc.durete <= 0:
            self.blocs[bloc.nom] += 1
            return True
        else:
            return False

    def ramasser_outil(self, outil: object) -> bool:
        """
        place l'outil dans l'inventaire s'il y a de la place

        Args:
            outil (object): l'outil ramassé

        Returns:
            bool: True si l'outil a été ramassé
        """
        if outil is not None:
            if len(self.outils) < NB_OUTILS_INVENTAIRE:
                # l'outil est ajouté à l'inventaire
                ......
                return True
        return False

