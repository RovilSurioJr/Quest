from tkinter import *
import tkinter.messagebox
import os
from PIL import Image, ImageFont, ImageDraw
import pandas as pd

import speakers as sp
import participants as ps


class Main():
    def __init__(self):
        root = Tk()
        _bgcolor = '#ffffff'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("963x749+540+110")
        root.title("Garden Management System")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Message6 = Message(self.Frame1)
        self.Message6.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
        self.Message6.configure(font=font16)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text='''Certificate Generator''')
        self.Message6.configure(width=791)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0, rely=0.17, height=180, width=290)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(font=font14)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Speakers''')
        self.Button1.configure(width=566)
        self.Button1.configure(command=sp.create_speaker_cert)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.33, rely=0.17, height=180, width=290)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Participants''')
        self.Button2.configure(width=566)
        self.Button2.configure(command=ps.create_participants_cert)

        root.mainloop()





if __name__ == '__main__':
    Main()
