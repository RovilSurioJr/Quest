
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageFont, ImageDraw
import pandas as pd
import os


class participants():
    
    def __init__(self,master):
        self.f_n = []
        self.t_n = []
        self.session_choice = []

        self.master = master

        self.pack_top = Frame(master, width=700, height=280) # Frames
        self.pack_top.pack(side=TOP)
        
        self.pack_bottom = Frame(master, width=700, height=400) #The remaining width
        self.pack_bottom.pack(side=BOTTOM)

        
        self.heading = Label(master)
        self.heading = Label(master, text="Create Certificate for participants", font = ('arial 20 bold'), fg ='green')
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
                break

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

        temp_fn = self.tempfile_entry.get()

        invalid_characters = ['/',':','?','<','>','|','\\']
        invalid_char_input = []
        
        open_tempfile_flag = False
        while open_tempfile_flag is False:
            for inc in invalid_characters:
                if inc in temp_fn:
                    invalid_char_input.append(inc)
                
            if len(invalid_char_input) > 0:
                tkinter.messagebox.showinfo('Error',"A file name can't contain any of the ff characters: \ / : ? > < | ")
                break
                invalid_char_input.clear()
            else: invalid_char_input.clear()
        
            try:
                with open("{}.jpg".format(temp_fn), 'r') as file:
                    open_tempfile_flag  = True
                    self.t_n.append(temp_fn) #Appending to list
                    self.show_session_button()
                    
                    
            except IOError as e:
                open_tempfile_flag = False
                tkinter.messagebox.showinfo('Error',e)
                break
                #print(e)
            

 
    def show_session_button(self):

        #Text
        self.dir= Label(self.pack_top, text = "Choose session:", font = ('arial 12 bold'))
        self.dir.place(x=25, y=165)

        s_choice = ['AM','PM']
        self.session_choices = ttk.Combobox(self.pack_top, value = s_choice,width =10)
        self.session_choices.bind("<<ComboboxSelected>>", self.combo_click)
        self.session_choices.place(x=250, y=165)


    def combo_click(self,session_choices):
        if session_choices.widget.get() == 'AM':
            self.session_choice.append('AM')
            self.show_directory_button()
            print("AM")
        else:
            self.session_choice.append('PM')
            self.show_directory_button()
            print("PM")


    def show_directory_button(self):

        self.dir= Label(self.pack_top, text = "Output Directory:", font = ('arial 12 bold'))
        self.dir.place(x=25, y=210)

        self.speci_file_button = Button(self.pack_top, text = "Specify", width = 10, height = 1, bg = 'green', fg='white', command = self.specify_dir)
        self.speci_file_button.place(x=250, y=210)

        self.gen_file_button = Button(self.pack_top, text = "Generate", width = 10, height = 1, bg = 'green', fg='white', command = self.gen_directory)
        self.gen_file_button.place(x=400, y=210)


    def specify_dir(self):

        #Text

        self.dir= Label(self.pack_top, text = "Input the directory path:", font = ('arial 12 bold'))
        self.dir.place(x=25, y=255)

        #Text box

        self.dir_path_entry =  Entry(self.pack_top, width = 25, font = ('arial 12 '))
        self.dir_path_entry.place(x=250, y=255)

        self.speci_enter_button = Button(self.pack_top, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.s_directory)
        self.speci_enter_button.place(x=500, y=255)

    def s_directory(self):

        directory = self.dir_path_entry.get()
        self.cert_gen_partici(directory)

    def gen_directory(self):

        if self.session_choice[-1] == 'AM':
            directory = os.getcwd()+'\AM_Participants'

        else:
            directory = os.getcwd()+'\PM_Participants'

        if not os.path.exists(os.getcwd()+'\AM_Participants'):
            os.makedirs(os.getcwd()+'\AM_Participants')

        if not os.path.exists(os.getcwd()+'\PM_Participants'):
            os.makedirs(os.getcwd()+'\PM_Participants')

        self.cert_gen_partici(directory)


    def cert_gen_partici(self,directory):
        
        if self.session_choice[-1] == 'AM':
            self.cert_gen_am_participants(directory)

        else:
            self.cert_gen_pm_participants(directory)
            

    def cert_gen_am_participants(self,directory):
        file_name = self.f_n[-1]
        temp_fn = self.t_n[-1]
        
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



        #display.place(x=100, y=300)
        
        df = pd.read_csv("{}.csv".format(file_name))
        for index, row in df.iterrows():
            if row['AM Participation'] == 1:
                img = Image.open("{}.jpg".format(temp_fn))
                draw = ImageDraw.Draw(img)
                draw.text(xy=(1873, 1101), text='{}'.format(row['Name']), fill=(0, 0, 0),
                          font=ImageFont.truetype('GOTHICB.ttf', 160), anchor='mm')

                if not os.path.exists(directory):
                    os.makedirs(directory)
                name = row['Name']
                img.save("{}/{}.jpg".format(directory, name), format= 'JPEG')
                img.close()
                A = "AM Participants certificate successfully saved, Filename: {} at {}".format(name, directory)
                print("AM Participants certificate successfully saved, Filename: {} at {}".format(name, directory))
                listbox.insert(END,A)
                self.pack_bottom.update_idletasks()
                
                print("\n")

    def cert_gen_pm_participants(self,directory):

        file_name = self.f_n[-1]
        temp_fn = self.t_n[-1]
        
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
            if row['PM Participation'] == 1:
                img = Image.open("{}.jpg".format(temp_fn))
                draw = ImageDraw.Draw(img)
                draw.text(xy=(1873, 1101), text='{}'.format(row['Name']), fill=(0, 0, 0),
                          font=ImageFont.truetype('GOTHICB.ttf', 160), anchor='mm')
                if not os.path.exists(directory):
                    os.makedirs(directory)
                name = row['Name']
                img.save("{}/{}.jpg".format(directory, name), format= 'JPEG')
                img.close()
                A = "PM Participants certificate successfully saved, Filename: {} at {}".format(name, directory)
                print("PM Participants certificate successfully saved, Filename: {} at {}".format(name, directory))
                listbox.insert(END,A)
                self.pack_bottom.update_idletasks()
                
                print("\n")

def create_participants_cert():
        window = Tk()
        create_cert = participants(window)
        window.geometry("963x500+540+110")
        window.title("Certificate Generator")
        window.mainloop()
