# Number Comparison Tool

# Step 1: Get user input for two numbers
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: "))

# Step 2: Compare the two numbers and display the result
print("\n---- Comparison Results ----")

if num1 == num2:
  print(f"Both numbers are equal: {num1} = {num2}")
elif num1 > num2:
  print(f"{num1} is greater than {num2}")
else:
  print(f"{num1} is less than {num2}")

# Step 3: Check if any number is zero
if num1 == 0 or num2 == 0:
  print("At least one of the numbers is zero.")
else:
  print("Neither of the numbers is zero.")