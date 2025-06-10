
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import ttk
import mysql.connector 
# A simple CRUD application using Tkinter in Python
# This application allows you to create, read, update, and delete records
# Note: This is a basic structure; you will need to implement the actual CRUD functionality.
def create_record():
    # Function to create a new record
    id = id_entry.get()
    name = name_entry.get()
    email = email_entry.get()
    if id and name and email:
        print(f"Record created: ID={id}, Name={name}, Email={email}")
        # Here you would typically add the record to a database or a list
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="08apr_py"
        )
        cursur = conn.cursor()
        query = "INSERT INTO reg (id, name, email) VALUES (%s, %s, %s)"
        values = (id, name, email)
        cursur.execute(query, values)
        conn.commit()
        cursur.close()
        conn.close()
        messagebox.showinfo("Success", "Record created successfully!")
        # For demonstration, we will just clear the entries
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        email_entry.delete(0, END)
        # Refresh the records in the Treeview
        for item in tree.get_children():
            tree.delete(item)
        show_records()
    else:
        print("Please fill all fields to create a record.")
    

def show_records():
    conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="08apr_py"
    )
    cursur = conn.cursor()
    query = "SELECT * FROM reg"
    cursur.execute(query)
    records = cursur.fetchall()
    for record in records:
        print(record)
        tree.insert("", "end", values=record)
    cursur.close()
    conn.close()

def getdata(event):
    # Function to get data from the Treeview when a record is double-clicked
    selected_item = tree.selection()[0]
    item_data = tree.item(selected_item, 'values')  
    id_entry.delete(0, END)
    id_entry.insert(0, item_data[0])
    name_entry.delete(0, END)
    name_entry.insert(0, item_data[1])
    email_entry.delete(0, END)
    email_entry.insert(0, item_data[2])

def update_record():
    # Function to update an existing record
    id = id_entry.get()
    name = name_entry.get()
    email = email_entry.get()
    if id and name and email:
        # print(f"Record updated: ID={id}, Name={name}, Email={email}")
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="08apr_py"
        )
        cursur = conn.cursor()
        query = "UPDATE reg SET name=%s, email=%s WHERE id=%s"
        values = (name, email, id)
        cursur.execute(query, values)
        conn.commit()
        cursur.close()
        conn.close()
        messagebox.showinfo("Success", "Record updated successfully!")
        # Refresh the records in the Treeview
        for item in tree.get_children():
            tree.delete(item)
        show_records()
    else:
        print("Please fill all fields to update a record.")

def delete_record():
    # Function to delete a record
    id = id_entry.get()
    if id:
        # print(f"Record deleted: ID={id}")
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="08apr_py"
        )
        cursur = conn.cursor()
        query = "DELETE FROM reg WHERE id=%s"
        cursur.execute(query, (id,))
        conn.commit()
        cursur.close()
        conn.close()
        messagebox.showinfo("Success", "Record deleted successfully!")
        # Refresh the records in the Treeview
        for item in tree.get_children():
            tree.delete(item)
        show_records()
    else:
        print("Please enter an ID to delete a record.")

root = Tk()
root.title("CRUD Application")
root.geometry("500x500")

id_label = Label(root, text="ID")
id_label.place(x=20, y=20)

id_entry = Entry(root)
id_entry.place(x=100, y=20)

name_label = Label(root, text="Name")
name_label.place(x=20, y=60)
name_entry = Entry(root)
name_entry.place(x=100, y=60)

email_label = Label(root, text="Email")
email_label.place(x=20, y=100)
email_entry = Entry(root)
email_entry.place(x=100, y=100)

Button(root, text="Create",command=create_record).place(x=20, y=140)
Button(root, text="Update",command=update_record).place(x=100, y=140)
Button(root, text="Delete",command=delete_record).place(x=180, y=140)

columns = ("ID", "Name", "Email")
tree = ttk.Treeview(root, columns=columns, show='headings')
# Adding headings to the Treeview
for col in columns:
    tree.heading(col, text=col)
    tree.place(x=20, y=180, width=450, height=250)


tree.bind('<Double-Button-1>',getdata)

show_records()

# Function to show records in the Treeview




root.mainloop()

