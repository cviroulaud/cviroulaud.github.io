#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sat Sep  5 12:21:13 2020

@auteur: Christophe Viroulaud
"""

from tkinter import *
from constantes import *
from class_vaisseau import Vaisseau
from class_invader import Invader
from class_missile import Missile

class Moteur:

    def __init__(self):
        self.fenetre =Tk()
        self.fenetre.title('Space Invaders')
        self.canevas = Canvas(self.fenetre,width=LARGEUR,height=HAUTEUR)
        self.canevas.pack()
        self.vaisseau=Vaisseau(self.canevas)
        self.list_invaders=[]
        for i in range(5):
            self.list_invaders.append(Invader(self.canevas,i))

        self.deplacements()
        self.gestionnaire_event()

        self.fenetre.mainloop()

    def gestionnaire_event(self):
        self.fenetre.bind("<Right>",self.vaisseau.deplacement)
        self.fenetre.bind("<Left>",self.vaisseau.deplacement)
        self.fenetre.bind("<space>",self.vaisseau.tir)

    def deplacements(self):
        for invader in self.list_invaders:
            invader.deplacement()

        if self.vaisseau.a_tire:
            self.vaisseau.tir()

        self.fenetre.after(1000,self.deplacements)


jeu=Moteur()

