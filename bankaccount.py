class BankAccount:

    bank_name = "Andy Bank"    

    all_accounts = []

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
        # your code here
    def withdraw(self, amount):
        self.balance -= amount
        return self
        # your code here
    def display_account_info(self):
        print(self.int_rate)
        print(self.balance)
        # your code here
    def yield_interest(self):
        self.balance * self.int_rate
        return self
        # your code here

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
    # your code here
    def display_user_balance(self, amount):
        self.account.balance(amount)

account1 = BankAccount(0,0)
account2 = BankAccount(0.2,0)

account1.deposit(1000)

account1.deposit(100).deposit(200).deposit(300).withdraw(200).yield_interest().display_account_info()
account2.deposit(50).deposit(100).deposit(150).withdraw(200).yield_interest().display_account_info()

