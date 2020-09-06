#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sat Sep  5 12:21:13 2020

@auteur: Christophe Viroulaud
"""

from tkinter import *
from constantes import *
from class_vaisseau import Vaisseau
from class_asteroide import Asteroide

class Moteur:

    def __init__(self):
        self.fenetre =Tk()
        self.fenetre.title('Asteroid')
        self.canevas = Canvas(self.fenetre,width=LARGEUR,height=HAUTEUR)
        self.canevas.pack()

        self.commence_partie()
        self.fenetre.mainloop()

    def commence_partie(self,event=None):
        self.canevas.delete("all")
        self.perdu=False
        self.vaisseau=Vaisseau(self.canevas)
        self.list_asteroides=[]
        self.boucle_jeu()
        self.gestionnaire_event()

    def gestionnaire_event(self):
        self.fenetre.bind("<Right>",self.vaisseau.deplacement)
        self.fenetre.bind("<Left>",self.vaisseau.deplacement)

    def boucle_jeu(self):
        #création astéroides
        self.list_asteroides.append(Asteroide(self.canevas))

        #déplacements des astéroides
        for asteroide in self.list_asteroides:
            asteroide.deplacement()

        #gestion des collisions
        for asteroide in self.list_asteroides:
            if(self.vaisseau.est_touche(asteroide)):
                self.perdu=True
                break

        if self.perdu:
            self.canevas.create_text(LARGEUR//2, HAUTEUR//2,
                                     text="GAME OVER",
                                     font="Arial 36",
                                     tag="gameover")
            self.fenetre.unbind("<Right>")
            self.fenetre.unbind("<Left>")
            self.fenetre.bind("<Escape>",self.commence_partie)
        else:
            #boucle
            self.fenetre.after(1000,self.boucle_jeu)



