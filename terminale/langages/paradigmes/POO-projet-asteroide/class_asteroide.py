#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sat Sep  5 15:51:39 2020

@auteur: Christophe Viroulaud
"""

from tkinter import *
from constantes import *
from random import randint

class Asteroide:

    def __init__(self,canevas):
        self.canevas=canevas
        #charger l'image depuis un fichier
        self.source=PhotoImage(file='ressources/asteroide.gif')
        #position de départ
        self.x=randint(0,9)*self.source.width()+self.source.width()//2
        self.y=self.source.height()//2
        self.img=self.canevas.create_image(self.x,self.y,image=self.source)

    def deplacement(self):
        self.y+=self.source.height()
        self.canevas.coords(self.img,self.x,self.y) #efface et redessine l'objet

