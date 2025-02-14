

class Bank:
    def __init__(self, cash = 0):
        self.current_balance = cash

    def deposit(self, cash):
        self.current_balance += cash

    def withdraw(self, cash):
        self.current_balance -= cash

    def balance(self):
        return self.current_balance

    def apply_interest(self, cash):
        mult_interest = 1 + cash
        self.current_balance = round((self.current_balance * mult_interest), 2)

    def check_bill(self, cash):
        if self.current_balance > cash:
            return True
        else:
            return False

acc = Bank()

acc.deposit(50)
print(acc.current_balance)

acc.withdraw(25)
print(acc.current_balance)

my_bal = acc.balance()
print(my_bal)

acc.apply_interest(0.10)
print(acc.current_balance)

afford = acc.check_bill(50)
print(afford)
