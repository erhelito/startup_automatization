#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

import os
import tkinter

def ouvrir_app():
    os.system("the_path_to_launching.sh_file")

fenetre = tkinter.Tk()
label = tkinter.Label(fenetre, text = "Launch applications ?")
label.pack()

bouton1 = tkinter.Button(fenetre, text = "yes", command = ouvrir_app)
bouton1.pack()

bouton2 = tkinter.Button(fenetre, text = "no", command = fenetre.quit)
bouton2.pack()

fenetre.mainloop()
