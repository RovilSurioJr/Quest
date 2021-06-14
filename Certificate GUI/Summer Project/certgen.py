from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageFont, ImageDraw
import pandas as pd
import os



class Names():

    def __init__(self,master):
        self.f_n = []
        self.t_n = []
        self.font_n = []
        self.font_s = []

        self.pack_top = Frame(master, width=700, height=280)
        self.pack_top.pack(side=TOP)
        
        self.pack_bottom = Frame(master, width=700, height=400) 
        self.pack_bottom.pack(side=BOTTOM)


        self.heading = Label(master)
        self.heading = Label(master, text="Create Certificate", font = ('arial 20 bold'), fg ='green')
        self.heading.place(x=300,y=0)

        #Text

        self.excelfile= Label(master, text = "Input csv filename:", font = ('arial 12 bold'))
        self.excelfile.place(x=155, y=75)

        #Text box

        self.excelfile_entry =  Entry(master, width = 25, font = ('arial 12 '))
        self.excelfile_entry.place(x=380, y=75)

        #Button

        self.search_file_button = Button(master, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.check_excel_file)
        self.search_file_button.place(x=630, y=75)

    def check_excel_file(self):
        
        file_name = self.excelfile_entry.get()
        
        invalid_characters = ['/',':','?','<','>','|','\\']
        invalid_char_input = []
        
        for ic in invalid_characters:
            if ic in file_name:
                invalid_char_input.append(ic)
                
        if len(invalid_char_input) > 0:
            tkinter.messagebox.showinfo('Error',"A file name can't contain any of the ff characters: \ / : ? > < | ")
            invalid_char_input.clear()
        else: invalid_char_input.clear()
                
        try:
            df = pd.read_csv("{}.csv".format(file_name))
            self.f_n.append(file_name) #Appending to list
            self.show_template_button() #Showing the template objects
                
        except IOError as e:
            open_file_flag = False
            tkinter.messagebox.showinfo('Error',e)

            
    def show_template_button(self):

        #Text
        self.tempfile= Label(self.pack_top, text = "Input template filename:", font = ('arial 12 bold'))
        self.tempfile.place(x=25, y=120)

        #Text box

        self.tempfile_entry =  Entry(self.pack_top, width = 25, font = ('arial 12 '))
        self.tempfile_entry.place(x=250, y=120)

        #Button

        self.enter_file_button = Button(self.pack_top, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.check_template_file)
        self.enter_file_button.place(x=500, y=120)

    
    def check_template_file(self):

        speaker_fn = self.tempfile_entry.get()

        invalid_characters = ['/',':','?','<','>','|','\\']
        invalid_char_input = []
        
        for inc in invalid_characters:
            if inc in speaker_fn:
                invalid_char_input.append(inc)
                
        if len(invalid_char_input) > 0:
            tkinter.messagebox.showinfo('Error',"A file name can't contain any of the ff characters: \ / : ? > < | ")
            invalid_char_input.clear()
        else: invalid_char_input.clear()
        
        try:
            with open("{}.jpg".format(speaker_fn), 'r') as file:
                self.t_n.append(speaker_fn) #Appending to list
                self.show_font_style_button()
                        
        except IOError as e:
            tkinter.messagebox.showinfo('Error',e)

    def show_font_style_button(self):

        self.f_style= Label(self.pack_top, text = "Input font style filename:", font = ('arial 12 bold'))
        self.f_style.place(x=25, y=165)

        #Text box

        self.f_style_entry =  Entry(self.pack_top, width = 25, font = ('arial 12 '))
        self.f_style_entry.place(x=250, y=165)

        #Button

        self.f_style_button = Button(self.pack_top, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.font_style_choice)
        self.f_style_button.place(x=500, y=165)
           
    def font_style_choice(self):
        
        f_style_fn = self.f_style_entry.get()

        invalid_characters = ['/',':','?','<','>','|','\\']
        invalid_char_input = []
        
        for inc in invalid_characters:
            if inc in f_style_fn:
                invalid_char_input.append(inc)
                
        if len(invalid_char_input) > 0:
            tkinter.messagebox.showinfo('Error',"A file name can't contain any of the ff characters: \ / : ? > < | ")
            invalid_char_input.clear()
        else: invalid_char_input.clear()
        
        try:
            with open("{}.ttf".format(f_style_fn), 'r') as file:
                self.font_n.append(f_style_fn) #Appending to list
                self.show_font_size_button()
                        
        except IOError as e:
            tkinter.messagebox.showinfo('Error',e)

    def show_font_size_button(self):
        self.f_size= Label(self.pack_top, text = "Input font size(pixel):", font = ('arial 12 bold'))
        self.f_size.place(x=25, y=210)

        #Text box

        self.f_size_entry =  Entry(self.pack_top, width = 25, font = ('arial 12 '))
        self.f_size_entry.place(x=250, y=210)

        #Button

        self.f_size_button = Button(self.pack_top, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.font_size_c)
        self.f_size_button.place(x=500, y=210)

    def font_size_c(self):
        font_s = self.f_size_entry.get()

        try:
            int(font_s)
            self.font_s.append(int(font_s)*.75)
            self.show_directory_button()
            
            
        except ValueError:
            tkinter.messagebox.showinfo('Error',"Please input an integer")

        #if int(font_s) == ty
        
        
        #print(self.font_s)
        
 

    #self.show_directory_button()
    def show_directory_button(self):

        #Text

        self.dir= Label(self.pack_top, text = "Output Directory:", font = ('arial 12 bold'))
        self.dir.place(x=25, y=255)

        #Button

        self.speci_file_button = Button(self.pack_top, text = "Specify", width = 10, height = 1, bg = 'green', fg='white', command = self.specify_dir)
        self.speci_file_button.place(x=250, y=255)

        self.gen_file_button = Button(self.pack_top, text = "Generate", width = 10, height = 1, bg = 'green', fg='white', command = self.gen_directory)
        self.gen_file_button.place(x=400, y=255)

    def specify_dir(self):

        #Text

        self.dir= Label(self.pack_top, text = "Input the directory path:", font = ('arial 12 bold'))
        self.dir.place(x=25, y=300)

        #Text box
        self.dir_path_entry =  Entry(self.pack_top, width = 25, font = ('arial 12 '))
        self.dir_path_entry.place(x=250, y=300)

        self.speci_enter_button = Button(self.pack_top, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.s_directory)
        self.speci_enter_button.place(x=500, y=300)

    def gen_directory(self):
        directory = os.getcwd()+'\Speakers'

        if not os.path.exists(os.getcwd()+'\Speakers'):
            os.makedirs(os.getcwd()+'\Speakers')

        self.cert_gen_speaker(directory)

    def s_directory(self):

        directory = self.dir_path_entry.get()
        self.cert_gen_speaker(directory)

    def cert_gen_speaker(self,directory):

        file_name = self.f_n[-1]
        speaker_fn = self.t_n[-1]
        font_style = self.font_n[-1]
        font_size = int(self.font_s[-1])

        scroll_barY = Scrollbar(self.pack_bottom,orient=VERTICAL)
        scroll_barX = Scrollbar(self.pack_bottom,orient=HORIZONTAL)
        
        listbox = Listbox(self.pack_bottom, height = 10,
                          width = 115,
                          yscrollcommand = scroll_barY,
                          xscrollcomman = scroll_barX)

        scroll_barX.config(command = listbox.xview)
        scroll_barY.config(command = listbox.yview)
        scroll_barX.pack(side = BOTTOM, fill = X)
        scroll_barY.pack(side = RIGHT, fill = Y)

        listbox.pack()

        df = pd.read_csv("{}.csv".format(file_name))
        for index, row in df.iterrows():
            img = Image.open("{}.jpg".format(speaker_fn))
            draw = ImageDraw.Draw(img)
            name = row['Name']
    
                
            if len(name) > 30: # IF THE NAME HAS MORE THAN 30 CHARACTERS THEN USE 140pt FONT SIZE
                draw.text(xy=(1873, 1101), text='{}'.format(row['Name']), fill=(0, 0, 0),
                            font=ImageFont.truetype("{}.ttf".format(font_style), font_size), anchor='mm')

                    #"{}.jpg".format(speaker_fn)

                        
            else: # IF THE NAME HAS LESS THAN 30 CHARACTERS THEN USE 160pt FONT SIZE
                draw.text(xy=(1873, 1101), text='{}'.format(row['Name']), fill=(0, 0, 0),
                            font=ImageFont.truetype("{}.ttf".format(font_style), font_size), anchor='mm')
        
            if not os.path.exists(directory):
                os.makedirs(directory)
                
            img.save("{}/{}.jpg".format(directory, name), format= 'JPEG')
            img.close()
            msg = "Appreciation certificate successfully saved, Filename: {} at {}".format(name, directory)
            print("Appreciation certificate successfully saved, Filename: {} at {}".format(name, directory))
            listbox.insert(END,msg)
            self.pack_bottom.update_idletasks()
 
            print("\n")


#def create_cert(self,window):
    #create_cert = Names(window)

window = Tk()
main = Names(window)
window.geometry("963x500+540+110")
window.title("Certificate Generator")
window.mainloop()
