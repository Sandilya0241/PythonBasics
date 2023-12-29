class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted")

    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print("Withdrawal Accepted")

    def __str__(self):
        return ("Account owner: {}\nAccount balance: ${}".format(self.owner, self.balance))


if __name__ == "__main__":
    acct1 = Account("Sandy", 100)
    print(acct1)
    print()
    acct1.deposit(50)
    print()
    acct1.withdraw(75)
    print()
    acct1.withdraw(500)

