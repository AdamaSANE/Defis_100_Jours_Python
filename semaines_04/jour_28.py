# Project: Mini ATM Machine

class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance

    # Validate PIN
    def validate_pin(self, entered_pin):
        return self.__pin == entered_pin
    
    # Check balance
    def check_balance(self):
        return f"Current balance: ${self.__balance}"
    
    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: ${amount}. New balance: ${self.__balance}"
        else:
            return "Deposit amount must be positive."

    # Withdraw money
    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds."
        elif amount > 0:
            self.__balance -= amount
            return f"Withdrew: ${amount}. New balance: ${self.__balance}"
        else:
            return "Withdrawal amount must be positive."
    
    # Change PIN
    def change_pin(self, old_pin, new_pin):
        if self.validate_pin(old_pin) and len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            return "PIN successfully changed."
        else:
            return "Failed to change PIN. Check old PIN and ensure new PIN is 4 digits."

# Class ATM
class ATM:
    def __init__(self):
        self.accounts = {}

    # Create Account
    def create_account(self):
        account_number = input("Enter account number: ")
        pin = input("Set a 4-digit PIN: ")
        if len(pin) == 4 and pin.isdigit():
            self.accounts[account_number] = BankAccount(account_number, pin)
            print("Account created successfully.")
        else:
            print("Invalid PIN. PIN must be 4 digits.")

    # Authenticate Account
    def authenticate_account(self):
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")

        account = self.accounts.get(account_number)
        if account and account.validate_pin(pin):
            print("Authentication successful.")
            self.account_menu(account)
        else:
            print("Authentication failed.")
      
    # Account Menu
    def account_menu(self, account):
        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Logout")

            choice = input("Choose an option(1-5): ")

            if choice == '1':
                account.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == '4':
                old_pin = input("Enter old PIN: ")
                new_pin = input("Enter new 4-digit PIN: ")
                account.change_pin(old_pin, new_pin)
            elif choice == '5':
                print("Logging out... Thank you for using the ATM.")
                break
            else:
                print("Invalid choice. Please try again.")

    # Main Menu
    def main_menu(self):
      while True:
        print("\n--- Welcome to Mini ATM Machine ---")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Exit")

        choice = input("Choose an option(1-3): ")

        if choice == '1':
            self.create_account()
        elif choice == '2':
            self.authenticate_account() 
        elif choice == '3':
            print("Exiting... Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the ATM application
if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()
        