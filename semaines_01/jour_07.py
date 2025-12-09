# Shopping List App

# Step 1: Initialize an empty shopping list
shopping_list = []

# Step 2: Define the main menu

def main_menu():
    print("\n==== Shopping List Menu ====")
    print("1. View shopping list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Clear List")
    print("5. Exit")

# Step 3: Main program loop
while True:
    main_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        print("\n===Your Shopping List===")
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            for indx, item in enumerate(shopping_list):
                print(f"{indx + 1}. {item}")

    elif choice == '2':
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} has been added to your shopping list.")

    elif choice == '3':
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from your shopping list.")
        else:
            print(f"{item} is not in your shopping list.")
    elif choice == '4':
        shopping_list.clear()
        print("Your shopping list has been cleared.")

    elif choice == '5':
        print("Exiting the Shopping List App. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option (1-5).")