# Ingredients Checker

# Step 1: Define the recipe ingredients

recipe_ingredients = { "flour", "sugar", "eggs", "milk", "butter" }

# Step 2: Get user input for available ingredients
user_input = input("Enter the ingredients you have (separated by commas): ")
user_ingredients = set(user_input.split(","))

# Step 3: Compare Ingredients
missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

# Step 4: Display Results
print("\n---- Ingredients Check ----\n")
if missing_ingredients:
    print(f"Missing ingredients: {', '.join(missing_ingredients)}")
else:
    print("You have all the necessary ingredients!")

if extra_ingredients:
    print(f"Extra ingredients: {', '.join(extra_ingredients)}")
else:
    print("No extra ingredients found.")