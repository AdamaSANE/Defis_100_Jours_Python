# Safe Calculator

# Step 1: Define Calculator Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b): 
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b  

# Step 2: Display Menu
def display_menu():
    print("\n--- Safe Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Step 3: Main Program Loop
while True:
    display_menu()
    choice = input("Select an operation (1-5): ")

    if choice == '5':
      print("Exiting the calculator. Goodbye!")
      break
    
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      if choice == '1':
          result = add(num1, num2)
          print(f"Result: {num1} + {num2} = {result}")
      elif choice == '2':
          result = subtract(num1, num2)
          print(f"Result: {num1} - {num2} = {result}")  
      elif choice == '3':
          result = multiply(num1, num2)
          print(f"Result: {num1} * {num2} = {result}")
      elif choice == '4':
          result = divide(num1, num2)
          print(f"Result: {num1} / {num2} = {result}")
      else:
          print("Invalid choice. Please select a valid operation.")
    except ValueError:
      print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError as e:
      print(f"Error: {e}")
    except Exception as e:
      print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Safe Calculator. Operation completed... Restarting\n")

        