# Example 11: Getters and Setters Example

class BankAccount:
    """A simple bank account class with encapsulation."""
    def __init__(self, account_number, balance=0):
        self.account_number = account_number    # Public attribute
        self.__balance = balance                # Private attribute

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}.")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        """Get the current balance."""
        return self.__balance

    def set_balance(self, amount):
        """Set the account balance (with validation)."""
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount.")

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: ${self.__balance}"

# Using the BankAccount class
account = BankAccount('123456789', 1000)

# Accessing the balance using the getter method
print(f"Balance: ${account.get_balance()}")

# Attempting to set a new balance using the setter method
account.set_balance(1200)
print(f"Balance after update: ${account.get_balance()}")

# Trying to set an invalid balance
account.set_balance(-500)

# Performing transactions
account.deposit(300)
account.withdraw(500)
print(account)
