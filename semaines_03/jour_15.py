# Recipe Viewer App

# Step 1: Load Recipes from a File
def load_recipes(file_path):
  try:
    with open(file_path, 'r') as file:
      content = file.read()
      recipes = content.split('\n\n')  # Assuming each recipe is separated by a blank line
      recipe_dict = {}
      for recipe in recipes:
        lines = recipe.strip().split('\n')
        if len(lines) >= 3:  # Ensure there is a title and at least two ingredients
          title = lines[0].strip()
          ingredients = lines[1].replace('Ingredients: ', '').strip()
          instructions = lines[2].replace('Instructions: ', '').strip()
          recipe_dict[title] = {
            'ingredients': ingredients,
            'instructions': instructions
          }
      return recipe_dict
  except FileNotFoundError:
    print("Recipe file not found.")
    return {}

# Step 2: Display Recipes Menu
def display_menu():
  print("\n--- Recipe Viewer Menu ---")
  print("1. View Recipes by Title")
  print("2. List All Recipes")
  print("3. Exit")

# Step 3: Display Recipe Details
def View_recipe(recipe):
  title = input("Enter the recipe title: ")
  if title in recipe:
    print(f"\n--- Recipe {title} Details ---")
    print(f"Ingredients: {recipe[title]['ingredients']}")
    print(f"Instructions: {recipe[title]['instructions']}\n")
  else:
    print("Recipe not found.")

# Step 4: Main Program Loop
recipe_file = 'recipes.txt'  # Path to the recipe file
recipes = load_recipes(recipe_file)

while True:
  display_menu()
  choice = input("Choose an option (1-3): ")
  
  if choice == '1':
    View_recipe(recipes)
  elif choice == '2':
    print("\n--- All Recipes ---")
    for title in recipes:
      print(title)
    
  elif choice == '3':
    print("Exiting the Recipe Viewer. Goodbye!")
    break
  else:
    print("Invalid choice. Please try again.")