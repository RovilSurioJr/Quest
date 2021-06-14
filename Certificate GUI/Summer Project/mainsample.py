from tkinter import *
import tkinter.messagebox
import os
from PIL import Image, ImageFont, ImageDraw
import pandas as pd
import names as nm




class Main():
    def __init__(self,master):

        self.Button1 = Button(master, text = "Start", width = 10, height = 1, bg = 'green',fg='white',  command=lambda:[self.delete_widget(),nm.create_cert(self,window)])
        self.Button1.place(x=155, y=75)


    def delete_widget(self):
        self.Button1.destroy()



window = Tk()
main = Main(window)
window.geometry("963x500+540+110")
window.title("Certificate Generator")
window.mainloop()
