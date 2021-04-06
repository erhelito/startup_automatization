#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

import os
import tkinter

path = os.path.abspath(".")
commande = str("cd " + path)

def installation():
    fenetre.quit
    os.system(commande)
    os.system("chmod a+x launching.sh")
    os.system("chmod a+x main.py")
    os.system("killall installation.py.py && killall python")

fenetre = tkinter.Tk()
label = tkinter.Label(fenetre, text = "Install ?")
label.pack()

bouton1 = tkinter.Button(fenetre, text = "yes", command = installation)
bouton1.pack()

bouton2 = tkinter.Button(fenetre, text = "no", command = fenetre.quit)
bouton2.pack()

fenetre.mainloop()
