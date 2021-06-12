from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageFont, ImageDraw
import pandas as pd
import os

class speakers():
    
    def __init__(self,master):
        self.f_n = []
        self.t_n = []

        self.pack_top = Frame(master, width=700, height=280)
        self.pack_top.pack(side=TOP)
        
        self.pack_bottom = Frame(master, width=700, height=400) 
        self.pack_bottom.pack(side=BOTTOM)

        
        self.heading = Label(master)
        self.heading = Label(master, text="Create Certificate for speaker", font = ('arial 20 bold'), fg ='green')
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
        
        open_file_flag = False
        while open_file_flag is False:
            for ic in invalid_characters:
                if ic in file_name:
                    invalid_char_input.append(ic)
                
            if len(invalid_char_input) > 0:
                tkinter.messagebox.showinfo('Error',"A file name can't contain any of the ff characters: \ / : ? > < | ")
                break
                #print("A file name can't contain any of the ff characters: \ / : ? > < | ")
                invalid_char_input.clear()
            else: invalid_char_input.clear()
                
            try:
                df = pd.read_csv("{}.csv".format(file_name))
                open_file_flag  = True
                self.f_n.append(file_name) #Appending to list
                self.show_template_button() #Showing the template objects
                
            except IOError as e:
                open_file_flag = False
                tkinter.messagebox.showinfo('Error',e)
                #create_speaker_cert()
                break
                #print(e)
            
    def show_template_button(self):


        #Text

        self.tempfile= Label(self.pack_top, text = "Input template filename:", font = ('arial 12 bold'))
        self.tempfile.place(x=25, y=120)
        #self.tempfile.pack()

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
        
        open_tempfile_flag = False
        while open_tempfile_flag is False:
            #speaker_fn = input(str("Filename of Speakers template (i.e, speakers_temp): "))
            for inc in invalid_characters:
                if inc in speaker_fn:
                    invalid_char_input.append(inc)
                
            if len(invalid_char_input) > 0:
                tkinter.messagebox.showinfo('Error',"A file name can't contain any of the ff characters: \ / : ? > < | ")
                break
                #print("A template file name can't contain any of the ff characters: \ / : ? > < | ")
                invalid_char_input.clear()
            else: invalid_char_input.clear()
        
            try:
                with open("{}.jpg".format(speaker_fn), 'r') as file:
                    open_tempfile_flag  = True
                    self.t_n.append(speaker_fn) #Appending to list
                    self.show_directory_button()
                    
                    
            except IOError as e:
                open_tempfile_flag = False
                tkinter.messagebox.showinfo('Error',e)
                break
                #print(e)
            
    def show_directory_button(self):
        #Text

        self.dir= Label(self.pack_top, text = "Output Directory:", font = ('arial 12 bold'))
        self.dir.place(x=25, y=165)

        #Text box

        #self.tempfile_entry =  Entry(self.pack_on_left, width = 25, font = ('arial 12 '))
        #self.tempfile_entry.place(x=250, y=120)

        #Button

        self.speci_file_button = Button(self.pack_top, text = "Specify", width = 10, height = 1, bg = 'green', fg='white', command = self.specify_dir)
        self.speci_file_button.place(x=250, y=165)

        self.gen_file_button = Button(self.pack_top, text = "Generate", width = 10, height = 1, bg = 'green', fg='white', command = self.gen_directory)
        self.gen_file_button.place(x=400, y=165)

    def specify_dir(self):

        #Text

        self.dir= Label(self.pack_top, text = "Input the directory path:", font = ('arial 12 bold'))
        self.dir.place(x=25, y=210)

        #Text box

        self.dir_path_entry =  Entry(self.pack_top, width = 25, font = ('arial 12 '))
        self.dir_path_entry.place(x=250, y=210)

        self.speci_enter_button = Button(self.pack_top, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.s_directory)
        self.speci_enter_button.place(x=500, y=210)

    def gen_directory(self):
        directory = os.getcwd()+'\Speakers'

        if not os.path.exists(os.getcwd()+'\Speakers'):
            os.makedirs(os.getcwd()+'\Speakers')

        self.cert_gen_speaker(directory)

    def s_directory(self):

        directory = self.dir_path_entry.get()
        self.cert_gen_speaker(directory)

    def cert_gen_speaker(self,directory):

        file_name = self.f_n[0]
        speaker_fn = self.t_n[0]

        scroll_barY = Scrollbar(self.pack_bottom,orient=VERTICAL)
        scroll_barX = Scrollbar(self.pack_bottom,orient=HORIZONTAL)
        
        listbox = Listbox(self.pack_bottom, height = 25,
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
            if row['Appreciation'] == 1:
                img = Image.open("{}.jpg".format(speaker_fn))
                draw = ImageDraw.Draw(img)
                name = row['Name']
                
                print("The number of characters of the name of the speaker are:",len(name))
                print("The number of characters of the topic of the speaker are:",len(row['Topic']))
                
                if len(name) > 30: # IF THE NAME HAS MORE THAN 30 CHARACTERS THEN USE 140pt FONT SIZE
                    draw.text(xy=(1873, 1101), text='{}'.format(row['Name']), fill=(0, 0, 0),
                              font=ImageFont.truetype('GOTHICB.ttf', 140), anchor='mm')

                    if len(row['Topic']) > 65: # IF THE TOPIC HAS MORE THAN 65 CHARACTERS THEN USE 70pt FONT SIZE
                        draw.text(xy=(1873, 1400), text='{}'.format(row['Topic']), fill=(0, 0, 0),
                                  font=ImageFont.truetype('GOTHICB.ttf', 70), anchor='mm')

                    else: # IF THE TOPIC HAS LESS THAN 65 CHARACTERS THEN USE 77pt FONT SIZE
                        draw.text(xy=(1873, 1400), text='{}'.format(row['Topic']), fill=(0, 0, 0),
                                  font=ImageFont.truetype('GOTHICB.ttf', 77), anchor='mm')
                        
                else: # IF THE NAME HAS LESS THAN 30 CHARACTERS THEN USE 160pt FONT SIZE
                    draw.text(xy=(1873, 1101), text='{}'.format(row['Name']), fill=(0, 0, 0),
                              font=ImageFont.truetype('GOTHICB.ttf', 160), anchor='mm')

                    if len(row['Topic']) > 65: # THE TOPIC HAS MORE THAN 65 CHARACTERS THEN USE 70pt FONT SIZE
                        draw.text(xy=(1873, 1400), text='{}'.format(row['Topic']), fill=(0, 0, 0),
                                  font=ImageFont.truetype('GOTHICB.ttf', 70), anchor='mm')
                        
                    else: # THE TOPIC HAS MORE THAN 65 CHARACTERS THEN USE 70pt FONT SIZE
                        draw.text(xy=(1873, 1400), text='{}'.format(row['Topic']), fill=(0, 0, 0),
                                  font=ImageFont.truetype('GOTHICB.ttf', 77), anchor='mm')
        
                if not os.path.exists(directory):
                    os.makedirs(directory)
                
                img.save("{}/{}.jpg".format(directory, name), format= 'JPEG')
                img.close()
                msg = "Appreciation certificate successfully saved, Filename: {} at {}".format(name, directory)
                print("Appreciation certificate successfully saved, Filename: {} at {}".format(name, directory))
                listbox.insert(END,msg)
                self.pack_bottom.update_idletasks()
 
                print("\n")

        
            



def create_speaker_cert(self,window):
        create_cert = speakers(window)
        #window.geometry("963x500+540+110")
        #window.title("Certificate Generator")
        #window.mainloop()
