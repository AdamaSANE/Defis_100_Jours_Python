# Temperature Converter

# Step 1: Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Step 2: Define a function to convert celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Step 3: Define a function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Step 4: Define a function to convert fehrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

# Step 5: Define a function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Step 6: Define a function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Step 7: Display the menu
def display_menu():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit & Kelvin")
    print("2. Fahrenheit to Celsius & Kelvin")
    print("3. Kelvin to Celsius & Fahrenheit")
    print("4. Exit")

# Step 8: Main program loop
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"Fahrenheit: {celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
            print(f"Kelvin: {celsius}°C = {celsius_to_kelvin(celsius):.2f}K")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"Celsius: {fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.2f}°C")
            print(f"Kelvin: {fahrenheit}°F = {fahrenheit_to_kelvin(fahrenheit):.2f}K")
        elif choice == '3':
            kelvin = float(input("Enter temperature in Kelvin: "))
            print(f"Celsius: {kelvin}K = {kelvin_to_celsius(kelvin):.2f}°C")
            print(f"Fahrenheit: {kelvin}K = {kelvin_to_fahrenheit(kelvin):.2f}°F")
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")