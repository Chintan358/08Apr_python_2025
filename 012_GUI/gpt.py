import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ---------- MySQL Connection ----------
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # Change if needed
    password="root",        # Change if needed
    database="08apr_py"
)
cursor = conn.cursor()

# ---------- Functions ----------
def show_records():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM reg")
    for record in cursor.fetchall():
        tree.insert('', tk.END, values=record)

def add_record():
    name = name_var.get()
    email = email_var.get()
    if name and email:
        cursor.execute("INSERT INTO reg (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        messagebox.showinfo("Success", "Record added successfully!")
        show_records()
        clear_fields()
    else:
        messagebox.showerror("Error", "All fields are required.")

def update_record():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select a record to update.")
        return
    record_id = tree.item(selected, 'values')[0]
    name = name_var.get()
    email = email_var.get()
    if name and email:
        cursor.execute("UPDATE reg SET name=%s, email=%s WHERE id=%s", (name, email, record_id))
        conn.commit()
        messagebox.showinfo("Success", "Record updated successfully!")
        show_records()
        clear_fields()
    else:
        messagebox.showerror("Error", "All fields are required.")

def delete_record():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select a record to delete.")
        return
    record_id = tree.item(selected, 'values')[0]
    cursor.execute("DELETE FROM reg WHERE id=%s", (record_id,))
    conn.commit()
    messagebox.showinfo("Deleted", "Record deleted successfully!")
    show_records()
    clear_fields()

def load_record(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, 'values')
        name_var.set(values[1])
        email_var.set(values[2])

def clear_fields():
    name_var.set("")
    email_var.set("")

# ---------- UI Setup ----------
root = tk.Tk()
root.title("Modern Tkinter MySQL CRUD")
root.geometry("700x550")
root.resizable(False, False)
root.configure(bg="#E1EFF6")  # Attractive soft blue background

# ---------- Fonts & Styles ----------
style = ttk.Style()
style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background="#f2f2f2")
style.configure("Treeview", font=("Segoe UI", 10), rowheight=25)
style.map("Treeview", background=[("selected", "#A7D1F5")])

# ---------- Variables ----------
name_var = tk.StringVar()
email_var = tk.StringVar()

# ---------- Title ----------
tk.Label(root, text="🌐 User Management System", font=("Segoe UI", 18, "bold"), bg="#E1EFF6", fg="#2B3A55").pack(pady=15)

# ---------- Form Frame ----------
form_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="ridge")
form_frame.pack(pady=10, padx=20, fill="x")

tk.Label(form_frame, text="Name", font=("Segoe UI", 11), bg="#ffffff").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Entry(form_frame, textvariable=name_var, font=("Segoe UI", 11), width=30, bd=2, relief="groove").grid(row=0, column=1, padx=10)

tk.Label(form_frame, text="Email", font=("Segoe UI", 11), bg="#ffffff").grid(row=1, column=0, padx=10, pady=10, sticky="e")
tk.Entry(form_frame, textvariable=email_var, font=("Segoe UI", 11), width=30, bd=2, relief="groove").grid(row=1, column=1, padx=10)

# ---------- Buttons ----------
btn_frame = tk.Frame(root, bg="#E1EFF6")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="➕ Add", font=("Segoe UI", 10, "bold"), bg="#4CAF50", fg="white", width=12, command=add_record).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="✏️ Update", font=("Segoe UI", 10, "bold"), bg="#2196F3", fg="white", width=12, command=update_record).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="❌ Delete", font=("Segoe UI", 10, "bold"), bg="#f44336", fg="white", width=12, command=delete_record).grid(row=0, column=2, padx=10)
tk.Button(btn_frame, text="🔄 Clear", font=("Segoe UI", 10, "bold"), bg="#9E9E9E", fg="white", width=12, command=clear_fields).grid(row=0, column=3, padx=10)

# ---------- Table Frame ----------
table_frame = tk.Frame(root, bg="#E1EFF6")
table_frame.pack(pady=20, padx=20, fill="both", expand=True)

cols = ("ID", "Name", "Email")
tree = ttk.Treeview(table_frame, columns=cols, show="headings", height=8)
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=200)
tree.pack(fill="x")
tree.bind('<<TreeviewSelect>>', load_record)

# ---------- Run ----------
show_records()
root.mainloop()
