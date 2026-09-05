class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.next_account = None

    def set_next(self, account):
        self.next_account = account
        return account

    def pay(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Paid {amount} using {self.name}")
        elif self.next_account:
            self.next_account.pay(amount)
        else:
            print("No account can pay")


account_a = Account("A", 100)
account_b = account_a.set_next(Account("B", 300))
account_b.set_next(Account("C", 1000))
account_a.pay(210)
