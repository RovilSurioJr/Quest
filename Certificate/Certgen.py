import os
from PIL import Image, ImageFont, ImageDraw
import pandas as pd

class Cert:
    
    def cert_gen_speaker(self,file_name,speaker_fn,directory):

        df = pd.read_csv("{}.csv".format(file_name))
        for index, row in df.iterrows():
            if row['Appreciation'] == 1:
                img = Image.open("{}.jpg".format(speaker_fn))
                draw = ImageDraw.Draw(img)
                draw.text(xy=(1873, 1101), text='{}'.format(row['Name']), fill=(0, 0, 0),
                          font=ImageFont.truetype('GOTHICB.ttf', 100), anchor='mm')
                draw.text(xy=(1873, 1400), text='{}'.format(row['Topic']), fill=(0, 0, 0),
                          font=ImageFont.truetype('GOTHICB.ttf', 100), anchor='mm')
        
                if not os.path.exists(directory):
                    os.makedirs(directory)
                name = row['Name']
                img.save("{}/{}.jpg".format(directory, name), format= 'JPEG')
                print("Appreciation certificate successfully saved, Filename: {} at {}".format(name, directory))
                img.close()
                print("\n")
    def cert_gen_am_participants(self,file_name,attendance_fn,directory):

        df = pd.read_csv("{}.csv".format(file_name))
        for index, row in df.iterrows():
            if row['AM Participation'] == 1:
                img = Image.open("{}.jpg".format(attendance_fn))
                draw = ImageDraw.Draw(img)
                draw.text(xy=(1873, 1101), text='{}'.format(row['Name']), fill=(0, 0, 0),
                          font=ImageFont.truetype('GOTHICB.ttf', 100), anchor='mm')

                if not os.path.exists(directory):
                    os.makedirs(directory)
                name = row['Name']
                img.save("{}/{}.jpg".format(directory, name), format= 'JPEG')
                print("AM Participants certificate successfully saved, Filename: {} at {}".format(name, directory))
                img.close()
                print("\n")


    def cert_gen_pm_participants(self,file_name,attendance_fn,directory):
        df = pd.read_csv("{}.csv".format(file_name))
        for index, row in df.iterrows():
            if row['PM Participation'] == 1:
                img = Image.open("{}.jpg".format(attendance_fn))
                draw = ImageDraw.Draw(img)
                draw.text(xy=(1873, 1101), text='{}'.format(row['Name']), fill=(0, 0, 0),
                          font=ImageFont.truetype('GOTHICB.ttf', 100), anchor='mm')
                if not os.path.exists(directory):
                    os.makedirs(directory)
                name = row['Name']
                img.save("{}/{}.jpg".format(directory, name), format= 'JPEG')
                print("PM Participants certificate successfully saved, Filename: {} at {}".format(name, directory))
                img.close()
                print("\n")

class Certs:

    def create_cert_speak(self,file_name,speaker_fn,directory):
        cert = Cert()
        cert.cert_gen_speaker(file_name,speaker_fn,directory)

    def create_cert_parti(self,file_name,attendance_fn,directory,session_choice):
        cert = Cert()
        if session_choice == 1:
            cert.cert_gen_am_participants(file_name,attendance_fn,directory)
        else:
            cert.cert_gen_pm_participants(file_name,attendance_fn,directory)
        

    def user_input(self):
        while True:
            try:
                p_choices = [1,2]
                print("1). Speakers")
                print("2). Participants")
                user_choice = (int(input("The certificate is for whom?")))
                while user_choice not in p_choices:
                    user_choice = (int(input("The certificate is for whom?")))
                break
            except ValueError:
                print("Please input a valid integer! Please try again")
                
                
        if user_choice == 1:
            invalid_characters = ['/',':','?','<','>','|','\\']
            invalid_char_input = []
        
            open_file_flag = False
            while open_file_flag is False:
                file_name = input("Filename of Data (i.e, TechnoSummitData): ")
                for ic in invalid_characters:
                    if ic in file_name:
                        invalid_char_input.append(ic)
                
                if len(invalid_char_input) > 0:
                    print("A file name can't contain any of the ff characters: \ / : ? > < | ")
                    invalid_char_input.clear()
                else: invalid_char_input.clear()
                
                try:
                    df = pd.read_csv("{}.csv".format(file_name))
                    open_file_flag  = True       
                except IOError as e:
                    open_file_flag = False
                    print(e)
            
            open_tempfile_flag = False
            while open_tempfile_flag is False:
                speaker_fn = input(str("Filename of Speakers template (i.e, speakers_temp): "))
                for inc in invalid_characters:
                    if inc in speaker_fn:
                        invalid_char_input.append(ic)
                
                if len(invalid_char_input) > 0:
                    print("A template file name can't contain any of the ff characters: \ / : ? > < | ")
                    invalid_char_input.clear()
                else: invalid_char_input.clear()
        
                try:
                    with open("{}.jpg".format(speaker_fn), 'r') as file:
                        open_tempfile_flag  = True
                    
                except IOError as e:
                    open_tempfile_flag = False
                    print(e)
                
            choices = ["y","n"]
            choice = input("Specify where to save the image(y) or save it to the output folder(n)")
            choice = choice.lower()
            while choice not in choices:
                print("Please choose y or n!")
                choice = input("Specify where to save the image(y) or save it to the output folder(n)")
                choice = choice.lower()
                
            if choice == 'y':
                directory = input(str("Choose the file path in where the image will be saved: "))
            elif choice == 'n':
                directory = os.getcwd()+'\Speakers'
           
            print("\n")
        
            if not os.path.exists(os.getcwd()+'\Speakers'):
                os.makedirs(os.getcwd()+'\Speakers')
            
            self.create_cert_speak(file_name,speaker_fn,directory)

        elif user_choice == 2:
            invalid_characters = ['/',':','?','<','>','|','\\']
            invalid_char_input = []
        
            open_file_flag = False
            while open_file_flag is False:
                file_name = input("Filename of Data (i.e, TechnoSummitData): ")
                for ic in invalid_characters:
                    if ic in file_name:
                        invalid_char_input.append(ic)
                
                if len(invalid_char_input) > 0:
                    print("A file name can't contain any of the ff characters: \ / : ? > < | ")
                    invalid_char_input.clear()
                else: invalid_char_input.clear()
                
                try:
                    df = pd.read_csv("{}.csv".format(file_name))
                    open_file_flag  = True       
                except IOError as e:
                    open_file_flag = False
                    print(e)
            
            open_tempfile_flag = False
            while open_tempfile_flag is False:
                attendance_fn = input(str("Filename of participants template (i.e, am_temp or pm_temp): "))
                for inc in invalid_characters:
                    if inc in attendance_fn:
                        invalid_char_input.append(ic)
                
                if len(invalid_char_input) > 0:
                    print("A template file name can't contain any of the ff characters: \ / : ? > < | ")
                    invalid_char_input.clear()
                else: invalid_char_input.clear()
        
                try:
                    with open("{}.jpg".format(attendance_fn), 'r') as file:
                        open_tempfile_flag  = True
                    
                except IOError as e:
                    open_tempfile_flag = False
                    print(e)

            
            while True:
                try:
                    sessions = [1,2]
                    print("1). AM")
                    print("2). PM")
                    session_choice = (int(input("For what session?")))
                    while session_choice not in sessions:
                        session_choice = (int(input("For what session?")))
                    break
                    
                except ValueError:
                    print("Please input a valid integer! Please try again")
            choices = ["y","n"]
            choice = input("Specify where to save the image(y) or save it to the output folder(n)")
            choice = choice.lower()
            while choice not in choices:
                print("Please choose y or n!")
                choice = input("Specify where to save the image(y) or save it to the output folder(n)")
                choice = choice.lower()
                
            if choice == 'y':
                directory = input(str("Choose the file path in where the image will be saved: "))
            elif choice == 'n':
                if session_choice == 1:
                    directory = os.getcwd()+'\AM_Participants'
                else:
                    directory = os.getcwd()+'\PM_Participants'
                    
           
            print("\n")
        
            if not os.path.exists(os.getcwd()+'\AM_Participants'):
                os.makedirs(os.getcwd()+'\AM_Participants')

            if not os.path.exists(os.getcwd()+'\PM_Participants'):
                os.makedirs(os.getcwd()+'\PM_Participants')

            self.create_cert_parti(file_name,attendance_fn,directory,session_choice)
            
        

            
if __name__ == '__main__':
    cert = Certs()
    cert.user_input()

