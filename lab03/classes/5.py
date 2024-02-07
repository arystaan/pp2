class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, months, percent):
        for i in range(months):
            self.balance += percent*self.balance
    
    def withdraw(self, take):
        if take < 0:
            print("You can't withdraw negative amount of money!")
        elif take > self.balance:
            print("Not enough balance!")
        else:
            print("Withdrawing", take, "from your balance", self.balance-take)
            self.balance = self.balance-take

account = Account("Ardak Abdullakhan", 15)
account.deposit(12, 0.15)
account.withdraw(3)
account.withdraw(-5)
account.withdraw(10)
account.withdraw(100)