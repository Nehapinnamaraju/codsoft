import json
import tkinter as tk
from tkinter import messagebox

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=2)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    save_contacts(contacts)
    messagebox.showinfo("Contact Book", "Contact added successfully.")
    clear_entries()

def view_contacts():
    result_text.delete(1.0, tk.END)
    for i, contact in enumerate(contacts, 1):
        result_text.insert(tk.END, f"{i}. {contact['name']} - {contact['phone']}\n")

def search_contact():
    result_text.delete(1.0, tk.END)
    search_term = search_entry.get().lower()
    found_contacts = []
    for contact in contacts:
        if search_term in contact["name"].lower() or search_term in contact["phone"]:
            found_contacts.append(contact)

    if found_contacts:
        for i, contact in enumerate(found_contacts, 1):
            result_text.insert(tk.END, f"{i}. {contact['name']} - {contact['phone']}\n")
    else:
        result_text.insert(tk.END, "No matching contacts found.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def on_contact_select(event):
    selected_contact = result_text.get(tk.SEL_FIRST, tk.SEL_LAST)
    if selected_contact:
        selected_index = int(selected_contact.split(".")[0]) - 1
        contact = contacts[selected_index]
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        name_entry.insert(0, contact["name"])
        phone_entry.insert(0, contact["phone"])
        email_entry.insert(0, contact["email"])
        address_entry.insert(0, contact["address"])

def update_contact():
    selected_contact = result_text.get(tk.SEL_FIRST, tk.SEL_LAST)
    if selected_contact:
        selected_index = int(selected_contact.split(".")[0]) - 1
        contact = contacts[selected_index]
        contact["name"] = name_entry.get()
        contact["phone"] = phone_entry.get()
        contact["email"] = email_entry.get()
        contact["address"] = address_entry.get()
        save_contacts(contacts)
        messagebox.showinfo("Contact Book", "Contact updated successfully.")
        view_contacts()
    else:
        messagebox.showwarning("Contact Book", "Please select a contact to update.")

def delete_contact():
    selected_contact = result_text.get(tk.SEL_FIRST, tk.SEL_LAST)
    if selected_contact:
        selected_index = int(selected_contact.split(".")[0]) - 1
        deleted_contact = contacts.pop(selected_index)
        save_contacts(contacts)
        messagebox.showinfo("Contact Book", f"{deleted_contact['name']} deleted successfully.")
        view_contacts()
        clear_entries()
    else:
        messagebox.showwarning("Contact Book", "Please select a contact to delete.")

# Main program
contacts = load_contacts()

root = tk.Tk()
root.title("Contact Book")

# Labels
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Phone:").grid(row=1, column=0, sticky="w")
tk.Label(root, text="Email:").grid(row=2, column=0, sticky="w")
tk.Label(root, text="Address:").grid(row=3, column=0, sticky="w")

# Entry Widgets
name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)
address_entry = tk.Entry(root)

name_entry.grid(row=0, column=1, padx=5, pady=5)
phone_entry.grid(row=1, column=1, padx=5, pady=5)
email_entry.grid(row=2, column=1, padx=5, pady=5)
address_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
view_button = tk.Button(root, text="View Contacts", command=view_contacts)
search_button = tk.Button(root, text="Search Contact", command=search_contact)
update_button = tk.Button(root, text="Update Contact", command=update_contact)
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)

add_button.grid(row=4, column=0, columnspan=2, pady=10)
view_button.grid(row=5, column=0, columnspan=2, pady=10)
search_button.grid(row=6, column=0, columnspan=2, pady=10)
update_button.grid(row=7, column=0, columnspan=2, pady=10)
delete_button.grid(row=8, column=0, columnspan=2, pady=10)

# Result Text
result_text = tk.Text(root, height=10, width=40)
result_text.grid(row=0, column=2, rowspan=9, padx=10)

# Search Entry
search_entry = tk.Entry(root)
search_entry.grid(row=9, column=0, padx=5, pady=5)
search_entry.bind("<Return>", lambda event: search_contact())

# Event Binding
result_text.bind("<ButtonRelease-1>", on_contact_select)

root.mainloop()
