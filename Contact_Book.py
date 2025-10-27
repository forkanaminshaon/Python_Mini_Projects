# Python Contact Book Application

contact = {}

def ShowFunction():
    print(contact.items())
    print("Name \t Contact")
    for key in contact:
        print("{} \t {}".format(key, contact.get(key)))

while True:
    choice = input("1. Add New Contact \n"
                   "2. Search the Contact \n"
                   "3. Display All Contacts \n"
                   "4. Edit The Contact \n"
                   "5. Delete the Contact \n"
                   "6. Exit \n"
                   "Please Write Number Between 1-6: ")
    
    if choice == '1':
        name = input("Enter Contact Name: ")
        phone = input("Enter Contact Phone Number: ")
        contact[name] = phone
        print(f"Contact {name} added successfully.")
    
    elif choice == '2':
        name = input("Enter Contact Name to Search: ")
        if name in contact:
            print(f"Contact Found: {name} - {contact[name]}")
        else:
            print("Contact Not Found.")
            
    elif choice == '3':
        if contact:
            print("All Contacts:")
            for name, phone in contact.items():
                print(f"{name} - {phone}")
        else:
            print("No Contacts Available.")     
    
    elif choice == '4': 
        EditContact = input("Enter Contact Name to Edit: ")
        if EditContact in contact:
            new_phone = input("Enter New Phone Number: ")
            contact[EditContact] = new_phone
            print(f"Contact {EditContact} updated successfully.")
        else:
            print("Contact Not Found.") 
    
    elif choice == '5':
        DeleteContact = input("Enter Contact Name to Delete: ")
        if DeleteContact in contact:
            del contact[DeleteContact]
            print(f"Contact {DeleteContact} deleted successfully.")
        else:
            print("Contact Not Found.")         
            
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1-6.")
