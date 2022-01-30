import tkinter
from tkinter import ttk

fenetre = tkinter.Tk()
fenetre.title("Pokemon Go")

label_nom = tkinter.Label(fenetre)
label_nom.grid(column=0, row=0)
label_nom["text"] = "Bulbasaur"

label_poids = tkinter.Label(fenetre)
label_poids.grid(column=0, row=1)
label_poids["text"] = "6.9kg"

label_taille = tkinter.Label(fenetre)
label_taille.grid(column=1, row=1)
label_taille["text"] = "0.71m"

# dernière ligne du programme: met à jour les variables 
fenetre.mainloop()