from tkinter import *
import sqlite3
import tkinter.messagebox

#connecting with sql
conn = sqlite3.connect("D:\FINAL APOLAKI\Apolaki Final\Database\store.db")
#creating curser to be able to communicate with sql
c = conn.cursor()
  
class add_plants:
    def __init__(self,master):

        self.master = master
        self.heading = Label(master)
        self.heading = Label(master, text="Add a plant to database", font = ('arial 20 bold'), fg ='green')
        self.heading.place(x=300,y=0)


        # Labels this window

        self.plant_name_l= Label(master, text = "Input plant name:", font = ('arial 12 bold'))
        self.plant_name_l.place(x=25, y=75)
        
        self.plant_type_l = Label(master, text = "Input plant type:", font = ('arial 12 bold'))
        self.plant_type_l.place(x=25, y=100)
        
        self.plant_price_l = Label(master, text = "Input plant price:", font = ('arial 12 bold'))
        self.plant_price_l.place(x=25, y=125)

        self.plant_quantity_l = Label(master, text = "Input plant quantity:", font = ('arial 12 bold'))
        self.plant_quantity_l.place(x=25, y=150)
        

        # Entries for the labels above or this window

        self.plant_name_e =  Entry(master, width = 25, font = ('arial 12 '))
        self.plant_name_e.place(x=250, y=75)

        self.plant_type_e =  Entry(master, width = 25, font = ('arial 12 '))
        self.plant_type_e.place(x=250, y=100)

        self.plant_price_e =  Entry(master, width = 25, font = ('arial 12 '))
        self.plant_price_e.place(x=250, y=125)

        self.plant_quantity_e =  Entry(master, width = 25, font = ('arial 12 '))
        self.plant_quantity_e.place(x=250, y=150)
        
        # Button to add to the database
        self.button_to_add = Button(master, text = "Add To Database", width = 25, height = 6, bg = 'green', fg='white', command = self.get_items)
        self.button_to_add.place(x=25, y=200)

        # Text box for the logs
        self.textbox = Text(master, width=50,height=10)
        self.textbox.place(x=525, y=75)

        # for plants checking how many plants in database
        result = c.execute("SELECT plant_name FROM plants")
        id_plant = result.fetchall()
        self.textbox.insert(1.0, "The items in inventory are: \n")
        for plant in id_plant:
            self.textbox.insert(END, plant[0] + "\n")

        # Button to delete what has been typed
        self.button_to_clear = Button(master, text = "Clear all inputs", width = 25, height = 6, bg = 'green', fg='white', command = self.clear_all)
        self.button_to_clear.place(x=250, y=200)

    def get_items(self):
        # get from entries
        try:
            self.plant_name = self.plant_name_e.get()
            self.plant_type = self.plant_type_e.get()
            self.plant_price  =  float(self.plant_price_e.get())
            self.plant_quantity = int(self.plant_quantity_e.get())

            # just to Check if there is an empty text box on the following

            if self.plant_name == ''or self.plant_name ==  '' or type(self.plant_price) != type(float()) or type(self.plant_quantity) != type(int()):
                tkinter.messagebox.showinfo("Error", "Please fill all the details.")#pop up error

            # ADDING TO SQL DATABASE
            # STUDY THE STATEMENT WRITING IN SQLITE; ALL THE CAPITAL WORD BELOW IS STATEMENT. ex.(INSERT INTO)
            # THE (plant_name,plant_type,plant_price,plant_quantity) Below is the name per column on database
            else:
                sql = "INSERT INTO plants (plant_name,plant_type,plant_price,plant_quantity) VALUES(?,?,?,?)"
                c.execute(sql,(self.plant_name, self.plant_type, self.plant_price, self.plant_quantity))
                conn.commit() # commit means to push everything we want to execute on database
                # Insert to text box
                self.textbox.insert(END, "\n\nInserted " + str(self.plant_name) + " into the database.")
                tkinter.messagebox.showinfo("Success", "The plant was added")

        except:
            tkinter.messagebox.showinfo('Error','Invalid details')


    def clear_all(self):
        self.plant_name_e.delete(0, END)
        self.plant_type_e.delete(0, END)
        self.plant_price_e.delete(0, END)
        self.plant_quantity_e.delete(0, END)


class add_customers:

    def __init__(self,master1):

        # Labels this window
        self.master1 = master1
        self.heading = Label(master1)
        self.heading = Label(master1, text="Add a customer to database", font = ('arial 20 bold'), fg ='green')
        self.heading.place(x=300,y=0)

        self.customer_name_l = Label(master1, text = "Input customer name", font = ('arial 12 bold'))
        self.customer_name_l.place(x=25, y=75)
        
        self.customer_address_l = Label(master1, text = "Input customer address", font = ('arial 12 bold'))
        self.customer_address_l.place(x=25, y=100)
        
        self.customer_email_l = Label(master1, text = "Input customer email", font = ('arial 12 bold'))
        self.customer_email_l.place(x=25, y=125)
        
        self.customer_contact_number_l = Label(master1, text = "Input customer contact number", font = ('arial 12 bold'))
        self.customer_contact_number_l.place(x=25, y=150)

        # Entries for the labels above or this window

        self.customer_name_e =  Entry(master1, width = 25, font = ('arial 12 '))
        self.customer_name_e.place(x=275, y=75)

        self.customer_address_e =  Entry(master1, width = 25, font = ('arial 12 '))
        self.customer_address_e.place(x=275, y=100)

        self.customer_email_e =  Entry(master1, width = 25, font = ('arial 12 '))
        self.customer_email_e.place(x=275, y=125)
        
        self.customer_contact_number_e =  Entry(master1, width = 25, font = ('arial 12 '))
        self.customer_contact_number_e.place(x=275, y=150)

        # Button to add to the database
        self.button_to_add = Button(master1, text = "Add To Database", width = 25, height = 6, bg = 'green', fg='white', command = self.get_items)
        self.button_to_add.place(x=25, y=200)

        # Text box for the logs
        self.textbox = Text(master1, width=50,height=10)
        self.textbox.place(x=525, y=75)

        # To check how many items now  using text box

        # for customers checking how many customers in database
        result2 = c.execute("SELECT customer_name FROM customers")

        id_cus = result2.fetchall()
        self.textbox.insert(1.0,"The registered customers are: \n")
        for customer in id_cus:
            self.textbox.insert(END,customer[0]+"\n")

        # Button to delete what has been typed
        self.button_to_clear = Button(master1, text = "Clear all inputs", width = 25, height = 6, bg = 'green', fg='white', command = self.clear_all)
        self.button_to_clear.place(x=250, y=200)

    def get_items(self):
        try:
            # get from entries
            self.customer_name = self.customer_name_e.get()
            self.customer_address = self.customer_address_e.get()
            self.customer_email = self.customer_email_e.get()
            self.customer_contact_number = int(self.customer_contact_number_e.get())

            # just to Check if there is an empty on the following

            if self.customer_name == ''or self.customer_address ==  '' or self.customer_email == '' or type(self.customer_contact_number) != type(int()):
                #print("Empty") <<= if in console
                tkinter.messagebox.showinfo("Error", "Please fill all the details.")#pop up error
            else:

                sql2 = "INSERT INTO customers (customer_name,customer_address,customer_email,customer_contact_number) VALUES(?,?,?,?)"
                c.execute(sql2,(self.customer_name,self.customer_address, self.customer_email, self.customer_contact_number))
                conn.commit()

                # Insert to text box

                self.textbox.insert(END, "\n\nInserted " + str(self.customer_name) + "  into the database.")
                tkinter.messagebox.showinfo("Success", "The customer was added")
        except:
            tkinter.messagebox.showinfo("Error","Invalid Details")


    def clear_all(self):
        self.customer_name_e.delete(0, END)
        self.customer_address_e.delete(0, END)
        self.customer_email_e.delete(0, END)
        self.customer_contact_number_e.delete(0, END)

class Main_menu:
    def __init__(self,master2):
        # Labels this window
        self.master2 = master2
        self.heading = Label(master2)
        self.heading = Label(master2, text="Welcome to Apolaki Garden", font = ('arial 20 bold'), fg ='green')
        self.heading.place(x=350,y=0)
        

# BUTTONS IN MAIN MENU OR WINDOW1
def add_plant():
        window3 = Tk()
        add_a_plants = add_plants(window3)
        window3.geometry("963x749+540+110")
        window3.title("Add to database a plant")
        window3.mainloop()

def add_customer():
        window2 = Tk()
        add_customer = add_customers(window2)
        window2.geometry("963x749+540+110")
        window2.title("Add to database a customer")
        window2.mainloop()
    
        

