# Bank Account Simulator

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    # Deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")
    # Withdraw money from the account
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    # Show Account Details
    def show_details(self):
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")

# Main Program
accounts = {}

def create_account():
    name = input("Enter account holder's name: ").strip()
    initial_deposit = float(input("Enter initial deposit amount: "))
    account = BankAccount(name, initial_deposit)
    accounts[name] = account
    print("Account created successfully!")

# Accessing an existing account
def access_account():
    name = input("Enter account holder's name: ").strip()
    account = accounts.get(name)
    if account:
        while True:
            print("\n--- Account Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Details")
            print("4. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == '3':
                account.show_details()
            elif choice == '4':
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Account not found.")

# Main Loop
while True:
    print("\n--- Bank Account Simulator ---")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")
    main_choice = input("Choose an option: ").strip()

    if main_choice == '1':
        create_account()
    elif main_choice == '2':
        access_account()
    elif main_choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")