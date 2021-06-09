from tkinter import *
import sqlite3
import tkinter.messagebox

#connecting with sql
conn = sqlite3.connect("D:\FINAL APOLAKI\Apolaki Final\Database\store.db")


#creating curser to be able to communicate with sql
c = conn.cursor()


# for plants checking how many plants in database
result= c.execute("SELECT  Max(id_plant)from plants")
for plants in result:
    id_plant = plants[0]

  
class add_plants:
    def __init__(self,master):

        self.master = master
        self.heading = Label(master)
        self.heading = Label(master, text="Update plants from database", font = ('arial 20 bold'), fg ='green')
        self.heading.place(x=280,y=0)
        #----------------------------------------------
        
        # Labels for id of plants
        self.id_l = Label(master, text=  "Input ID: ", font = ('arial 12 bold'))
        self.id_l.place(x = 25, y=50)

        # Entries for id of plants
        self.id_e = Entry(master, width = 25, font = ('arial 12'))
        self.id_e.place(x=250, y=50)

        # Button for search

        self.button_to_search = Button(master, text = "Search ID", width = 10, height = 1, bg = 'green', fg='white', command = self.search_id)
        self.button_to_search.place(x=500, y=50)

        #------------------------------------------------------

        # Labels for this window

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
        self.button_to_add = Button(master, text = "Update Plant", width = 25, height = 6, bg = 'green', fg='white', command=self.update)
        self.button_to_add.place(x=25, y=250)

        # Text box for the logs
        self.textbox = Text(master, width=113,height=11)
        self.textbox.place(x=25, y=400)

        # To check how many items now  using text box

        # for plants checking how many plants in database
        result = c.execute("SELECT plant_name FROM plants")
        id_plant = result.fetchall()
        self.textbox.insert(1.0, "The items in inventory are: \n")
        for plant in id_plant:
            self.textbox.insert(END, plant[0] + "\n")

    def search_id(self):
        # Note: The " * " below means "everything" in sql
        sql = "SELECT * FROM plants WHERE id_plant=?"
        result = c.execute(sql,(self.id_e.get(), ))
        for r in result:
            self.plantname =r[1] #[1] is the name in database while [0] is the ID
            self.planttype =r[2]
            self.plantprice =r[3]
            self.plantquantity =r[4]
        conn.commit()

        # Now inserting the existing datas from database to entries/textbox to update
        self.plant_name_e.delete(0, END) # We need a delete so that the "searched" plant from database will be removed
        self.plant_name_e.insert(0,str(self.plantname))

        self.plant_type_e.delete(0, END)
        self.plant_type_e.insert(0,str(self.planttype))

        self.plant_price_e.delete(0, END)
        self.plant_price_e.insert(0,str(self.plantprice))

        self.plant_quantity_e.delete(0, END)
        self.plant_quantity_e.insert(0,str(self.plantquantity))

    def update(self):
        # Updating now the existing datas from database

        self.update_plant_name = self.plant_name_e.get()
        self.update_plant_type = self.plant_type_e.get()
        self.update_plant_price = self.plant_price_e.get()
        self.update_plant_quantity = self.plant_quantity_e.get()

        # Note that query is like asking an access to the database/sql for the set of data
        # Used for updating a data on database
        
        update = "UPDATE plants SET plant_name=?, plant_type=?, plant_price=?,  plant_quantity=? WHERE id_plant=? "
        c.execute(update,(self.update_plant_name,self.update_plant_type,self.update_plant_price,self.update_plant_quantity,self.id_e.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "The plant details on database has been updated")
        
def update_plant():
    window3 = Tk()
    add_plants(window3)
    window3.geometry("963x749+540+110")
    window3.title("Update plant details")
    window3.mainloop()
        
        
    
#window3 = Tk()
#add_a_plants = add_plants(window3)
#window3.geometry("963x749+540+110")
#window3.title("Update plant details")
#window3.mainloop()
