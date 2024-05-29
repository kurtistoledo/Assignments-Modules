# Lesson 1: Overview of Modules In Python
# 2. Exploring Python Modules and Data Structures Assignment

contacts = []

def add_contact(name, phone, email):
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)
    return f"Contact {name} added successfully."

def remove_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'] != name]
    return f"Contact {name} removed successfully."

def display_contacts():
    if not contacts:
        return "No contacts found."
    contact_list = "\n".join([f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}" for contact in contacts])
    return contact_list

import Task1_2

def main():
    while True:
        print("""
        Contact List Manager
        1. Add Contact
        2. Remove Contact
        3. Display Contacts
        4. Quit
        """)
        choice = input("Select an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            print(Task1_2.add_contact(name, phone, email))
        
        elif choice == '2':
            name = input("Enter the name of the contact to remove: ")
            print(Task1_2.remove_contact(name))
        
        elif choice == '3':
            print(Task1_2.display_contacts())
        
        elif choice == '4':
            print("Exiting Contact List Manager. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
