class User:

    def __init__(self,name,balance):
        self.name = name
        self.account_balance= balance

    def make_withdraw(self,amount):
        self.account_balance -= amount
        return self
    def deposit(self,amount):
        self.account_balance += amount
        return self
    def display_balance(self):
        print(f'User:{self.name}, Balance: {self.account_balance}')
        return self

Alex = User('Alex', 100)
Alex.deposit(100).deposit(20).deposit(80).make_withdraw(50).display_balance()
Uin = User('Uin', 70)
Uin.deposit(18).deposit(30).make_withdraw(15).make_withdraw(30).display_balance()
Jake = User('Jake',200)
Jake.deposit(40).make_withdraw(70).make_withdraw(25).make_withdraw(20).display_balance()


