
from subprocess import call
from tkinter import *
import add_inventory_or_customer as inv
import update_customers as customer
import update_plants as plant
import transaction as transac


class Garden():
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
        self.Message6.configure(text='''Apolaki's Community Garden''')
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
        self.Button1.configure(text='''ADD PLANT/S''')
        self.Button1.configure(width=566)
        self.Button1.configure(command=inv.add_plant)

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
        self.Button2.configure(text='''REGISTER CUSTOMER/S''')
        self.Button2.configure(width=566)
        self.Button2.configure(command=inv.add_customer)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0, rely=0.45, height=180, width=290)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=font14)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''MODIFY PLANT''')
        self.Button3.configure(width=566)
        self.Button3.configure(command=plant.update_plant)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.67, rely=0.17, height=180, width=290)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font14)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''MODIFY CUSTOMER''')
        self.Button4.configure(width=566)
        self.Button4.configure(command=customer.update_customer)

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.33, rely=0.45, height=180, width=290)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=font14)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''TRANSACTION''')
        self.Button5.configure(width=566)
        self.Button5.configure(command=transac.transaction)

        #------ Not working -------#

        self.Button9 = Button(self.Frame1)
        self.Button9.place(relx=0.33, rely=0.73, height=180, width=290)
        self.Button9.configure(activebackground="#d9d9d9")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(disabledforeground="#bfbfbf")
        self.Button9.configure(font=font14)
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''TRANSACTION HISTORY''')
        self.Button9.configure(width=566)
        self.Button9.configure(command=quit)

        self.Button10 = Button(self.Frame1)
        self.Button10.place(relx=0.67, rely=0.45, height=180, width=290)
        self.Button10.configure(activebackground="#d9d9d9")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(disabledforeground="#bfbfbf")
        self.Button10.configure(font=font14)
        self.Button10.configure(foreground="#000000")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self.Button10.configure(pady="0")
        self.Button10.configure(text='''TOTAL SALES''')
        self.Button10.configure(width=566)
        self.Button10.configure(command=quit)


        root.mainloop()


if __name__ == '__main__':
    Garden()


