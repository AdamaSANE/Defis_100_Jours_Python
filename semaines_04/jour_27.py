# Inventory Management System

class Inventory:
  total_items = 0

  def __init__(self, product_name, price, quantity):
    self.product_name = product_name
    self.price = price
    self.quantity = quantity
    Inventory.total_items += quantity

  # Instance method to display product details
  def show_product(self):
    print("\n--- Product Details ---")
    print(f"Product Name: {self.product_name}")
    print(f"Price: ${self.price}")
    print(f"Quantity: {self.quantity}")

  # Instance method: Sell product
  def sell_product(self, amount):
    if amount <= self.quantity:
      self.quantity -= amount
      Inventory.total_items -= amount
      print(f"\nSold {amount} of {self.product_name}.")
    else:
      print(f"\nInsufficient stock to sell {amount} of {self.product_name}.")

  # Static Method: Calculate discounted price
  @staticmethod
  def calculate_discounted_price(price, discount_percentage):
    return price * (1 - discount_percentage / 100)
  
  # Class Method: Display total items Report
  @classmethod
  def total_items_report(cls):
    print(f"\nTotal items report: {cls.total_items}")

# Main Program
products = []

# Adding products to inventory
def add_product():
  product_name = input("Enter product name: ")
  price = float(input("Enter product price: "))
  quantity = int(input("Enter product quantity: "))
  product = Inventory(product_name, price, quantity)
  products.append(product)
  print(f"\nProduct {product_name} added to inventory.")

# Display all products
def view_products():
  print("\n--- Inventory Products ---")
  if not products:
    print("No products in inventory.")  
  else:
    for product in products:
      product.show_product()


# Sell a product
def sell_product():
  product_name = input("Enter product name to sell: ")
  for product in products:
    if product.product_name == product_name:
      amount = int(input(f"Enter quantity to sell of {product_name}: "))
      product.sell_product(amount)
      break
  else:
    print(f"\nProduct {product_name} not found in inventory.")

# Calculate discounted price
def discount_price():
  price = float(input("Enter product price: "))
  discount_percentage = float(input("Enter discount percentage: "))
  discounted_price = Inventory.calculate_discounted_price(price, discount_percentage)
  print(f"\nDiscounted price: ${discounted_price:.2f}")

# Main Menu
while True:
  print("\n--- Inventory Management System ---")
  print("1. Add Product")
  print("2. View Products")
  print("3. Sell Product")
  print("4. Calculate Discounted Price")
  print("5. Total Items Report")
  print("6. Exit")

  choice = input("Enter your choice (1-6): ")

  if choice == '1':
    add_product()
  elif choice == '2':
    view_products()
  elif choice == '3':
    sell_product()
  elif choice == '4':
    discount_price()
  elif choice == '5':
    Inventory.total_items_report()
  elif choice == '6':
    print("Exiting Inventory Management System.")
    break
  else:
    print("Invalid choice. Please try again.")