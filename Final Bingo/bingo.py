import random
import textwrap as TW
import os
from PIL import Image, ImageFont, ImageDraw

class Phrase:
    
    def random_phrase(self,file_name,bingocard_filename,directory,f_n):
        bingo_card = [] # For final phrases per card
        duplicate_checker = [] # For avoiding duplication
        final_phrases = [] # For text wrapping

        font_style = ImageFont.truetype("Roboto-Medium.ttf",size = 40)
        bingo_template = Image.open("{}.PNG".format(bingocard_filename))
        draw = ImageDraw.Draw(bingo_template)
        x = 350
        y1 = 790
        y2 = 840

        while len(bingo_card) != 9:
            with open("{}.txt".format(file_name), 'r') as file:
                lines = file.readlines()
                random_line = random.choice(lines)
                duplicate_checker.append(random_line)
                for phrase in duplicate_checker:
                    if phrase ==  "\n":
                       pass
                    elif phrase not in bingo_card:
                        bingo_card.append(phrase)

        print("The set of phrases per card has been generated ")
                  #,bingo_card)

        for p in bingo_card:
            line_wrapped = TW.wrap(p,width = 20)
            final_phrases.append(line_wrapped)

        for line in final_phrases:

            if y1 <= 1650 and y2 <= 1700:

                if len(line) > 1:
                    draw.text((x,y1),line[0],font = font_style,fill = "black",anchor = "mm")
                    draw.text((x,y2),line[1],font = font_style,fill = "black", anchor = "mm")

                else:
                    draw.text((x,y1),line[0],font = font_style,fill="black",anchor = "mm")
                y1+=430
                y2+=430
            
                
            else:
                if x <= 1000:
                    x+=425
                else:
                    x = 150
                y1 = 790
                y2 = 840
                if len(line) > 1:
                    draw.text((x,y1),line[0],font = font_style,fill = "black",anchor = "mm")
                    draw.text((x,y2),line[1],font = font_style,fill = "black", anchor = "mm")

                else:
                    draw.text((x,y1),line[0],font = font_style,fill="black",anchor = "mm")
                y1+=430
                y2+=430
        
        name = f_n
        bingo_template.save("{}/{}.PNG".format(directory, name), format= 'PNG')
        print("Bingo Card successfully saved, Filename: {} at {}".format(name, directory))
        print("\n")
        if not os.path.exists(directory):
            os.makedirs(directory)



class Phrases:

    def create_card(self,file_name,bingocard_filename,directory,f_n):
        phrase = Phrase()
        phrase.random_phrase(file_name,bingocard_filename,directory,f_n)
        

    def user_input(self):
        while True:
            try:
                number_of_card_to_be_added = (int(input("How many bingo card to create?: ")))
                break
            except ValueError:
                print("Please input a valid integer! Please try again!")
        
        invalid_characters = ['/',':','?','<','>','|','\\']
        invalid_char_input = []
        
        open_file_flag = False
        while open_file_flag is False:
            file_name = input("Filename of phrases (i.e, hello): ")
            for ic in invalid_characters:
                if ic in file_name:
                    invalid_char_input.append(ic)
                
            if len(invalid_char_input) > 0:
                print("A file name can't contain any of the ff characters: \ / : ? > < | ")
                invalid_char_input.clear()
            else: invalid_char_input.clear()
                
            try:
                with open("{}.txt".format(file_name), 'r') as file:
                    open_file_flag  = True
                    
            except IOError as e:
                open_file_flag = False
                print(e)
                
        open_tempfile_flag = False
        while open_tempfile_flag is False:
            bingocard_filename = input(str("Filename of template (i.e, bingocard): "))
            for inc in invalid_characters:
                if inc in bingocard_filename:
                    invalid_char_input.append(ic)
                
            if len(invalid_char_input) > 0:
                print("A template file name can't contain any of the ff characters: \ / : ? > < | ")
                invalid_char_input.clear()
            else: invalid_char_input.clear()
        
            try:
                with open("{}.PNG".format(bingocard_filename), 'r') as file:
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
            directory = os.getcwd()+'\output'
           
        print("\n")
        f_n = 0
        
        file_name_l = os.listdir(os.getcwd()+'\output')
        if len(file_name_l) > 0:
            f_n = len(file_name_l)
            for i in range(number_of_card_to_be_added):
                f_n+=1
                self.create_card(file_name,bingocard_filename,directory,f_n)
        else:
            for i in range(number_of_card_to_be_added):
                f_n+=1
                self.create_card(file_name,bingocard_filename,directory,f_n)
            
if __name__ == '__main__':
    phrase = Phrases()
    phrase.user_input()

