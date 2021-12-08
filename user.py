class User:

    def __init__(self,name):
        self.name = name
        self.account_balance= 0

    def make_withdraw(self,amount):
        self.acount_balance -= amount
        return self
    def deposit(self,amount):
        self.account_balance += amount
        return self
    def display_balance(self):
        print(f'User:{self.name}, Balance: {self.account_balance}')
        return self

Alex = User('Alex', 100)
Alex.make_withdraw(50)
print(Alex.display_balance())

