from tkinter import *
import sqlite3
import tkinter.messagebox

#connecting with sql
conn = sqlite3.connect("D:\FINAL APOLAKI\Apolaki Final\Database\store.db")

#creating curser to be able to communicate with sql
c = conn.cursor()

# for customers checking how many customers in database
# result2= c.execute("SELECT Max(id_cus)from customers")
# for customers in result2:
#     id_cus = customers[0]

class add_customers:

    def __init__(self,master1):

        # Labels this window

        self.master1 = master1
        self.heading = Label(master1)
        self.heading = Label(master1, text="Update a customer from database", font = ('arial 20 bold'), fg ='green')
        self.heading.place(x=275,y=0)
        #----------------------------------------------

        # Labels for id of customer
        self.idc_l = Label(master1, text=  "Input ID: ", font = ('arial 12 bold'))
        self.idc_l.place(x = 25, y=75)

        # Entries for id of customer
        self.idc_e = Entry(master1, width = 25, font = ('arial 12'))
        self.idc_e.place(x=275, y=75)

        # Button for search

        self.button_to_search = Button(master1, text = "Search ID", width = 10, height = 1, bg = 'green', fg='white', command = self.search_id_cus)
        self.button_to_search.place(x=525, y=75)

        # Labels for customer
        self.customer_name_l = Label(master1, text = "Input customer name", font = ('arial 12 bold'))
        self.customer_name_l.place(x=25, y=100)
        
        self.customer_address_l = Label(master1, text = "Input customer address", font = ('arial 12 bold'))
        self.customer_address_l.place(x=25, y=125)
        
        self.customer_email_l = Label(master1, text = "Input customer email", font = ('arial 12 bold'))
        self.customer_email_l.place(x=25, y=150)
        
        self.customer_contact_number_l = Label(master1, text = "Input customer contact number", font = ('arial 12 bold'))
        self.customer_contact_number_l.place(x=25, y=175)

        # Entries for the labels above or this window

        self.customer_name_e =  Entry(master1, width = 25, font = ('arial 12 '))
        self.customer_name_e.place(x=275, y=100)

        self.customer_address_e =  Entry(master1, width = 25, font = ('arial 12 '))
        self.customer_address_e.place(x=275, y=125)

        self.customer_email_e =  Entry(master1, width = 25, font = ('arial 12 '))
        self.customer_email_e.place(x=275, y=150)
        
        self.customer_contact_number_e =  Entry(master1, width = 25, font = ('arial 12 '))
        self.customer_contact_number_e.place(x=275, y=175)

        # Button to add to the database
        self.button_to_add = Button(master1, text = "Update Customer", width = 25, height = 6, bg = 'green', fg='white', command = self.update_cus)
        self.button_to_add.place(x=25, y=250)

        # Text box for the logs
        self.textbox = Text(master1, width=113,height=11)
        self.textbox.place(x=25, y=400)

        # To check how many items now  using text box

        # for customers checking how many customers in database
        result2 = c.execute("SELECT customer_name FROM customers")

        id_cus = result2.fetchall()
        self.textbox.insert(1.0,"The registered customers are: \n")
        for customer in id_cus:
            self.textbox.insert(END,customer[0]+"\n") #accesing the ID


    def search_id_cus(self):
        # Note: The " * " below means "everything" in sql
        sql3 = "SELECT * FROM customers WHERE id_cus=?"
        result = c.execute(sql3,(self.idc_e.get(), ))
        for r in result:
            self.customername =r[1] #[1] is the name in database while [0] is the ID
            self.customeraddress =r[2]
            self.customeremail =r[3]
            self.customernumber =r[4]
        conn.commit()

        # Now inserting the existing datas from database to entries/textbox to update
        self.customer_name_e.delete(0, END) # We need a delete so that the "searched" plant from database will be removed
        self.customer_name_e.insert(0,str(self.customername))

        self.customer_address_e.delete(0, END)
        self.customer_address_e.insert(0,str(self.customeraddress))

        self.customer_email_e.delete(0, END)
        self.customer_email_e.insert(0,str(self.customeremail))

        self.customer_contact_number_e.delete(0, END)
        self.customer_contact_number_e.insert(0,str(self.customernumber))

    def update_cus(self):
        # Updating now the existing datas from database

        self.update_customer_name = self.customer_name_e.get()
        self.update_customer_address = self.customer_address_e.get()
        self.update_customer_email = self.customer_email_e.get()
        self.update_customer_contact_number = self.customer_contact_number_e.get()
        
        update = "UPDATE customers SET customer_name=?, customer_address=?, customer_email=?,  customer_contact_number=? WHERE id_cus=? "
        c.execute(update,(self.update_customer_name,self.update_customer_address,self.update_customer_email,self.update_customer_contact_number,self.idc_e.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "The customer details on database has been updated")

def update_customer():
    window2 = Tk()
    add_customers(window2)
    window2.geometry("963x749+540+110")
    window2.title("Add to database a customer")
    window2.mainloop()
