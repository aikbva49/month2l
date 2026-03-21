class Money:
    def __init__(self, amount, corrency='KGS'):
        self.amount = amount
        self.corrency = corrency

    def __str__(self):
        return f'<Money  obj amount={self.amount} corrency={self.corrency}>'

    def __eq__(self, other):
        if self.amount == other.amount:
            return True
        else:
            return False

        # gt -> greater than '>'
        #gte -> greater than or equal ">="
        #lt -> less than '<'
        #lte -> less than or equal ">="

    def __gt__(self, other):
        if self.amount == other.amount:
            return True
        else:
            return False
        ###ine line###
        return self.amount > other.amount



money_ai = Money(100)
money_aa = Money(156)
print(money_ai)
print(money_ai.amount)
print(money_ai == money_aa)
print(money_ai < money_aa)
