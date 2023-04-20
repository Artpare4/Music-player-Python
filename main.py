import tkinter
from tkinter import *
class main :
    def __init__(self):
        self.app= Tk()
        self.app.title("MP3 player")
        self.app.geometry("500x300")
        self.button_position=[(340,200),(200,100)]
    def add_button(self,texte:str):
        return tkinter.Button(self.app,text=texte)
    def set_position_button(self,bouton:Button,x:int,y:int):
        bouton.place(x=x,y=y)


    def set_all(self):
        button1=self.add_button("test")
        self.set_position_button(button1,100,110)

    def main(self):
        self.set_all()
        self.app.mainloop()



