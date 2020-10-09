#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Oct  9 11:50:25 2020

@auteur: Christophe Viroulaud
"""


import turtle as t

def get_coord(x: int, y: int)->tuple:
    return (x,y)

def dessiner_pion(coord: tuple, couleur: int):
    t.goto(coord)
    t.dot(50, couleur)


"""
paramétrage de la fenêtre
"""
t.setup(700,700)
t.setworldcoordinates(0,0,700,700)
t.title("Puissance 4")
t.bgcolor("blue")
t.hideturtle()
t.goto(0, 0)

"""
grille de jeu
0 = vide
1 = rouge
2 = jaune
"""
grille = [[0 for i in range(7)] for j in range(6)]
#création graphique de la grille
for i in range(7):
    for j in range(6):
        t.up()
        t.goto(i*100+50, j*100+50)
        t.down()
        t.dot(80, "white")

tour = 1

t.onscreenclick(get_coord)
t.mainloop()
