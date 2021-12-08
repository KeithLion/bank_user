class User:

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def make_withdraw(self,amount):
        balance -= amount
        return self
    def deposit(self):
        balance += amount
        return self
    def display_balance():
        print(f'{self.name}, Balanc: {self.balance}')
