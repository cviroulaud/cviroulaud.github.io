#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Date de création Fri Nov 13 22:21:39 2020

@auteur: Christophe Viroulaud
"""

import pygame
from pygame.locals import *

from constantes import *
from mod_labyrinthe import Labyrinthe
from mod_pirate import Pirate

pygame.init()

#Création de la fenêtre Pygame
fenetre = pygame.display.set_mode((largeur*taille, hauteur*taille))
icone = pygame.image.load(img_icone)
pygame.display.set_icon(icone)
pygame.display.set_caption(titre)

labyrinthe = Labyrinthe(fenetre)
pirate = Pirate(fenetre)

continuer = True
while continuer:
    #Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = True
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                pirate.deplacer(0, labyrinthe.tab)
            elif event.key == K_RIGHT:
                pirate.deplacer(1, labyrinthe.tab)
            elif event.key == K_DOWN:
                pirate.deplacer(2, labyrinthe.tab)
            elif event.key == K_LEFT:
                pirate.deplacer(3, labyrinthe.tab)

    # Affichages aux nouvelles positions
    labyrinthe.afficher()
    pirate.afficher()
    #fenetre.blit(dk.direction, (dk.x, dk.y))
    pygame.display.flip()
