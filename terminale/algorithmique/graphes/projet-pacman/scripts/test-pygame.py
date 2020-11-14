#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Nov 13 22:21:39 2020

@auteur: Christophe Viroulaud
"""


import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("ressources/background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("ressources/perso.png").convert_alpha()
fenetre.blit(perso, (200,300))

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
            pygame.quit()