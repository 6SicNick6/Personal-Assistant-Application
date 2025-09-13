import sqlite3
import tkinter as tk
from tkinter import messagebox

def load_contacts():
    contacts = []
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, phone TEXT)")
    connection.commit()

    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()

    for row in rows:
        contacts.append(row)

    cursor.close()
    connection.close()

    return contacts

def select_contact(event):
    if listbox.curselection():
        index = listbox.curselection()[0]
        selected_contact = contacts[index]
        edit_button.configure(state=tk.NORMAL)
        delete_button.configure(state=tk.NORMAL)
    else:
        selected_contact = None
        edit_button.configure(state=tk.DISABLED)
        delete_button.configure(state=tk.DISABLED)

def add_contact():
    def save_contact():
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()

        if name and email and phone:
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()

            cursor.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))

            connection.commit()
            cursor.close()
            connection.close()

            load_and_display_contacts()
            contact_window.destroy()
        else:
            messagebox.showwarning("Invalid Input", "Please fill in all the fields.")

    contact_window = tk.Toplevel()
    contact_window.title("Contact Details")
    contact_window.geometry("300x200")

    name_label = tk.Label(contact_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(contact_window)
    name_entry.pack(pady=5)

    email_label = tk.Label(contact_window, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(contact_window)
    email_entry.pack(pady=5)

    phone_label = tk.Label(contact_window, text="Phone:")
    phone_label.pack()
    phone_entry = tk.Entry(contact_window)
    phone_entry.pack(pady=5)

    save_button = tk.Button(contact_window, text="Save", command=save_contact)
    save_button.pack(pady=5)

def edit_contact():
    def save_contact():
        nonlocal selected_contact
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()

        if name and email and phone:
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()

            cursor.execute("UPDATE contacts SET name=?, email=?, phone=? WHERE id=?", (name, email, phone, selected_contact[0]))

            connection.commit()
            cursor.close()
            connection.close()

            load_and_display_contacts()
            contact_window.destroy()
        else:
            messagebox.showwarning("Invalid Input", "Please fill in all the fields.")

    selected_contact = contacts[listbox.curselection()[0]] if listbox.curselection() else None

    contact_window = tk.Toplevel()
    contact_window.title("Contact Details")
    contact_window.geometry("300x200")

    name_label = tk.Label(contact_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(contact_window)
    name_entry.pack(pady=5)

    email_label = tk.Label(contact_window, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(contact_window)
    email_entry.pack(pady=5)

    phone_label = tk.Label(contact_window, text="Phone:")
    phone_label.pack()
    phone_entry = tk.Entry(contact_window)
    phone_entry.pack(pady=5)

    if selected_contact:
        name_entry.insert(tk.END, selected_contact[1])
        email_entry.insert(tk.END, selected_contact[2])
        phone_entry.insert(tk.END, selected_contact[3])

    save_button = tk.Button(contact_window, text="Save", command=save_contact)
    save_button.pack(pady=5)

def delete_contact():
    selected_contact = contacts[listbox.curselection()[0]] if listbox.curselection() else None

    if selected_contact:
        connection = sqlite3.connect("contacts.db")
        cursor = connection.cursor()

        cursor.execute("DELETE FROM contacts WHERE id=?", (selected_contact[0],))

        connection.commit()
        cursor.close()
        connection.close()

        load_and_display_contacts()

def load_and_display_contacts():
    contacts = load_contacts()
    listbox.delete(0, tk.END)
    for contact in contacts:
        contact_info = f"{contact[1]}       {contact[2]}        {contact[3]}"
        listbox.insert(tk.END, contact_info)

root = tk.Tk()
root.title("Contact App")
root.geometry("600x300")  # Updated width of the root window

contacts = load_contacts()
selected_contact = None

listbox = tk.Listbox(root, width=50)  # Increased width of the listbox
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", select_contact)

load_and_display_contacts()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Contact", state=tk.DISABLED, command=edit_contact)
edit_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Contact", state=tk.DISABLED, command=delete_contact)
delete_button.pack(pady=5)

root.mainloop()