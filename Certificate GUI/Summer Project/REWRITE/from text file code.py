import os
from PIL import Image, ImageFont, ImageDraw

f_name = []
ff = 1

final_x = 1300
final_y = 1100
directory = "E:/roviljr/OneDrive/Documents/GitHub/Quest/Certificate GUI/Summer Project/Output"
with open("try text.txt", 'r') as file:
    #font_style = ImageFont.truetype("g.ttf",size = 40)

    lines = [name.strip() for name in file.readlines()]
    for l in lines:
        if l == "":
            pass
        else:
            f_name.append(l)

    for f in f_name:
        img = Image.open("t.jpg")
        draw = ImageDraw.Draw(img)
        draw.text(xy=(final_x, final_y), text='{}'.format(f), fill=(0, 0, 0),
                  font=ImageFont.truetype("g.ttf", 180), anchor='mm')
    
        img.save("{}/{}.jpg".format(directory,  f), format= 'JPEG')
    #print(lines)
    #for name in lines:
       # if name ==  "\n":
            #pass
       # elif name not in f_name:
            #f_name.append(name)
        
            
    #print(lines )
        

