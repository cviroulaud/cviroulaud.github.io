#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 22 Octobre 2021 13:57
"""
from threading import Thread
from threading import Lock
import time
import random

COMPTEUR = 0


def pilotage_manuel():
    global COMPTEUR
    while True:
        print("pilotage manuel : demande de moteurs...")
        moteurs.acquire()
        print("pilotage manuel : demande de wifi...")
        wifi.acquire()
        print("pilotage manuel : début travail")
        time.sleep(random.random()/100.0)
        print("pilotage manuel : fin travail")
        COMPTEUR += 1
        print(f"*** {COMPTEUR} tâche(s) terminée(s)")
        print("pilotage manuel : libération de moteurs...")
        moteurs.release()
        print("pilotage manuel : libération de wifi...")
        wifi.release()


def flux_video():
    global COMPTEUR
    while True:
        print("flux vidéo : demande de wifi...")
        wifi.acquire()
        print("flux vidéo : demande de caméra...")
        camera.acquire()
        print("flux vidéo : début travail")
        time.sleep(random.random()/100.0)
        print("flux vidéo : fin travail")
        COMPTEUR += 1
        print(f"*** {COMPTEUR} tâche(s) terminée(s)")
        print("flux vidéo : libération de wifi...")
        wifi.release()
        print("flux vidéo : libération de caméra...")
        camera.release()


def autotest():
    global COMPTEUR
    while True:
        print("autotest : demande de caméra...")
        camera.acquire()
        print("autotest : demande de moteurs...")
        moteurs.acquire()
        print("autotest : début travail")
        time.sleep(random.random()/100.0)
        print("autotest : fin travail")
        COMPTEUR += 1
        print(f"*** {COMPTEUR} tâche(s) terminée(s)")
        print("autotest : libération de caméra...")
        camera.release()
        print("autotest : libération de moteurs...")
        moteurs.release()


moteurs = Lock()
wifi = Lock()
camera = Lock()

# Création des threads
t1 = Thread(target=pilotage_manuel)
t2 = Thread(target=flux_video)
t3 = Thread(target=autotest)

# Lancement des threads
t1.start()
t2.start()
t3.start()

# Attente de la fin du travail
t1.join()
t2.join()
t3.join()
