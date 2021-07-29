from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageFont, ImageDraw
import pandas as pd
import os
from tkinter import filedialog


class Names():
    def __init__(self,master):

        self.f_n = [] #filename
        self.file_t_choice = [] #filetype
        self.t_n = [] #templatename
        self.img_type_choice = [] #chosen filetype img

        self.pack_top = Frame(master, width=963, height=450 ,bg = 'white')
        self.pack_top.pack(side=TOP)
        
        self.pack_bottom = Frame(master, width=700, height=400) 
        self.pack_bottom.pack(side=BOTTOM)


        self.heading = Label(master)
        self.heading = Label(master, text="Create Certificate", font = ('arial 20 bold'), fg ='green')
        self.heading.place(x=375,y=0)


        #Text
        self.excelfile= Label(master, text = "Input source filename:", font = ('arial 12 bold'))
        self.excelfile.place(x=120, y=75)

        #Text box
        self.excelfile_entry =  Entry(master, width = 25, font = ('arial 12 '))
        self.excelfile_entry.place(x=340, y=75)


        self.search_browse_button = Button(master, text = "Browse", width = 10, height = 1, bg = 'green', fg='white', command = self.browseFiles)
        self.search_browse_button.place(x=767, y=72)

        file_type_choices = ['csv','txt']
        self.file_type_choice = ttk.Combobox(master, value = file_type_choices,width =10)
        self.file_type_choice.current(0)
        self.file_type_choice.bind("<<ComboboxSelected>>", self.combo_click1)
        self.file_type_choice.place(x=590, y=75)
        self.file_t_choice.append('csv')

    def browseFiles(self):
        
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("csv files",
                                                        "*.csv*"),
                                                       ("text files",
                                                        "*.txt*")))

        try:
            self.excelfile_entry.delete(0,END)
        except: pass
        
        if len(filename) == 0:
            tkinter.messagebox.showinfo('Error',"You haven't selected any file upon browsing")
            print(self.file_t_choice)

        else:
            file_path = os.path.splitext(filename)[0]
            file_name = file_path.split('/')[-1]
            self.f_n.append(file_name)
            print(file_name)
        
            file_ext = os.path.splitext(filename)[1]
            final_ext = file_ext.split('.')[-1]
            self.file_t_choice.append(final_ext)
            print(final_ext)
            
            self.excelfile_entry.insert(0, "{}".format(filename))
            self.show_template_button()

        
        #print(os.path.basename(filename))
            
    def combo_click1(self,file_type_choice):
        if self.file_type_choice.get() == 'txt':
            self.file_t_choice.append('txt')
            print("txt")
        else:
            self.file_t_choice.append('csv')
            print("csv")


    def show_template_button(self):

        #Text
        self.tempfile= Label(self.pack_top, text = "Input template filename:", font = ('arial 12 bold'))
        self.tempfile.place(x=120, y=120)

        #Text box

        self.tempfile_entry =  Entry(self.pack_top, width = 25, font = ('arial 12 '))
        self.tempfile_entry.place(x=340, y=120)


        img_type = ['jpg','PNG']
        self.img_type_choices = ttk.Combobox(self.pack_top, value = img_type,width =10)
        self.img_type_choices.current(0)
        self.img_type_choices.bind("<<ComboboxSelected>>", self.combo_click2)
        self.img_type_choices.place(x=592, y=123)
        self.img_type_choice.append('jpg')

        self.search_browse_button2 = Button(self.pack_top, text = "Browse", width = 10, height = 1, bg = 'green', fg='white', command = self.browseFilesTemplate)
        self.search_browse_button2.place(x=767, y=120)

    def browseFilesTemplate(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("JPEG",
                                                        "*.jpg*"),
                                                       ("PNG",
                                                        "*.PNG*")))
        try:
            self.tempfile_entry.delete(0,END)
        except: pass

        if len(filename) == 0:
            tkinter.messagebox.showinfo('Error',"You haven't selected any file upon browsing")

        else:
            
            file_path = os.path.splitext(filename)[0]
            file_name = file_path.split('/')[-1]
            self.t_n.append(file_name)
            print(file_name)
        
            file_ext = os.path.splitext(filename)[1]
            final_ext = file_ext.split('.')[-1]
            self.img_type_choice.append(final_ext)
            print(final_ext)


            self.tempfile_entry.insert(0, "{}".format(filename))
            self.show_font_style_button()

    def combo_click2(self,img_type_choices):
        if self.img_type_choices.get() == 'jpg':
            self.img_type_choice.append('jpg')
            print("jpg")
        else:
            self.img_type_choice.append('PNG')
            print("PNG")



window = Tk()
main = Names(window)
window.geometry("963x600+540+110")
window.title("Certificate Generator")
window.resizable(width=False, height=False)
window.mainloop()
