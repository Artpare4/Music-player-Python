import tkinter
from tkinter import *
from tkinter import filedialog
import os
import pygame.mixer_music
from pydoc import *

class main :
    def __init__(self):
        """
        Constructeur de la classe main. Ce constructeur ne prend pas de paramètre et créer une instance de la classe main.
        Ce contructeur appel le constructeur de Tkinter pour créer une application tkinter.
        """
        self.app= Tk() ##Constructeur de la class Tkinter
        self.app.title("MP3 player") ## Titre de l'application
        self.app.geometry("500x300") ## Dimension de l'application
        self.button_position=[(340,200),(200,100)] ## Position des bouton
        self.song_list=[] ## Liste des chansons contenu dans la répertoire que l'utilisateur peut choisir
        self.song_directory=None ##Chemin d'accès au répertoire

    def add_button(self,texte:str):
        """
        Méthode de la classe main. Cette méthode permet de créer un bouton avec un texte associé passé un paramètre.
        :param texte: Texte du bouton
        :return: Un bouton
        """
        return tkinter.Button(self.app,text=texte)

    def set_position_button(self,bouton:Button,x:int,y:int):
        """
        Méthode de la classe main. Cette méthode prend en paramètre un bouton, et deux entiers et modifie l'emplacement du bouton par les valeurs passé en paramètre.
        :param bouton: Bouton dont on doit modifer l'emplacement
        :param x: Position sur l'axe x (en pixel)
        :param y: Position sur l'axe y (en pixel)
        :return: Rien
        """
        bouton.place(x=x,y=y)

    def play(self):
        """
        Méthode de la classe main. Cette méthode active et joue la musique choise par l'utilisateur.
        :return:
        """
        pass
    def stop(self):
        """
        Méthode de la classe main. Cette méthode stop la musique choise par l'utilisateur.
        :return:
        """
        pass
    def set_empty_list_song(self):
        """

        :return:
        """
        self.song_list=[]
    def set_list_song(self):
        """
        Méthode de la classe main. Cette méthode permet de récupérer tous le fichiers .mp3 du dossier choisi par l'utilisateur sous forme d'une liste.
        Ne retoune rien et ne prend pas de paramètre.
        :return:
        """
        for file in os.listdir(self.song_directory):
            if file.endswith(".mp3"):
                self.song_list.append(file)
    def set_song_folder(self):
        """
        Méthode de la classe main. Cette méthode récupère le chemin d'accès au dossier choisi par l'utilisateur
        et met à jour la liste de chanson disponible (que l'utilisateur peut écouter).
        :return:
        """
        self.song_directory=filedialog.askdirectory()
        self.set_empty_list_song()
        self.set_list_song()
    def set_command_button(self,bouton:Button,methode):
        """
        Méthode de la classe main. Cette méthode prend en paramètre un bouton et une méthode et ajoute cette commande dans l'action du bouton quand il est cliqué.

        :param bouton:
        :param methode:
        :return:
        """
        bouton.configure(command=methode)

    def set_all(self):
        """
        Méthode de la classe main. Cette méthode permet de tout initialiser (boutons, liste,...) avant de lancer le programme.
        Ne prend pas de paramètre et ne retourn rien.
        :return:
        """
        button1=self.add_button("open")
        self.set_position_button(button1,100,110)
        self.set_command_button(button1,self.set_song_folder)

    def test(self):
        print("test Validé")

    def main(self):
        """
        Méthode de la classe main. Cette méthode permet d'exécuter l'application.
        :return:
        """
        self.set_all()
        self.app.mainloop()



