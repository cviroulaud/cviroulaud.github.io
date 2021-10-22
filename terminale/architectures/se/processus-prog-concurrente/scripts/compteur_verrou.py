#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 22 Octobre 2021 11:06
"""
from threading import Thread, Lock
from time import sleep

# Variable globale
INTERMEDIAIRE = 0
verrou = Lock()


def calcul():
    global INTERMEDIAIRE
    print("section non critique 1")
    
    for c in range(100):
        # Début de la section critique
        verrou.acquire()
        temp = INTERMEDIAIRE
        # simule un traitement nécessitant des calculs
        sleep(0.000000001)
        INTERMEDIAIRE = temp + 1
        # fin de la section critique
        verrou.release()
        
    print("section non critique 2")



INTERMEDIAIRE = 0
tab_threads = []
for i in range(4):  # Lance en parallèle 4 exécutions de calcul
    p = Thread(target=calcul)
    p.start()      # Lance calcul dans un processus à part.
    tab_threads.append(p)

# On attend la fin de l'exécution des threads.
for p in tab_threads:
    p.join()

print(INTERMEDIAIRE)
