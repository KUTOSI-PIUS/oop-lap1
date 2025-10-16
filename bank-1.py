bank.<i class="fas fa-python    "></i>
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance  # Corrected from account_number to balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount(260)
account.deposit(100)
account.withdraw(50)
print(account.balance)


