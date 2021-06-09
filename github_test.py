class Money:
    def __init__(self, amount, currency, amount_2):
        self.amount_1 = amount
        self.currency_1 = currency
        self.amount_second = amount_2
    def __repr__(self):
        return str(self.amount_1) + " " + self.currency_1
    def represetation(self):
        return str(self.amount_1 - self.amount_second) + self.currency_1




final = Money(35, "usd", 15)
final_second = Money(67, "usd", 55)
print(final)
print(final.represetation())
print()