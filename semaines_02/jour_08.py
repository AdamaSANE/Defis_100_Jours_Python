# Contact Book

# Step: 1: Initialize an empty contact book
contact_book = {}

# Step 2: Display the menu

def display_menu():
    print("\n---- Contact Book Menu ----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Contact")

# Step 3: Add a contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contact_book[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} added successfully.")

# Step 4: View all contacts
def view_contacts():
    if contact_book:
      print("\n---- Contact List ----")
      for name, details in contact_book.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
      else:
         print("Your contact book is empty.")

# Step 5: Search for a contact
def search_contact():
    name = input("Enter contact name to search: ")
    if name in contact_book:
        details = contact_book[name]
        print("\n---- Contact Details ----")
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
    else:
        print(f"Contact {name} not found in your contact book.")

# Step 6: Edit a contact
def edit_contact():
    name = input("Enter contact name to edit: ")
    if name in contact_book:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contact_book[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found in your contact book.")

# Step 7: Delete a contact
def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found in your contact book.")

# Step 8: Main loop to run the contact book application
while True:
    display_menu()
    choice = input("Choose an option (1-6): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        edit_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Thank you for using Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option and try again.")