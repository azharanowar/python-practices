class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.__balance = balance
    
    def account_holder_info(self):
        print(f"Account number: {self.account_number}, account holder name: {self.account_holder_name}")
    def get_current_balance(self):
        return self.__balance
    
    def deposit_amount(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
        else:
            print("Invalid deposit amount!")
    
    def withdraw_amount(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
        else:
            print("Invalid withdraw amount!")

account1 = BankAccount(123123123123, "Md Anwar Hosen")
account1.account_holder_info()
print(f"Current balance: {account1.get_current_balance()}")

deposit_amount = float(input("Enter amount you want to deposit: "))
account1.deposit_amount(deposit_amount)
print(f"Current balance: {account1.get_current_balance()}")

withdraw_amount = float(input("Enter amount you want to withdraw: "))
account1.withdraw_amount(withdraw_amount)
print(f"Current balance: {account1.get_current_balance()}")
