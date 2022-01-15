class Investment:

    def __init__(self, sum_of_investment, investment_term):
        self.sum_of_investment = sum_of_investment
        self.investment_term = investment_term


class Bank:
    def __init__(self, percent):
        self.percent = percent

    def deposit(self, investment: Investment):
        result = investment.sum_of_investment * \
                 pow((1 + self.percent / 1200),
                     investment.investment_term * 12)
        result = round(result, 2)
        print(f'Сумма депозита через {investment.investment_term} '
              f'год/a = {result}')


investment1 = Investment(1000, 1)
bank = Bank(10)
bank.deposit(investment1)
