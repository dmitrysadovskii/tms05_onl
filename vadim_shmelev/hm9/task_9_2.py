class Investment:

    def __init__(self, amount):
        self.amount = amount


class Capital:

    @staticmethod
    def deposit(investment: Investment, deposit_time: int,
                deposit_rate: int) -> (float, int):

        amount = investment.amount
        for month in range(deposit_time):
            amount *= (1 + deposit_rate / 100)
        return amount


first_investment = Investment(1500)
capital = Capital()
print(first_investment.amount)
print(capital.deposit(Investment(100), 10, 5))
