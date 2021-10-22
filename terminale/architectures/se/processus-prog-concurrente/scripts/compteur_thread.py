#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Jeudi 21 Octobre 2021 22:34
"""
from threading import Thread
from time import sleep

INTERMEDIAIRE = 0


def calcul():
    global INTERMEDIAIRE
    print("section non critique 1")
    
    for c in range(100):
        # début section critique
        temp = INTERMEDIAIRE
        
        # simule un traitement nécessitant des calculs
        sleep(0.000000001)
        
        INTERMEDIAIRE = temp + 1
        # fin section critique
        
    print("section non critique 2")



tab_threads = []
for i in range(4):  # Lance en parallèle 4 exécutions de calcul
    p = Thread(target=calcul)
    p.start()      # Lance calcul dans un processus à part.
    tab_threads.append(p)

# On attend la fin de l'exécution des threads.
for p in tab_threads:
    p.join()

print(INTERMEDIAIRE)
