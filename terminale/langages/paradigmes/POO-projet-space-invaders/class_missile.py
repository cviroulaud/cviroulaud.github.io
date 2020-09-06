#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sat Sep  5 17:01:13 2020

@auteur: Christophe Viroulaud
"""


from tkinter import *
from constantes import *

class Missile:

    def __init__(self,canevas):
        self.canevas=canevas
        #charger l'image depuis un fichier
        self.source=PhotoImage(file='ressources/missile.gif')
        #position de départ
        self.x=LARGEUR//2
        self.y=HAUTEUR-self.source.height()//2-10
        self.img=self.canevas.create_image(self.x,self.y,image=self.source)

        self.est_tire=False

    def deplacement(self,event):
        if self.est_tire:
            self.y-=10
            self.canevas.coords(self.img,self.x,self.y)
        else:
            if event.keysym=="Right" and self.x<(LARGEUR-self.source.width()//2):
                self.x+=5
            elif event.keysym=="Left" and self.x>self.source.width()//2:
                self.x-=5

    def tir(self,event):
        self.est_tire=True

    def tir_en_cours(self):
        self.y-=10
        self.canevas.coords(self.img,self.x,self.y)