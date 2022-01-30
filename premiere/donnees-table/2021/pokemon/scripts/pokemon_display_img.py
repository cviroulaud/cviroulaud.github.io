#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/29 14:51:55
"""

import tkinter
from pokemon_utils import creer_image

fenetre = tkinter.Tk()
# l'image est crée avec 'fenetre' pour référence
image_affichee = creer_image(fenetre, 
    "http://www.serebii.net/pokemongo/pokemon/001.png")
# l'image est plaquée dans 'fenetre'
image_affichee.pack()

lab = tkinter.Label(text="test")
lab.pack()
fenetre.mainloop()