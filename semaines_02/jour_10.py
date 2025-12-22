# Note-Taking App

# Step 1: Define file name
file_name = "notes.txt"

# Step 2: Display menu options
def display_menu():
    print("\n --- Note-Taking App Menu --- ")
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Delete all notes")
    print("4. Exit")

# Step 3: Add a new note
def add_note():
    note = input("Enter your note: ")
    with open(file_name, "a") as file:
        file.write(note + "\n")
    print("Note added successfully.")

# Step 4: View all notes
def view_notes():
    try:
        with open(file_name, "r") as file:
            notes = file.read()
            if notes:
                print("\n--- Your Notes ---")
                print(notes)
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes found.")

# Step 5: Delete all notes
def delete_notes():
    confirm = input("Are you sure you want to delete all notes? (yes/no): ")
    if confirm.lower() == "yes":  
      with open(file_name, "w") as file:
        pass  # Overwrite the file with nothing to delete all notes 
      print("All notes deleted successfully.")
    else: 
      print("Deletion cancelled.") 

# Step 6: Main program loop
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("Exiting the Note-Taking App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
 