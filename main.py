#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

import os
import tkinter

def ouvrir_app():
    os.system("/home/erhelito/Documents/programmation/python/automatisation_démarrage/ouverture.sh")

fenetre = tkinter.Tk()
label = tkinter.Label(fenetre, text = "Lancer les applications ?")
label.pack()

bouton1 = tkinter.Button(fenetre, text = "oui", command = ouvrir_app)
bouton1.pack()

bouton2 = tkinter.Button(fenetre, text = "non", command = fenetre.quit)
bouton2.pack()

fenetre.mainloop()
