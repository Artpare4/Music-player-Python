import tkinter
from tkinter import *
from tkinter import filedialog
import os
from pydoc import *
from pydub import AudioSegment,playback

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
        self.listbox_musique=Listbox(selectmode="select") ## liste de choix des musique disponible
        self.full_song_directory=None ## concaténation du chemin d'accès au répertoire (song_directory) + le nom du titre
        self.play_obj=None
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
        song=self.listbox_musique.get(self.listbox_musique.curselection())
        if self.full_song_directory!=None:
            self.play_obj.stop()
            self.full_song_directory=self.song_directory+"/"+song
            music=AudioSegment.from_file(self.full_song_directory)
            self.play_obj = playback._play_with_simpleaudio(music)
        else:

            self.full_song_directory=self.song_directory+"/"+song
            music = AudioSegment.from_file(self.full_song_directory)
            self.play_obj = playback._play_with_simpleaudio(music)

    def stop(self):
        """
        Méthode de la classe main. Cette méthode stop la musique choise par l'utilisateur.
        :return:
        """
        self.play_obj.stop()
    def set_empty_list_song(self):
        """
        Méthode de la classe main. Cette méthode permet de vider la liste des titres des chansons disponible dans le répertoire.
        :return:
        """
        self.song_list=[]
    def set_list_song(self):
        """
        Méthode de la classe main. Cette méthode permet de récupérer tous le fichiers .mp3 ou.wav du dossier choisi par l'utilisateur sous forme d'une liste.
        Ne retoune rien et ne prend pas de paramètre.
        :return:
        """
        for file in os.listdir(self.song_directory):
            if file.endswith(".mp3") or file.endswith(".wav"):
                self.song_list.append(file)

    def set_song_choice(self):
        """
        Méthode de la classe main. Cette méthode récupère le chemin d'accès au dossier choisi par l'utilisateur
        et met à jour la liste de chanson disponible (que l'utilisateur peut écouter).
        :return:
        """
        self.song_directory=filedialog.askdirectory() ## on demande le chemin d'accès au répertoire
        self.set_empty_list_song() ## suppression du contenu de la liste de chanson
        self.listbox_musique.delete(0,"end") ## suppression du contenu de la listebox
        self.set_list_song() ## On ajoute à la liste de chanson disponible tous les sons de dossier
        self.add_musique_listbox(self.listbox_musique) ##Ajout de la liste de musique dans la listbox

    def set_command_button(self,bouton:Button,methode):
        """
        Méthode de la classe main. Cette méthode prend en paramètre un bouton et une méthode et ajoute cette commande dans l'action du bouton quand il est cliqué.

        :param bouton:
        :param methode:
        :return:
        """
        bouton.configure(command=methode)

    def add_musique_listbox(self,listbox:Listbox):
        """
        Méthode de la classe main. Cette méthode ajoute tous les titres des chansons disponible dans la listbox.
        :param listbox:
        :return:
        """
        for song in self.song_list:
            listbox.insert("end",song)

    def set_all(self):
        """
        Méthode de la classe main. Cette méthode permet de tout initialiser (boutons, liste,...) avant de lancer le programme.
        Ne prend pas de paramètre et ne retourn rien.
        :return:
        """
        # Bouton de recherche de dossier
        #button1=self.add_button("open")
        #self.set_position_button(button1,100,110)
        #self.set_command_button(button1,self.set_song_folder)
        button1=Button(self.app,text="Ouvrir")
        button1.place(x=100,y=100)
        button1.configure(command=self.set_song_choice)
        ## bouton play
        button_play=Button(self.app,text="Play",command=self.play)
        button_play.place(x=50,y=50)
        ## bouton pause
        button_pause=Button(self.app,text="Pause",command=self.stop)
        button_pause.place(x=50,y=100)
        ## mise en place listebox
        self.listbox_musique.place(x=200,y=200)

        ## première recherche dans un répertoire (quand on lance l'appli)
        self.set_song_choice()
        self.add_musique_listbox(self.listbox_musique)
    def test(self):
        print("test Validé")
    def main(self):
        """
        Méthode de la classe main. Cette méthode permet d'exécuter l'application.
        :return:
        """
        self.set_all()
        self.app.mainloop()



