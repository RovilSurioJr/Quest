import random
import textwrap as TW
import os
import uuid
from PIL import Image, ImageFont, ImageDraw

class Phrase:
    
    def random_phrase(self,file_name,bingocard_filename,directory ):
        bingo_card = [] # For final phrases per card
        duplicate_checker = [] # For avoiding duplication
        final_phrases = [] # For text wrapping

        try:
            font_style = ImageFont.truetype("Roboto-Medium.ttf",size = 23)
            bingo_template = Image.open("{}.jpg".format(bingocard_filename))
            draw = ImageDraw.Draw(bingo_template)
            x = 100
            y1 = 340
            y2 = 390

            while len(bingo_card) != 9:
                with open(file_name, 'r') as file:
                    lines = file.readlines()
                    random_line = random.choice(lines)
                    duplicate_checker.append(random_line.rstrip('\n'))
                    for phrase in duplicate_checker:
                        if phrase not in bingo_card:
                            bingo_card.append(phrase)

            print("The set of phrases per card has been generated: ",bingo_card)

            for p in bingo_card:
                line_wrapped = TW.wrap(p,width = 18)
                final_phrases.append(line_wrapped)

            for line in final_phrases:

                if y1 <= 800 and y2 <= 850:

                    if len(line) > 1:
                        draw.text((x,y1),line[0],font = font_style,fill = "black",align = "center")
                        draw.text((x,y2),line[1],font = font_style,fill = "black", aligh = "center")

                    else:
                        draw.text((x,y1),line[0],font = font_style,fill="black")
                    y1+=230
                    y2+=230
            
                
                else:
                    if x <= 510:
                        x+=205
                    else:
                        x = 100
                    y1 = 340
                    y2 = 390
                    if len(line) > 1:
                        draw.text((x,y1),line[0],font = font_style,fill = "black",align = "center")
                        draw.text((x,y2),line[1],font = font_style,fill = "black", aligh = "center")

                    else:
                        draw.text((x,y1),line[0],font = font_style,fill="black")
                    y1+=230
                    y2+=230


            name = uuid.uuid4()
            bingo_template.save("{}/{}.jpg".format(directory, name), format= 'JPEG')
            print("Bingo Card successfully saved, Filename: {} at {}".format(name, directory))
            print("\n")

            if not os.path.exists(directory):
                os.makedirs(directory)

        except IOError as e:
            print(e)


class Phrases:

    def create_card(self,file_name,bingocard_filename,directory ):
        phrase = Phrase()
        phrase.random_phrase(file_name,bingocard_filename,directory)
        

    def user_input(self):
        self.number_of_card_to_be_added = (int(input("How many bingo card to create?: ")))
        file_name = input("Filename of phrases (i.e, hello.txt): ")
        bingocard_filename = input(str("Filename of template (i.e, bingocard): "))
        directory = input(str("Choose the file path in where the image will be saved: "))
        print("\n")
        for i in range (self.number_of_card_to_be_added):
            self.create_card(file_name,bingocard_filename,directory)
            
if __name__ == '__main__':
    phrase = Phrases()
    phrase.user_input()

