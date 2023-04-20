import tkinter
from tkinter import *
from tkinter import filedialog
import os
import pygame.mixer_music


class main :
    def __init__(self):
        self.app= Tk() ##Constructeur de la class Tkinter
        self.app.title("MP3 player") ## Titre de l'application
        self.app.geometry("500x300") ## Dimension de l'application
        self.button_position=[(340,200),(200,100)] ## Position des bouton
        self.song_list=[] ## Liste des chansons contenu dans la répertoire
        self.song_directory=None ##Chemin d'accès au répertoire
    def add_button(self,texte:str):

        return tkinter.Button(self.app,text=texte,command=self.set_song_folder)
    def set_position_button(self,bouton:Button,x:int,y:int):
        bouton.place(x=x,y=y)
    def play(self):
        pass
    def stop(self):
        pass
    def set_list_song(self):
        for file in os.listdir(self.song_directory):
            print(file)
            if file.endswith(".mp3"):
                self.song_list.append(file)

    def test(self):
        print("test validé")
    def set_song_folder(self):
        self.song_directory=filedialog.askdirectory()
        self.set_list_song()
    def set_command_button(self,bouton:Button,methode):
        bouton.configure(command=methode)
    def set_all(self):
        button1=self.add_button("open")
        self.set_position_button(button1,100,110)
    def main(self):
        self.set_all()
        self.app.mainloop()



