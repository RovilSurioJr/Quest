from tkinter import *
import sqlite3
import tkinter.messagebox
import math
import datetime
import os #for directory check in generating receipt
import random #for random number in filename

conn = sqlite3.connect("D:\FINAL APOLAKI\Apolaki Final\Database\store.db")
c = conn.cursor()
#date
date = datetime.datetime.now().date()

# pack()geometry manager organizes widgets in BLOCKS(LEFT,RIGHT ETC) before placing them in the parent widget.
# The Frame widget is used as a container widget to organize other widgets.

plant_list = []
plant_price = []
plant_quantity = []
plant_id = []
apolaki_total_sales = []

# List for labels in add to cart() to clear it after generating receipt
# This is in global in order to access it on generate receipt ()
labels_list = []


class Application:
    def __init__(self,master):
       
        self.master = master
        self.pack_on_left = Frame(master, width=700, height=800, bg ='white') # Frames
        self.pack_on_left.pack(side=LEFT)
        
        self.pack_on_right = Frame(master, width=380, height=800, bg ='lightgreen') #The remaining width
        self.pack_on_right.pack(side=RIGHT)

        # Components
        self.heading = Label(self.pack_on_left, text = "Apolaki Garden Bro", font=('arial 18 bold'),bg='white')
        self.heading.place(x=200, y=0)

        # Plant details for cart section
        self.products = Label(self.pack_on_right, text = "Plants", font = ('arial 12 bold'),bg='lightgreen',fg='black')
        self.products.place(x=20,y=60)

        self.quantity = Label(self.pack_on_right, text = "Quantity", font = ('arial 12 bold'),bg='lightgreen',fg='black')
        self.quantity.place(x=85,y=60)

        self.price = Label(self.pack_on_right, text = "Amount", font = ('arial 12 bold'),bg='lightgreen',fg='black')
        self.price.place(x=175,y=60)

        self.choose_customer_l = Label(self.pack_on_left, text="Input customer name: ", font=('arial 12 '),
                                       bg='white')
        self.choose_customer_l.place(x=5, y=50)

        self.choose_customer_e = Entry(self.pack_on_left, width=25, font=('arial 12'), bg='white')
        self.choose_customer_e.place(x=200, y=50)
        self.button_to_select_customer = Button(self.pack_on_left, text="Check Customer", width=12, height=1,
                                                bg='lightgreen',
                                                command=self.customer_check_if_in_the_db)
        self.button_to_select_customer.place(x=450, y=50)
        self.choose_customer_e.focus()

        self.check_customer_b = Button(self.pack_on_left, text="Customer List", width=12, height=1,
                                       bg='lightgreen',
                                       command=self.show_registered_customers)

        self.check_customer_b.place(x=550, y=50)
        # self.chooseplant_e.focus() # This focus method gives a focus on this specific widget around the window
        # Without the focus() you need to click the text box in order to start typing

    def display_plant_buttons(self):

        # Entering what to buy
        # Label

        self.chooseplant_l = Label(self.pack_on_left, text="Input plant name: ", font=('arial 12'), bg='white')
        self.chooseplant_l.place(x=5, y=200)

        # Entry

        self.chooseplant_e = Entry(self.pack_on_left, width=25, font=('arial 12'), bg='white')
        self.chooseplant_e.place(x=200, y=200)

        # Button to show plant details
        self.button_to_show_plant_details = Button(self.pack_on_left, text="Show details", width=12, height=1,
                                                    bg='lightgreen', command=self.get_plant_details)
        self.button_to_show_plant_details.place(x=450, y=200)

        # Button show all available plants

        self.button_for_available_plants = Button(self.pack_on_left, text="Show available plants", width=16, height=1,
                                                  bg='lightgreen', command=self.show_all_avail_plants)
        self.button_for_available_plants.place(x=550, y=200)

        # To be fill by the function "get_plant_details" below

        self.plant_name = Label(self.pack_on_left, text="", font=('arial 12 bold'), bg='white')
        self.plant_name.place(x=225, y=375)

        self.plant_type = Label(self.pack_on_left, text="", font=('arial 12 bold'), bg='white')
        self.plant_type.place(x=225, y=400)

        self.plant_price = Label(self.pack_on_left, text="", font=('arial 12 bold'), bg='white')
        self.plant_price.place(x=250, y=450)

        # TOTAL amount to pay
        # Label
        self.total_l = Label(self.pack_on_right, text="", font=('arial 12 bold'), bg='lightgreen', fg='black')
        self.total_l.place(x=30, y=500)  # This is configured below the add to cart ()

    def get_plant_details(self):
        self.get_plant_name = self.chooseplant_e.get()
        # Accessing database

        get = "SELECT * FROM plants WHERE plant_name =?"
        result = c.execute(get, (
        self.get_plant_name,))  # the purpose of self.get_plant_name here is to pass it to the "plant_name =?" to search on tables

        for row in result:
            self.get_id_plant = row[0]
            self.get_plant_name = row[1]  # remember, the "id" is in index 0 in out table in sql
            self.get_plant_type = row[2]
            self.get_plant_price = row[3]
            self.get_plant_quantity = row[4]

        # setting thhe values of the "text" on the lines above this function

        self.plant_name.configure(text="Plant name: " + str(self.get_plant_name))
        self.plant_type.configure(text="Plant type: " + str(self.get_plant_type))
        self.plant_price.configure(text="Price: " + str(self.get_plant_price))

        # label of qty
        self.enter_quantity_l = Label(self.pack_on_left, text="Enter Quantity: ", font=('arial 12 bold'), bg='white')
        self.enter_quantity_l.place(x=5, y=500)

        # Entry of qty

        self.enter_quantity_e = Entry(self.pack_on_left, width=25, font=('arial 12'), bg='white')
        self.enter_quantity_e.place(x=150, y=500)
        self.enter_quantity_e.focus()

        # button to add to cart

        self.add_to_cart_button = Button(self.pack_on_left, text="Add to cart", width=10, height=1, bg='lightgreen',
                                         command=self.add_to_cart)
        self.add_to_cart_button.place(x=400, y=500)

        # Generate change label and entry

        self.enter_change_l = Label(self.pack_on_left, text="Given amount: ", font=('arial 12 bold'), bg='white')
        self.enter_change_l.place(x=5, y=550)

        self.enter_change_e = Entry(self.pack_on_left, width=25, font=('arial 12'), bg='white')
        self.enter_change_e.place(x=150, y=550)

        # Button for change

        self.button_for_change = Button(self.pack_on_left, text="Calculate change", width=15, height=1, bg='lightgreen',
                                        command=self.change_of_customer)
        self.button_for_change.place(x=400, y=550)

        # Button for receipt

        self.button_for_receipt = Button(self.pack_on_left, text="Print receipt", width=15, height=1, bg='lightgreen',
                                         command=self.generate_receipt)
        self.button_for_receipt.place(x=260, y=600)

    def customer_check_if_in_the_db(self):
        self.chosen_customer = self.choose_customer_e.get()
        # with conn:
        all_customer_names = []
        c.execute("SELECT * FROM customers")
        all_customers = c.fetchall()

        for i in range(len(all_customers)):
            all_customer_names.append(all_customers[i][1])
        for name in all_customer_names:
            if self.chosen_customer == name:
                register = Label(self.pack_on_left, text="REGISTERED", font=('arial 12'),
                                                fg='red')
                register.place(x=5, y=75)
                self.display_plant_buttons()
        if self.chosen_customer not in all_customer_names:
            tkinter.messagebox.showinfo("Error","Customer is not registered")



    def show_registered_customers(self):
        # with conn:
        all_customer_names = []
        c.execute("SELECT * FROM customers")
        all_customers = c.fetchall()
        for i in range(len(all_customers)):
            all_customer_names.append(all_customers[i][1])


        customer_listbox = Listbox(self.pack_on_left,width=74,height = 7)
        customer_listbox.place(x=200,y=80)
        for customer_name in all_customer_names:
            customer_listbox.insert(END,customer_name)

    def show_all_avail_plants(self):
        # with conn:
        all_plants_name = []
        c.execute("SELECT * FROM plants")
        all_plants = c.fetchall()
        for i in range(len(all_plants)):
            all_plants_name.append(all_plants[i][1])
        my_listbox = Listbox(self.pack_on_left,width=74,height= 7)
        my_listbox.place(x=200,y=230)

        for plant_name in all_plants_name:
            my_listbox.insert(END,plant_name)
                


    def add_to_cart(self):
        # Getting the value from the quantity entered by the user
        self.quantity_value = int(self.enter_quantity_e.get())
        if self.quantity_value > int(self.get_plant_quantity):
            tkinter.messagebox.showinfo("Error", "The stocks of this plant is not enough")
        else:
            # Calculating the price
            self.total_price = float(self.quantity_value)* float(self.get_plant_price)
            # Appending to global list
            plant_list.append(self.get_plant_name)
            plant_price.append(self.total_price)
            plant_quantity.append(self.quantity_value)
            plant_id.append(self.get_id_plant)

            # Just to check on console
            
            print(plant_list)
            print(plant_price)
            print(plant_quantity)
            print(plant_id)

            # The y_index is for the placement on the right side of gui per plant order

            self.y_index = 80
            self.index = 0 #in order to move on the list
            for plant in plant_list:
                self.temp_plant = Label(self.pack_on_right, text = plant, font=('arial 12 bold'), bg = 'lightgreen', fg='White')
                self.temp_plant.place(x= 20, y = self.y_index)
                labels_list.append(self.temp_plant)

                self.temp_quantity = Label(self.pack_on_right, text = str(plant_quantity[self.index]), font=('arial 12 bold'), bg = 'lightgreen', fg='White')
                self.temp_quantity.place(x = 100, y = self.y_index)
                labels_list.append(self.temp_quantity)

                self.temp_price = Label(self.pack_on_right, text = str(plant_price[self.index]), font=('arial 12 bold'), bg = 'lightgreen', fg='White')
                self.temp_price.place(x = 175, y = self.y_index)
                labels_list.append(self.temp_price)

                self.y_index += 30 #To make the printing of the order moves down per order
                self.index += 1  #in order to move on the index on the list per order

                #Total configuration

                self.total_l.configure(text = "Total: " + str(sum(plant_price)))

                #removing labels created by ordering using place_forget() from tkinter
                self.enter_quantity_l.place_forget()
                self.enter_quantity_e.place_forget()
                self.add_to_cart_button.place_forget()

                #Configuring the plant details to empty to clean it on screen
                self.plant_name.configure(text="")
                self.plant_type.configure(text="")
                self.plant_price.configure(text="")

                #Auto focus/delete method in chooseplant_e/entered PLANT NAME in its entrybox
                self.chooseplant_e.focus()
                self.chooseplant_e.delete(0,END)


    def change_of_customer(self):
        # get the amount given by the customer and total amount to pay

        self.amount_given_by_customer = float(self.enter_change_e.get())
        self.the_total = float(sum(plant_price))

        if self.amount_given_by_customer >= self.the_total:
            self.total_change  = self.amount_given_by_customer - self.the_total

            # Label change

            self.customer_change = Label(self.pack_on_left, text = "Change: " + str(self.total_change),font = ('arial 12 bold'), bg = 'white')
            self.customer_change.place(x=5,y=600)
        else:
            tkinter.messagebox.showinfo("Error", "Not enough funds")

    def generate_receipt(self):

        # Creating a receipt before updating QUANTITY/STOCK
        # Choosing the path of generated receipt
        directory = "D:/FINAL APOLAKI/Apolaki Final/Invoice/" + str(date) + "/"

        if not os.path.exists(directory):
            os.makedirs(directory)
        # Template for receipt

        garden_name = "\t\t\t\t Apolaki Community Garden\n"
        address = "\t\t\t\t Philippines, Manila\n"
        phone = "\t\t\t\t\t 09321401\n"
        sample = "\t\t\t\t\t Invoice\n"
        dt = "\t\t\t\t\t" + str(date)

        table_header = "\n\n\t\t-----------------------------------------------\n\t\tSN.\t\tProducts\t\tQty\t\tAmount\n\t\t-----------------------------------------------"
        final_format_receipt = garden_name + address + phone + sample + dt + table_header

        file_name = str(directory)+ str(random.randrange(5000,10000)) + ".rtf" #generating random file name number/filetype
        file = open(file_name, 'w') #'w' = write
        file.write(final_format_receipt)

        # Getting the actual data
        # Only the 7 characters [:7];it will filled by "...." if not 7 so that the format still ok
        index = 0
        r = 1
        for plant in plant_list:
            file.write("\n\t\t" + str(r) + "\t\t"  + str(plant_list[index] + "......")[:7] + "\t\t" + str(plant_quantity[index]) + "\t\t" + str(plant_price[index]))
            index += 1
            r += 1
        file.write("\n\n\t\tCustomer name: " + self.chosen_customer)
        file.write("\n\n\t\t\t\t\t\t\t\tTotal: " + str(sum(plant_price)))
        file.write("\n\n\t\t\t\t\t\t\t\tTotal Paid: " + str(self.amount_given_by_customer))
        file.write("\n\n\t\t\t\t\t\t\t\tTotal Change: " + str(self.total_change))
        file.write("\n\t\t\t\tThanks for purchasing.")
        file.close()
                
        # Accessing the database again to update
        # note that "plant_id" below is the global list created
        # note that "plant_quantity" below is the global list

        # UPDATING THE QUANTITY/STOCK
        
        self.index_of_plant_id = 0 

        selecting = "SELECT * FROM plants WHERE id_plant=?"
        result = c.execute(selecting,(plant_id[self.index_of_plant_id],)) 
 
        for i in plant_list:
            for index_of_quantity in result:
                self.original_quantity = index_of_quantity[4] # 4 index in table/database
            
            self.new_quantity_of_plant = int(self.original_quantity) - int(plant_quantity[self.index_of_plant_id])

            sql = "UPDATE plants SET plant_quantity=? WHERE id_plant=?"
            c.execute(sql,(self.new_quantity_of_plant, plant_id[self.index_of_plant_id]))
            conn.commit()
     

            # INSERTING TO TRANSACTION TABLE IN DATABASE
            sql2 = "INSERT INTO transactions (plant_name,plant_quantity,amount,date) VALUES(?,?,?,?)"
            c.execute(sql2,(plant_list[self.index_of_plant_id],plant_quantity[self.index_of_plant_id],plant_price[self.index_of_plant_id],date))
            conn.commit()                      

            print("Decreased")
            self.index_of_plant_id += 1

        #Destroying everything labels created by ordering
        for i in labels_list:
            i.destroy()
        #Deleting also the list to for the next customer after generating receipt
        del(plant_list[:])
        del(plant_price[:])
        del(plant_quantity[:])
        del(plant_id[:])

        self.total_l.configure(text="")
        self.enter_change_l.configure(text="")
        self.enter_change_e.delete(0,END)
        self.chooseplant_e.focus() # Again to focus on input plant name entry box

        tkinter.messagebox.showinfo("Success", "Processed order")

def transaction():
    window  = Tk()
    Application(window)

    window.geometry("963x749+540+110")
    window.title("App")
    window.mainloop()

    

       

        
        
        
            


            
#if __name__ == '__main__':

    #window  = Tk()
    #app = Application(window)

    #window.geometry("963x749+540+110")
    #window.title("App")
    #window.mainloop()
