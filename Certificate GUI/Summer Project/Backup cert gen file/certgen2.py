from tkinter import *
from tkinter import ttk
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
        self.img_type_choice = []
        self.file_t_choice = []

        self.x_coor = []
        self.y_coor = []

        self.pack_top = Frame(master, width=700, height=450 ,bg = 'white')
        self.pack_top.pack(side=TOP)
        
        self.pack_bottom = Frame(master, width=700, height=400) 
        self.pack_bottom.pack(side=BOTTOM)


        self.heading = Label(master)
        self.heading = Label(master, text="Create Certificate", font = ('arial 20 bold'), fg ='green')
        self.heading.place(x=375,y=0)

        #Text

        self.excelfile= Label(master, text = "Input source filename:", font = ('arial 12 bold'))
        self.excelfile.place(x=155, y=75)

        #Text box

        self.excelfile_entry =  Entry(master, width = 25, font = ('arial 12 '))
        self.excelfile_entry.place(x=380, y=75)


        #Button

        self.search_file_button = Button(master, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.check_excel_file)
        self.search_file_button.place(x=630, y=75)

        file_type_choices = ['csv','txt']
        self.file_type_choice = ttk.Combobox(master, value = file_type_choices,width =10)
        self.file_type_choice.current(0)
        self.file_type_choice.bind("<<ComboboxSelected>>", self.combo_click1)
        self.file_type_choice.place(x=730, y=75)
        self.file_t_choice.append('csv')
        
    def combo_click1(self,file_type_choice):
        if self.file_type_choice.get() == 'txt':
            self.file_t_choice.append('txt')
            print("txt")
        else:
            self.file_t_choice.append('csv')
            print("csv")

    def check_excel_file(self):
        
        file_name = self.excelfile_entry.get()
        file_type_choice = self.file_t_choice[-1]
        
        invalid_characters = ['/',':','?','<','>','|','\\']
        invalid_char_input = []
        
        for ic in invalid_characters:
            if ic in file_name:
                invalid_char_input.append(ic)
                
        if len(invalid_char_input) > 0:
            tkinter.messagebox.showinfo('Error',"A file name can't contain any of the ff characters: \ / : ? > < | ")
            invalid_char_input.clear()
        else: invalid_char_input.clear()

        if file_type_choice == 'csv':
            try:
                df = pd.read_csv("{}.csv".format(file_name))
                self.f_n.append(file_name) #Appending to list
                self.show_template_button() #Showing the template objects
            except IOError as e:
                tkinter.messagebox.showinfo('Error',e)
        else:
            try:
                with open("{}.txt".format(file_name), 'r') as file:
                    self.f_n.append(file_name)
                    self.show_template_button()
            except IOError as e:
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

        img_type = ['jpg','PNG']
        self.img_type_choices = ttk.Combobox(self.pack_top, value = img_type,width =10)
        self.img_type_choices.current(0)
        self.img_type_choices.bind("<<ComboboxSelected>>", self.combo_click2)
        self.img_type_choices.place(x=600, y=123)
        self.img_type_choice.append('jpg')

    def combo_click2(self,img_type_choices):
        if self.img_type_choices.get() == 'jpg':
            self.img_type_choice.append('jpg')
            print("jpg")
        else:
            self.img_type_choice.append('PNG')
            print("PNG")


    def check_template_file(self):

        speaker_fn = self.tempfile_entry.get()
        image_type = self.img_type_choice[-1]

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
            image =Image.open("{}.{}".format(speaker_fn,image_type))
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
            with open("{}.ttf".format(f_style_fn)):
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
            self.show_imgsize_button()
            
            
        except ValueError:
            tkinter.messagebox.showinfo('Error',"Please input an integer")

        #if int(font_s) == ty
        
        
        #print(self.font_s)
    def show_imgsize_button(self):

        speaker_fn = self.t_n[-1]
        image_type = self.img_type_choice[-1]
        
        self.img_s= Label(self.pack_top, text = "X & Y for placement of names:", font = ('arial 12 bold'))
        self.img_s.place(x=25, y=255)
        self.img_sz_note= Label(self.pack_top, text = "*The default is at center of the image", font = ('arial 9 italic'))
        self.img_sz_note.place(x=267, y=275)

        img = Image.open("{}.{}".format(speaker_fn,image_type))
        lxw = img.size
        length= lxw[0] // 2
        width = lxw[1] //2
        
        self.X_val_entry =  Entry(self.pack_top, width = 6, font = ('arial 12'))
        self.X_val_entry.place(x=300, y=255)
        self.X_val_entry.insert(0, "{}".format(length))

        self.Y_val_entry =  Entry(self.pack_top, width = 6, font = ('arial 12'))
        self.Y_val_entry.place(x=380, y=255)
        self.Y_val_entry.insert(0, "{}".format(width))

        self.proceed_button = Button(self.pack_top, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.check_coordinates_input )
        self.proceed_button.place(x=500, y=255)


    def check_coordinates_input(self):
        l = self.X_val_entry.get()
        w = self.Y_val_entry.get()

        try:
            
            X_img = int(l)
            Y_img = int(w)
            self.x_coor.append(X_img)
            self.y_coor.append(Y_img)

            self.show_directory_button()
            
        except ValueError:
            tkinter.messagebox.showinfo('Error',"Please input an integer")


    #self.show_directory_button()
    def show_directory_button(self):

        #Text

        self.dir= Label(self.pack_top, text = "Output Directory:", font = ('arial 12 bold'))
        self.dir.place(x=25, y=300)

        #Button

        self.speci_file_button = Button(self.pack_top, text = "Specify", width = 10, height = 1, bg = 'green', fg='white', command = self.specify_dir)
        self.speci_file_button.place(x=250, y=300)

        self.gen_file_button = Button(self.pack_top, text = "Generate", width = 10, height = 1, bg = 'green', fg='white', command = self.gen_directory)
        self.gen_file_button.place(x=400, y=300)

    def specify_dir(self):

        self.generate = False
        self.widget_column_name_exist = False

        if self.file_t_choice[-1] == 'csv':
            self.dir= Label(self.pack_top, text = "Input the directory path:", font = ('arial 12 bold'))
            self.dir.place(x=25, y=345)

            self.dir_path_entry =  Entry(self.pack_top, width = 25, font = ('arial 12'))
            self.dir_path_entry.place(x=250, y=345)

            self.speci_enter_button = Button(self.pack_top, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.check_column_if_csv)
            self.speci_enter_button.place(x=500, y=345)

            

        else:
            self.dir= Label(self.pack_top, text = "Input the directory path:", font = ('arial 12 bold'))
            self.dir.place(x=25, y=345)
            
            self.dir_path_entry =  Entry(self.pack_top, width = 25, font = ('arial 12'))
            self.dir_path_entry.place(x=250, y=345)
            
            self.speci_enter_button = Button(self.pack_top, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.s_directory)
            self.speci_enter_button.place(x=500, y=345)

    def gen_directory(self):
        
        if self.file_t_choice[-1] == 'csv':
            self.generate = True
            self.check_column_if_csv()

            #self.cert_gen_speaker(directory)

        else:
            directory = os.getcwd()+'\Output'
            if not os.path.exists(os.getcwd()+'\Output'):
                os.makedirs(os.getcwd()+'\Output')

            self.cert_gen_speaker(directory)

    def s_directory(self):

        directory = self.dir_path_entry.get()
        self.cert_gen_speaker(directory)

    def check_column_if_csv(self):
        

        if self.generate == True:
            self.column_excel= Label(self.pack_top, text = "Input the column name:", font = ('arial 12 bold'))
            self.column_excel.place(x=25, y=345)

            self.column_excel_entry =  Entry(self.pack_top, width = 25, font = ('arial 12'))
            self.column_excel_entry.place(x=250, y=345)

            self.column_excel_button = Button(self.pack_top, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.check_if_column_exist)
            self.column_excel_button.place(x=500, y=345)

            print(self.widget_column_name_exist)
            if self.widget_column_name_exist == True:
                self.column_excel2.destroy()
                self.column_excel_entry2.destroy()
                self.column_excel_button2.destroy()

        else:
            #if self.widget_column_name_exist == True:
                #self.column_excel.destroy()
                #self.column_excel_entry.destroy()
                #self.column_excel_button.destroy()


            self.widget_column_name_exist = True
        
            self.column_excel2= Label(self.pack_top, text = "Input the column name:", font = ('arial 12 bold'))
            self.column_excel2.place(x=25, y=390)

            self.column_excel_entry2 =  Entry(self.pack_top, width = 25, font = ('arial 12'))
            self.column_excel_entry2.place(x=250, y=390)

            self.column_excel_button2 = Button(self.pack_top, text = "Enter", width = 10, height = 1, bg = 'green', fg='white', command = self.check_if_column_exist)
            self.column_excel_button2.place(x=500, y=390)

    def check_if_column_exist(self):
        
        file_name = self.f_n[-1]

        if self.generate == True:
            column_name = self.column_excel_entry.get()
        else:
            column_name = self.column_excel_entry2.get()
        df = pd.read_csv("{}.csv".format(file_name))

        #try:
        if '{}'.format(column_name) in df:
            directory = os.getcwd()+'\Output'
            if not os.path.exists(os.getcwd()+'\Output'):
                os.makedirs(os.getcwd()+'\Output')
            self.cert_gen_speaker(directory)
        else:
            tkinter.messagebox.showinfo('Error',"Either you don't have input or the column name does not exist")
                
        #except:
            #tkinter.messagebox.showinfo('Error',"error")

        

    def cert_gen_speaker(self,directory):

        file_name = self.f_n[-1]
        file_type_choice = self.file_t_choice[-1]
        template_fn = self.t_n[-1]
        font_style = self.font_n[-1]
        font_size = int(self.font_s[-1])
        image_type = self.img_type_choice[-1]


        if image_type == 'jpg':
            format_saving = 'JPEG'
        else:
            format_saving = 'PNG'
            
        
        final_x = self.x_coor[-1]
        final_y = self.y_coor[-1]
        
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
                draw.text(xy=(final_x, final_y), text='{}'.format(name), fill=(0, 0, 0),
                          font=ImageFont.truetype("{}.ttf".format(font_style), font_size), anchor='mm')
                if not os.path.exists(directory):
                    os.makedirs(directory)
                img.save("{}/{}.jpg".format(directory, name), format= '{}'.format(format_saving))
                img.close()
                msg = "Appreciation certificate successfully saved, Filename: {} at {}".format(name, directory)
                print("Appreciation certificate successfully saved, Filename: {} at {}".format(name, directory))
                
                listbox.insert(END,msg)
                    
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
                    listbox.insert(END,msg)
                    self.pack_bottom.update_idletasks()
                    print("\n")
            


#def create_cert(self,window):
    #create_cert = Names(window)

window = Tk()
main = Names(window)
window.geometry("963x600+540+110")
window.title("Certificate Generator")
window.resizable(width=False, height=False)
window.mainloop()
