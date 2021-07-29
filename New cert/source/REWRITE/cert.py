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

        self.session_chosen = [] #selected session/topic
        self.font_name = [] #selected font

        self.font_s_name = [] #name font size
        self.font_s_session = [] #session font size

        self.x_coor_name = [] #X_coordinates
        self.y_coor_name = [] #Y_coordinates

        self.x_coor_session = [] #X_coordinates
        self.y_coor_session = [] #Y_coordinates

        self.generate = False
        self.widget_column_name_exist = False
        
        self.pack_top = Frame(master, width=963, height=550 ,bg = 'white')
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
            self.show_list_of_sessions() ##

    def combo_click2(self,img_type_choices):
        if self.img_type_choices.get() == 'jpg':
            self.img_type_choice.append('jpg')
            print("jpg")
        else:
            self.img_type_choice.append('PNG')
            print("PNG")

    def show_list_of_sessions(self):

        
        self.session_choice= Label(self.pack_top, text = "Select the session:", font = ('arial 12 bold'))
        self.session_choice.place(x=120, y=165)


        file_name = self.f_n[-1]
        sessions_list = []
        
        df = pd.read_csv("{}.csv".format(file_name))
        for row in df['Sessions'].dropna():
            sessions_list.append(row)

        
        self.session_choices = ttk.Combobox(self.pack_top, value = sessions_list,width =50)
        self.session_choices.current(0)
        self.session_choices.bind("<<ComboboxSelected>>", self.combo_click3)
        self.session_choices.place(x=340, y=168)
        self.session_chosen.append(sessions_list[0])


    def combo_click3(self,session_choices):
        self.session_chosen.append(self.session_choices.get())
        print(self.session_chosen[-1])
        self.show_font_style_button()

    def show_font_style_button(self):


        self.f_style= Label(self.pack_top, text = "Input font style filename:", font = ('arial 12 bold'))
        self.f_style.place(x=120, y=210)

        #Text box

        self.f_style_entry =  Entry(self.pack_top, width = 25, font = ('arial 12 '))
        self.f_style_entry.place(x=340, y=210)

        #Button

        self.search_browse_button3 = Button(self.pack_top, text = "Browse", width = 10, height = 1, bg = 'green', fg='white', command = self.browseFilesFont)
        self.search_browse_button3.place(x=680, y=210)

    def browseFilesFont(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = [("TTF",
                                                        "*.ttf*")])
        try:
            self.f_style_entry.delete(0,END)
        except: pass

        if len(filename) == 0:
            tkinter.messagebox.showinfo('Error',"You haven't selected any file upon browsing")

        else:
            
            file_path = os.path.splitext(filename)[0]
            file_name = file_path.split('/')[-1]
            self.font_name.append(file_name)
            print(self.font_name)
        
            self.f_style_entry.insert(0, "{}".format(filename))
            self.show_font_size_button()

    def show_font_size_button(self):
        self.f_size= Label(self.pack_top, text = "Input name & session font size(pt):", font = ('arial 12 bold'))
        self.f_size.place(x=120, y=255)

        #Text box

        self.f_size_entry =  Entry(self.pack_top, width = 5, font = ('arial 12 '))
        self.f_size_entry.place(x=400, y=255)

        #Button

        #self.f_size_button = Button(self.pack_top, text = "<-- Name", width = 8, height = 1, bg = 'green', fg='white', command = self.font_size_name)
        #self.f_size_button.place(x=400, y=255)

        #self.f_size_button = Label(self.pack_top, text = "Name", font = ('arial 9 italic'))
        #self.f_size_button.place(x=340, y=285)

        self.f_size_t_entry =  Entry(self.pack_top, width = 5, font = ('arial 12 '))
        self.f_size_t_entry.place(x=500, y=255)

        self.f_size_t_button = Button(self.pack_top, text = "Enter", width = 8, height = 1, bg = 'green', fg='white', command = self.font_size_choice)
        self.f_size_t_button.place(x=560, y=255)

        self.default_fs_button = Button(self.pack_top, text = "Default", width = 8, height = 1, bg = 'green', fg='white', command = self.default_font_size_but)
        self.default_fs_button.place(x=660, y=255)

    def default_font_size_but(self):

        #try:
            #self.f_size_entry.delete(0,END)
            #self.f_size_t_entry.delete(0,END)
        #except: pass

        self.f_size_entry.delete(0,END)
        self.f_size_t_entry.delete(0,END)
        self.f_size_entry.insert(0, "46")
        self.f_size_t_entry.insert(0, "23")


        font_s_def = self.f_size_entry.get()
        font_si_def = self.f_size_t_entry.get()
        int(font_s_def)
        int(font_si_def)
        self.font_s_name.append(font_s_def)
        self.font_s_session.append(font_si_def)        
        self.show_imgsize_button()

    def font_size_choice(self):
        
        font_s = self.f_size_entry.get()
        font_si = self.f_size_t_entry.get()

        try:
            int(font_s)
            int(font_si)
            self.font_s_name.append(font_s)
            self.font_s_session.append(font_si)
            self.show_imgsize_button()
            tkinter.messagebox.showinfo('Confirmation',"Font size updated!")

            print(self.font_s_name)
            print(self.font_s_session)
            
            
        except ValueError:
            tkinter.messagebox.showinfo('Error',"Please input an integer")

    def show_imgsize_button(self):

        template_fn = self.t_n[-1]
        image_type = self.img_type_choice[-1]
        
        self.img_s= Label(self.pack_top, text = "X & Y for placement of names:", font = ('arial 12 bold'))
        self.img_s.place(x=120, y=300)
        self.img_sz_note= Label(self.pack_top, text = "*The default is at center of the image", font = ('arial 9 italic'))
        self.img_sz_note.place(x=350, y=320)

        img = Image.open("{}.{}".format( template_fn,image_type))
        lxw = img.size
        length= lxw[0] // 2
        width = lxw[1] //2
        
        self.X_val_entry =  Entry(self.pack_top, width = 6, font = ('arial 12'))
        self.X_val_entry.place(x=390, y=300)
        self.X_val_entry.insert(0, "{}".format(length))

        self.Y_val_entry =  Entry(self.pack_top, width = 6, font = ('arial 12'))
        self.Y_val_entry.place(x=480, y=300)
        self.Y_val_entry.insert(0, "{}".format(width))

        self.proceed_button = Button(self.pack_top, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.check_coordinates_input )
        self.proceed_button.place(x=590, y=300)

    def check_coordinates_input(self):
        l = self.X_val_entry.get()
        w = self.Y_val_entry.get()

        try:
            
            X_img = int(l)
            Y_img = int(w)
            self.x_coor_name.append(X_img)
            self.y_coor_name.append(Y_img)

            self.show_imgsize_button_session()
            
        except ValueError:
            tkinter.messagebox.showinfo('Error',"Please input an integer")

    def show_imgsize_button_session(self):

        template_fn = self.t_n[-1]
        image_type = self.img_type_choice[-1]
        
        self.img_s= Label(self.pack_top, text = "X & Y for placement of sessions:", font = ('arial 12 bold'))
        self.img_s.place(x=120, y=345)
        self.img_sz_note= Label(self.pack_top, text = "*The default is at center of the image", font = ('arial 9 italic'))
        self.img_sz_note.place(x=350, y=365)

        img = Image.open("{}.{}".format( template_fn,image_type))
        lxw = img.size
        length= lxw[0] // 2
        width = lxw[1] //2
        
        self.X_val_entry_2 =  Entry(self.pack_top, width = 6, font = ('arial 12'))
        self.X_val_entry_2.place(x=390, y=345)
        self.X_val_entry_2.insert(0, "{}".format(length))

        self.Y_val_entry_2 =  Entry(self.pack_top, width = 6, font = ('arial 12'))
        self.Y_val_entry_2.place(x=480, y=345)
        self.Y_val_entry_2.insert(0, "{}".format(width))

        self.proceed_button = Button(self.pack_top, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.check_coordinates_input_2 )
        self.proceed_button.place(x=590, y=345)

    def check_coordinates_input_2(self):
        l = self.X_val_entry_2.get()
        w = self.Y_val_entry_2.get()

        try:
            
            X_img = int(l)
            Y_img = int(w)
            self.x_coor_session.append(X_img)
            self.y_coor_session.append(Y_img)

            self.show_directory_button()
            
        except ValueError:
            tkinter.messagebox.showinfo('Error',"Please input an integer")

    def show_directory_button(self):

        #Text

        self.dir= Label(self.pack_top, text = "Output Directory:", font = ('arial 12 bold'))
        self.dir.place(x=120, y=390)

        #Button

        self.speci_file_button = Button(self.pack_top, text = "Specify", width = 10, height = 1, bg = 'green', fg='white', command = self.specify_dir)
        self.speci_file_button.place(x=390, y=390)

        self.gen_file_button = Button(self.pack_top, text = "Generate", width = 10, height = 1, bg = 'green', fg='white', command = self.gen_directory)
        self.gen_file_button.place(x=480, y=390)

    def specify_dir(self):
        if self.file_t_choice[-1] == 'csv':
            self.generate = False
            self.dir1= Label(self.pack_top, text = "Input the directory path:", font = ('arial 12 bold'))
            self.dir1.place(x=120, y=435)

            self.dir_path_entry1 =  Entry(self.pack_top, width = 25, font = ('arial 12'))
            self.dir_path_entry1.place(x=340, y=435)

            self.locate_folder_button = Button(self.pack_top, text = "Browse", width = 10, height = 1, bg = 'green', fg='white', command = self.locate_folder_dir)
            self.locate_folder_button.place(x=680, y=435)

            

        else:
            self.dir= Label(self.pack_top, text = "Input the directory path:", font = ('arial 12 bold'))
            self.dir.place(x=120, y=435)
            
            self.dir_path_entry =  Entry(self.pack_top, width = 25, font = ('arial 12'))
            self.dir_path_entry.place(x=340, y=435)

            self.locate_folder_button1 = Button(self.pack_top, text = "Browse", width = 10, height = 1, bg = 'green', fg='white', command = self.locate_folder_dir)
            self.locate_folder_button1.place(x=680, y=435)


    def locate_folder_dir(self):
        folder_selected = filedialog.askdirectory()
        try:
            self.dir_path_entry1.delete(0,END)
            self.dir_path_entry.delete(0,END)
        except: pass
        
        try:
            self.dir_path_entry1.insert(0, "{}".format(folder_selected))
        except:
            self.dir_path_entry.insert(0, "{}".format(folder_selected))

        self.check_specify_path_entry()

    def check_specify_path_entry(self):
        if self.file_t_choice[-1] == 'txt':
            if self.dir_path_entry.get() != '':
                self.s_directory()
            else:
                tkinter.messagebox.showinfo('Error',"Please input a directory path")
        else:
            if self.dir_path_entry1.get() != '':
                self.check_column_if_csv()
            else:
                tkinter.messagebox.showinfo('Error',"Please input a directory path")


    def gen_directory(self):
        
        if self.file_t_choice[-1] == 'csv':
            self.generate = True
            self.check_column_if_csv()
            
        else:
            directory = os.getcwd()+'\Output'
            if not os.path.exists(os.getcwd()+'\Output'):
                os.makedirs(os.getcwd()+'\Output')

            self.cert_gen_speaker(directory)

    def check_column_if_csv(self):
        
        if self.generate == True:
            self.column_excel= Label(self.pack_top, text = "Input the column name:", font = ('arial 12 bold'))
            self.column_excel.place(x=120, y=435)

            self.column_excel_entry =  Entry(self.pack_top, width = 25, font = ('arial 12'))
            self.column_excel_entry.place(x=340, y=435)

            self.column_excel_button = Button(self.pack_top, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.check_if_column_exist)
            self.column_excel_button.place(x=590, y=435)

            print("self.widget_column_name_exist:",self.widget_column_name_exist)
            
            if self.widget_column_name_exist == True:
                self.column_excel2.destroy()
                self.column_excel_entry2.destroy()
                self.column_excel_button2.destroy()

        else:

            self.widget_column_name_exist = True
        
            self.column_excel2= Label(self.pack_top, text = "Input the column name:", font = ('arial 12 bold'))
            self.column_excel2.place(x=120, y=480)

            self.column_excel_entry2 =  Entry(self.pack_top, width = 25, font = ('arial 12'))
            self.column_excel_entry2.place(x=340, y=480)

            self.column_excel_button2 = Button(self.pack_top, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.check_if_column_exist)
            self.column_excel_button2.place(x=590, y=480)

    def s_directory(self):

        directory = self.dir_path_entry.get()
        self.cert_gen_speaker(directory)

    def check_if_column_exist(self):
        
        file_name = self.f_n[-1]

        if self.generate == True:
            column_name = self.column_excel_entry.get()
        else:
            column_name = self.column_excel_entry2.get()
        df = pd.read_csv("{}.csv".format(file_name))

        #try:
        if '{}'.format(column_name) in df:

            if self.generate == False:
                directory = self.dir_path_entry1.get()
                self.cert_gen_speaker(directory)
                

            else:
                directory = os.getcwd()+'\Output'
                if not os.path.exists(os.getcwd()+'\Output'):
                    os.makedirs(os.getcwd()+'\Output')
                self.cert_gen_speaker(directory)
        else:
            tkinter.messagebox.showinfo('Error',"Either you don't have input or the column name does not exist")


    def cert_gen_speaker(self,directory):
        print(directory)
        
        self.destroy_output_screen_but = Button(self.pack_top, text = "Clear Output screen", width = 20, height = 1, bg = 'green', fg='white', command = self.destroy_listbox)
        self.destroy_output_screen_but.place(x=400, y=510)

        file_name = self.f_n[-1]
        file_type_choice = self.file_t_choice[-1]
        template_fn = self.t_n[-1]
        chosen_session = self.session_chosen[-1]
        font_style = self.font_name[-1]
        font_size_name = int(self.font_s_name[-1])
        font_size_session = int(self.font_s_session[-1])
        session_ch = self.session_chosen[-1]
        
        image_type = self.img_type_choice[-1]


        if image_type == 'jpg':
            format_saving = 'JPEG'
        else:
            format_saving = 'PNG'
            
        
        final_x_name = self.x_coor_name[-1]
        final_y_name = self.y_coor_name[-1]

        final_x_session = self.x_coor_session[-1]
        final_y_session = self.y_coor_session[-1]
        
        self.scroll_barY = Scrollbar(self.pack_bottom,orient=VERTICAL)
        self.scroll_barX = Scrollbar(self.pack_bottom,orient=HORIZONTAL)
        
        self.listbox = Listbox(self.pack_bottom, height = 10,
                          width = 115,
                          yscrollcommand = self.scroll_barY,
                          xscrollcomman = self.scroll_barX)

        self.scroll_barX.config(command = self.listbox.xview)
        self.scroll_barY.config(command = self.listbox.yview)
        self.scroll_barX.pack(side = BOTTOM, fill = X)
        self.scroll_barY.pack(side = RIGHT, fill = Y)

        self.listbox.pack()

        if file_type_choice == 'csv':
            if self.generate == True:
                column_name = self.column_excel_entry.get()
            else:
                column_name = self.column_excel_entry2.get()
            df = pd.read_csv("{}.csv".format(file_name))
            for index, row in df.iterrows():
                img = Image.open("{}.{}".format(template_fn,image_type))
                draw = ImageDraw.Draw(img)
                name = row['{}'.format(column_name)]
                draw.text(xy=(final_x_name, final_y_name), text='{}'.format(name), fill=(0, 0, 0),
                          font=ImageFont.truetype("{}.ttf".format(font_style), font_size_name), anchor='mm')

                draw.text(xy=(final_x_session, final_y_session), text='{}'.format(session_ch), fill=(0, 0, 0),
                         font=ImageFont.truetype("{}.ttf".format(font_style), font_size_session), anchor='mm')
                
                if not os.path.exists(directory):
                    os.makedirs(directory)
                img.save("{}/{}.jpg".format(directory, name), format= '{}'.format(format_saving))
                img.close()
                msg = "Appreciation certificate successfully saved, Filename: {} at {}".format(name, directory)
                print("Appreciation certificate successfully saved, Filename: {} at {}".format(name, directory))
                
                self.listbox.insert(END,msg)
                    
                self.pack_bottom.update_idletasks()
                print("\n")
        else:
            list_of_names = []
            with open("{}.txt".format(file_name), 'r') as file:
                lines = [name.strip() for name in file.readlines()]
                for l in lines:
                    if l == "":
                        pass
                    else:
                        list_of_names.append(l)
                for f in list_of_names:
                    img = Image.open("{}.{}".format(template_fn,image_type))
                    draw = ImageDraw.Draw(img)
                    draw.text(xy=(final_x, final_y), text='{}'.format(f), fill=(0, 0, 0),
                              font=ImageFont.truetype("{}.ttf".format(font_style), font_size), anchor='mm')
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    img.save("{}/{}.jpg".format(directory, f), format= '{}'.format(format_saving))
                    img.close()
                    msg = "Appreciation certificate successfully saved, Filename: {} at {}".format(f, directory)
                    print("Appreciation certificate successfully saved, Filename: {} at {}".format(f, directory))
                    self.listbox.insert(END,msg)
                    self.pack_bottom.update_idletasks()
                    print("\n")
                    
    def destroy_listbox(self):
        self.listbox.destroy()
        self.scroll_barX.destroy()
        self.scroll_barY.destroy()


window = Tk()
main = Names(window)
window.geometry("963x700+540+110")
window.title("Certificate Generator")
window.resizable(width=False, height=False)
window.mainloop()
