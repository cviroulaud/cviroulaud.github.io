#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/06/25 10:49:54
"""
import tkinter
from PIL import Image, ImageTk
from constantes import *
from blocs import *
from outils import *
from joueur import Joueur
from random import shuffle, randint


class Moteur:
    def __init__(self):
        self.fenetre = tkinter.Tk()
        self.fenetre.title("Minecraft")
        self.canevas = tkinter.Canvas(self.fenetre,
                                      width=LARGEUR * TAILLE_BLOC,
                                      height=TAILLE_BLOC*5+HAUTEUR*TAILLE_BLOC)
        self.canevas.pack()
        # pour stocker images de l'inventaire
        self.sources = [None for _ in range(NB_OUTILS_INVENTAIRE)]
        self.sources_outils = [None for _ in range(NB_OUTILS)]
        self.sources_blocs = [None for _ in range(3)]
        self.sources_blocs[0] = ImageTk.PhotoImage(Image.open(
            'ressources/terre.png').resize((2*TAILLE_BLOC, 2*TAILLE_BLOC)))
        self.sources_blocs[1] = ImageTk.PhotoImage(Image.open(
            'ressources/roche.png').resize((2*TAILLE_BLOC, 2*TAILLE_BLOC)))
        self.sources_blocs[2] = ImageTk.PhotoImage(Image.open(
            'ressources/obsidienne.png').resize((2*TAILLE_BLOC, 2*TAILLE_BLOC)))
        # pour placer les outils au début
        self.coordonnees = self.creer_coordonnees(NB_OUTILS)

        self.joueur = None
        self.img_joueur = None
        self.head = ImageTk.PhotoImage(Image.open(
            'ressources/head.png').resize((TAILLE_BLOC, TAILLE_BLOC)))
        self.outils_poses = None
        self.grille = None
        self.selectionne = None

    def commencer(self, joueur: Joueur, grille: list, outils_poses: dict):
        """
        initialise et lance la partie

        Args:
            joueur (Joueur)
            grille (list): tableau des objets (1D)
            outils_poses (list): tableau des outils placés sur la grille
        """
        self.joueur = joueur
        self.grille = grille
        self.outils_poses = outils_poses

        self.boucle_jeu()
        self.gestionnaire_event()
        self.fenetre.mainloop()

    def boucle_jeu(self):
        self.canevas.delete("all")
        # affichage plateau
        for i in range(900):
            if self.grille[i] is not None:
                self.afficher_bloc(i, self.grille[i].couleur)
        self.afficher_outils()
        self.img_joueur = self.afficher_joueur()

        # affichage menu bas
        self.afficher_menu()
        self.afficher_outils_inventaire()
        self.fenetre.after(1000, self.boucle_jeu)

    def afficher_menu(self) -> None:
        """
        affiche le fond du menu
        """
        # cases outils
        for i in range(5):
            self.canevas.create_rectangle(TAILLE_BLOC+3*TAILLE_BLOC*i,
                                          TAILLE_BLOC+LARGEUR*TAILLE_BLOC,
                                          TAILLE_BLOC+3*TAILLE_BLOC*(i+1),
                                          4*TAILLE_BLOC + LARGEUR*TAILLE_BLOC,
                                          fill="#ccc")
        self.selectionne = self.canevas.create_rectangle(TAILLE_BLOC+3*TAILLE_BLOC*self.joueur.en_main,
                                                         TAILLE_BLOC+LARGEUR*TAILLE_BLOC,
                                                         TAILLE_BLOC+3*TAILLE_BLOC *
                                                         (self.joueur.en_main+1),
                                                         4*TAILLE_BLOC + LARGEUR*TAILLE_BLOC,
                                                         fill="#ff0000")
        # inventaire
        
        self.canevas.create_image(18*TAILLE_BLOC, (2+LARGEUR)
                                  * TAILLE_BLOC, image=self.sources_blocs[0])
        self.canevas.create_text(18*TAILLE_BLOC, (4+LARGEUR)*TAILLE_BLOC,
                                 text="x"+str(self.joueur.blocs["dirt"]),
                                 font="Arial 24")        
        
        self.canevas.create_image(21*TAILLE_BLOC, (2+LARGEUR)
                                  * TAILLE_BLOC, image=self.sources_blocs[1])
        self.canevas.create_text(21*TAILLE_BLOC, (4+LARGEUR)*TAILLE_BLOC,
                                 text="x"+str(self.joueur.blocs["stone"]),
                                 font="Arial 24")
        
        self.canevas.create_image(24*TAILLE_BLOC, (2+LARGEUR)
                                  * TAILLE_BLOC, image=self.sources_blocs[2])
        self.canevas.create_text(24*TAILLE_BLOC, (4+LARGEUR)*TAILLE_BLOC,
                                 text="x"+str(self.joueur.blocs["obsidian"]),
                                 font="Arial 24")

    def creer_coordonnees(self, nb: int) -> set:
        """
        crée un ensemble de 'nb' coordonnées (x,y) distinctes

        Args:
            nb (int): le nombre de coordonnées

        Returns:
            set: ensemble des coordonnées
        """
        coordonnees = set()
        for i in range(nb):
            coord = (randint(0, LARGEUR-1), randint(0, HAUTEUR-1))
            while coord in coordonnees:
                coord = (randint(0, LARGEUR-1), randint(0, HAUTEUR-1))
            coordonnees.add(coord)
        return coordonnees

    def donner_coordonnees(self) -> tuple:
        """
        renvoie des coordonnées (x,y) libre (= sans outil)

        Returns:
            tuple: (x,y)
        """
        assert len(
            self.coordonnees) > 0, "Il n'y a plus de coordonnées disponibles."
        return self.coordonnees.pop()

    def afficher_outils_inventaire(self) -> None:
        """
        affiche les outils dans l'inventaire
        """
        for i in range(len(self.joueur.outils)):
            self.sources[i] = ImageTk.PhotoImage(Image.open(
                "ressources/"+self.joueur.outils[i].nom+".png").resize((2*TAILLE_BLOC, 2*TAILLE_BLOC)))
            self.canevas.create_image(TAILLE_BLOC+3*TAILLE_BLOC*(i+0.5),
                                      TAILLE_BLOC +
                                      (1.5+LARGEUR)*TAILLE_BLOC,
                                      image=self.sources[i])

    def afficher_bloc(self, indice: int, couleur: str) -> None:
        """
        place un bloc sur la carte

        Args:
            canevas (tkinter.Canvas)
            indice (int): l'indice du bloc à placer
            couleur (str): la couleur du bloc
        """
        ligne = (indice//LARGEUR)*TAILLE_BLOC
        colonne = (indice % LARGEUR)*TAILLE_BLOC
        self.canevas.create_rectangle(colonne, ligne,
                                      colonne+TAILLE_BLOC, ligne+TAILLE_BLOC,
                                      fill=couleur)

    def afficher_outils(self) -> None:
        """
        place les outils sur la carte

        Args:
            outils (dict): dict "coord: outil"
        """
        i = 0
        for coord, outil in self.outils_poses.items():
            self.sources_outils[i] = ImageTk.PhotoImage(Image.open(
                "ressources/"+outil.nom+".png").resize((TAILLE_BLOC, TAILLE_BLOC)))
            self.canevas.create_image(TAILLE_BLOC*(coord[0]+0.5),
                                      TAILLE_BLOC*(coord[1]+0.5),
                                      image=self.sources_outils[i])
            i += 1

    def afficher_joueur(self) -> object:
        x, y = self.joueur.x, self.joueur.y        
        return self.canevas.create_image((x+0.5)*TAILLE_BLOC, (y+0.5)*TAILLE_BLOC, image=self.head)
        
    def deplacer_joueur(self, event):
        """
        événement à réaliser en fonction touche pressée
        """
        j = self.joueur
        if event.keysym == "Right" and j.x < (LARGEUR-1):
            j.x += 1
        elif event.keysym == "Left" and j.x > 0:
            j.x -= 1
        elif event.keysym == "Up" and j.y > 0:
            j.y -= 1
        elif event.keysym == "Down" and j.y < (HAUTEUR-1):
            j.y += 1
        # efface et redessine le joueur
        self.canevas.coords(self.img_joueur, (j.x+0.5)*TAILLE_BLOC, (j.y+0.5)*TAILLE_BLOC)
        
    def ramasser_outil(self, event):
        """
        ramasse l'outil sur la case (si présent)
        """
        # il y a un outil ici
        if (self.joueur.x, self.joueur.y) in self.outils_poses:
            outil = self.outils_poses[(self.joueur.x, self.joueur.y)]
            if self.joueur.ramasser_outil(outil):
                # on retire de la liste si ramassé
                del self.outils_poses[(self.joueur.x, self.joueur.y)]
        else:
            self.joueur.ramasser_outil(None)

    def poser_outil(self, event):
        """
        pose l'outil sur la case (si vide)
        """
        # il y a un outil ici
        if (self.joueur.x, self.joueur.y) in self.outils_poses:
            outil = self.outils_poses[(self.joueur.x, self.joueur.y)]
            if self.joueur.ramasser_outil(outil):
                # on retire de la liste si ramassé
                del self.outils_poses[(self.joueur.x, self.joueur.y)]
        else:
            self.joueur.ramasser_outil(None)

    def selectionner_outil(self, event):
        """
        choix de l'outil de l'inventaire
        w x c v b
        """
        if event.keysym == "w":
            self.joueur.en_main = 0
        elif event.keysym == "x":
            self.joueur.en_main = 1
        elif event.keysym == "c":
            self.joueur.en_main = 2
        elif event.keysym == "v":
            self.joueur.en_main = 3
        elif event.keysym == "b":
            self.joueur.en_main = 4
        self.canevas.coords(self.selectionne,
                            TAILLE_BLOC+3*TAILLE_BLOC*self.joueur.en_main,
                            TAILLE_BLOC+LARGEUR*TAILLE_BLOC,
                            TAILLE_BLOC+3*TAILLE_BLOC*(self.joueur.en_main+1),
                            4*TAILLE_BLOC + LARGEUR*TAILLE_BLOC)

    def miner_bloc(self, event):
        """
        mine le bloc actuel
        ou
        laboure si c'est pelle + terre
        si une pelle frappe roche ou obsidienne il ne se passe rien
        (changer comportement?)
        """
        indice = self.joueur.y*LARGEUR+self.joueur.x
        bloc = self.grille[indice]
        
        if bloc is not None: # si bloc déjà miné: case vide
            if self.joueur.en_main < len(self.joueur.outils) and \
                self.joueur.outils[self.joueur.en_main].nom == "shovel": # pelle
                # laboure et supprime pelle si usée
                if not self.joueur.outils[self.joueur.en_main].labourer(bloc):
                    self.joueur.outils.pop(self.joueur.en_main)
            else: # main ou pioche
                # efface le bloc si complètement miné
                if self.joueur.miner(bloc):
                    self.grille[indice] = None
                # supprime l'outil si usé
                if self.joueur.en_main < len(self.joueur.outils):  # un outil en main
                    if self.joueur.outils[self.joueur.en_main].resistance <= 0:
                        self.joueur.outils.pop(self.joueur.en_main)

    def gestionnaire_event(self):
        self.fenetre.bind("<Right>", self.deplacer_joueur)
        self.fenetre.bind("<Left>", self.deplacer_joueur)
        self.fenetre.bind("<Up>", self.deplacer_joueur)
        self.fenetre.bind("<Down>", self.deplacer_joueur)
        self.fenetre.bind("<r>", self.ramasser_outil)
        self.fenetre.bind("<w>", self.selectionner_outil)
        self.fenetre.bind("<x>", self.selectionner_outil)
        self.fenetre.bind("<c>", self.selectionner_outil)
        self.fenetre.bind("<v>", self.selectionner_outil)
        self.fenetre.bind("<b>", self.selectionner_outil)
        self.fenetre.bind("<space>", self.miner_bloc)
