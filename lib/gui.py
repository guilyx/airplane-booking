"""
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 14/02/2020
@brief : airplane reservation gui
"""

import tkinter as tk


class Interface(tk.Frame):
    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=tk.BOTH)
        self.nb_clic = 0

        # Création de nos widgets
        self.message = tk.Label(self, text="Vous n'avez pas cliqué sur le bouton.")
        self.message.pack()

        self.bouton_quitter = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")

        self.bouton_cliquer = tk.Button(
            self, text="Cliquez ici", fg="red", command=self.cliquer
        )
        self.bouton_cliquer.pack(side="right")

    def cliquer(self):

        self.nb_clic += 1
        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)

