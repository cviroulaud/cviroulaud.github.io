#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 13 Mars 2022 23:04
"""

from constantes import *


class Joueur:

    def __init__(self):
        self.ligne = 0
        self.colonne = 0

    def deplacement(self, event):
        # écoute de l'événement et réaction
        if event.keysym == "Right" and self.ligne < TAILLE-1:
            self.ligne += 1
        elif event.keysym == "Left" and self.ligne > 0:
            self.ligne -= 1
