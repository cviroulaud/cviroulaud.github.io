#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sat Sep  5 13:52:16 2020

@auteur: Christophe Viroulaud
"""

from tkinter import *
from constantes import *
from class_missile import Missile

class Vaisseau:

    def __init__(self,canevas):
        self.canevas=canevas
        #charger l'image depuis un fichier
        self.source=PhotoImage(file='ressources/vaisseau.gif')
        #position de départ
        self.x=LARGEUR//2
        self.y=HAUTEUR-self.source.height()//2-10
        self.img=self.canevas.create_image(self.x,self.y,image=self.source)

        self.a_tire=False
        self.missile=Missile(self.canevas)


    def deplacement(self,event):
        if event.keysym=="Right" and self.x<(LARGEUR-self.source.width()//2):
            self.x+=5
        elif event.keysym=="Left" and self.x>self.source.width()//2:
            self.x-=5
        self.canevas.coords(self.img,self.x,self.y) #efface et redessine l'objet

    def tir(self):
        self.missile.tir_en_cours(True)
