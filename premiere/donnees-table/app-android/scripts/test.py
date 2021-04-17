import csv
# charge le fichier dans le programme
fichier = open("googleplaystore.csv")
# crée un itérateur sur les données
lecteur_donnees = csv.DictReader(fichier)

table = []
for ligne in lecteur_donnees:
    dico = {}
    for nom, val in ligne.items():
        # validation des données
        if nom == "Rating":
            val = float(val)
        if nom == "Installs" or nom == "Reviews":
            val = int(val)

        dico[nom] = val
    table.append(dico)