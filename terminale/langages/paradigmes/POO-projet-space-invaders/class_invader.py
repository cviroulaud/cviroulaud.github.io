#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sat Sep  5 15:51:39 2020

@auteur: Christophe Viroulaud
"""

from tkinter import *
from constantes import *

class Invader:

    def __init__(self,canevas,rang):
        self.canevas=canevas
        #charger l'image depuis un fichier
        self.source=PhotoImage(file='ressources/invader.gif')
        #position de départ
        self.x=18+(self.source.width()+36)*rang+self.source.width()//2
        self.y=self.source.height()//2+10
        self.img=self.canevas.create_image(self.x,self.y,image=self.source)

    def deplacement(self):
        self.y+=5
        self.canevas.coords(self.img,self.x,self.y) #efface et redessine l'objet

