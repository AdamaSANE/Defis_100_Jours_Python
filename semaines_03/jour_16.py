# Daily Journal Logger

# Step 1: Define the journal file 
JOURNAL_FILE = "daily_journal.txt"

# Step 2: Add a new entry to the journal
def add_entry():
    entry = input("Write your journal entry for today:\n")
    with open(JOURNAL_FILE, "a") as file:
        file.write(entry + "\n")
    print("Entry added to the journal.")

# Step 3: View all journal entries
def view_entries():
    try:
        with open(JOURNAL_FILE, "r") as file:
            content = file.read()
            if content:
                print("\n--- Your Journal Entries ---")
                print(content)
            else:
                print("No entries found in the journal. Start by adding an entry.")
    except FileNotFoundError:
        print("No journal file found. Add an entry first!")

# Step 4: Search for a keyword in the journal
def search_entries():
    keyword = input("Enter a keyword to search for in your journal:\n").lower()
    try:
        with open(JOURNAL_FILE, "r") as file:
            content = file.readlines()
            found = False
            print("\n--- Search Results ---")
            for entry in content:
                if keyword in entry.lower():
                    print(entry.strip())
                    found = True
            if not found:
                print("No entries found containing the keyword.")
    except FileNotFoundError:
        print("No journal file found. Add an entry first!")

# Step 5: Display Menu
def display_menu():
    print("\n--- Daily Journal Logger ---")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Search entries by keyword")
    print("4. Exit")
        
# Step 6: Main program loop
while True:
    display_menu()
    choice = input("Choose an option (1-4): ").strip()
    
    if choice == '1':
        add_entry()
    elif choice == '2':
        view_entries()
    elif choice == '3':
        search_entries()
    elif choice == '4':
        print("Exiting the journal logger. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")