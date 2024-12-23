class BankAccount:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"The amount ${amount} is deposited. new balance: ${self.balance}.")
        else:
            print("Invalid deposit amount, enter a valid amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"The amount ${amount} is widrawned. The new balance: ${self.balance}.")
        else:
            print("Error: Not valid transection.")
    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: ${self.balance}"

bank = BankAccount('123456789', 5000)

bank.deposit(700)
bank.withdraw(200)
print(bank)