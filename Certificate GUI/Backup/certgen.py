from tkinter import *
import tkinter.messagebox
import os
from PIL import Image, ImageFont, ImageDraw
import pandas as pd

import speakers as sp
import participants as ps


class Main():
    def __init__(self,master):

        self.Button1 = Button(master, text = "Speaker", width = 10, height = 1, bg = 'green',fg='white',  command=lambda:[self.delete_widget(),sp.create_speaker_cert(self,window)])
        self.Button1.place(x=155, y=75)

        self.Button2 = Button(master,text = "Participants", width = 10, height = 1, bg = 'green',fg='white', command=lambda:[self.delete_widget(),ps.create_participants_cert(self,window)])
        self.Button2.place(x=500, y=75)
                              
    def delete_widget(self):
        self.Button1.destroy()
        self.Button2.destroy()



        
window = Tk()
main = Main(window)
window.geometry("963x500+540+110")
window.title("Certificate Generator")
window.mainloop()



