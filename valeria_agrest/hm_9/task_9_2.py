class Investment:

    def __init__(self, summa, period, percent):
        self.summa = summa
        self.period = period
        self.percent = percent


class Bank:

    def __init__(self):
        self.invests = list()

    def add_invest(self, invest):
        self.invests.append(invest)

    def deposit(self):
        for invest in self.invests:
            period_in_months = invest.period * 12
            one_month = invest.percent / 12
            for i in range(1, period_in_months + 1):
                new_summa = invest.summa + (invest.summa * one_month) / 100
                invest.summa = round(new_summa, 2)
            print(f'Summa will be {invest.summa}')


investment = Investment(2000, 1, 10)
bank = Bank()
bank.add_invest(investment)
bank.deposit()
