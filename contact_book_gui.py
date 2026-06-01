from tkinter import *
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    contacts.append({"name": name, "phone": phone})
    messagebox.showinfo("Success", "Contact Added!")

    name_entry.delete(0, END)
    phone_entry.delete(0, END)

def view_contacts():
    listbox.delete(0, END)
    for contact in contacts:
        listbox.insert(END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    search = name_entry.get().lower()

    for contact in contacts:
        if contact["name"].lower() == search:
            messagebox.showinfo(
                "Contact Found",
                f"Name: {contact['name']}\nPhone: {contact['phone']}"
            )
            return

    messagebox.showerror("Not Found", "Contact not found!")
def edit_contact():
    search = name_entry.get().lower()

    for contact in contacts:
        if contact["name"].lower() == search:
            new_name = name_entry.get()
            new_phone = phone_entry.get()

            if new_name == "" or new_phone == "":
                messagebox.showwarning(
                    "Warning",
                    "Enter updated name and phone number!"
                )
                return

            contact["name"] = new_name
            contact["phone"] = new_phone

            messagebox.showinfo("Success", "Contact Updated!")
            view_contacts()
            return

    messagebox.showerror("Not Found", "Contact not found!")

def delete_contact():
    search = name_entry.get().lower()

    for contact in contacts:
        if contact["name"].lower() == search:
            contacts.remove(contact)
            messagebox.showinfo("Deleted", "Contact Deleted!")
            view_contacts()
            return

    messagebox.showerror("Not Found", "Contact not found!")

# Main Window
root = Tk()
root.title("Contact Book")
root.geometry("400x400")

Label(root, text="Name").pack(pady=5)
name_entry = Entry(root, width=30)
name_entry.pack()

Label(root, text="Phone Number").pack(pady=5)
phone_entry = Entry(root, width=30)
phone_entry.pack()

Button(root, text="Add Contact", command=add_contact).pack(pady=5)
Button(root, text="View Contacts", command=view_contacts).pack(pady=5)
Button(root, text="Search Contact", command=search_contact).pack(pady=5)
Button(root, text="Edit Contact", command=edit_contact).pack(pady=5)
Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

listbox = Listbox(root, width=50, height=10)
listbox.pack(pady=10)

root.mainloop()