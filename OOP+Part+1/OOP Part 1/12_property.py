# Example 12: Using @property Decorator

class BankAccount:
    """A bank account class using property decorators."""
    def __init__(self, account_number, balance=0):
        self.account_number = account_number    # Public attribute
        self.__balance = balance                # Private attribute

    @property
    def balance(self):
        """Get the current balance."""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Set the account balance (with validation)."""
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}.")
        else:
            print("Insufficient funds or invalid amount.")

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: ${self.__balance}"

# Using the BankAccount class with @property
account = BankAccount('987654321', 500)

# Accessing the balance using the property
print(f"Balance: ${account.balance}")

# Setting a new balance using the setter
account.balance = 700
print(f"Balance after update: ${account.balance}")

# Attempting to set an invalid balance
account.balance = -200

# Performing transactions
account.deposit(300)
account.withdraw(100)
print(account)
