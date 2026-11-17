# Bank Account System (Class, Object, Constructor)

class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)

b = BankAccount(12345, 10000)

b.deposit(2000)
b.withdraw(3000)
b.display()