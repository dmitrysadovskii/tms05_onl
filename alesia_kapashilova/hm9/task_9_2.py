class Investment:

    def __init__(self, sum_inv, period, percent):
        self.sum_inv = sum_inv
        self.period = period
        self.percent = percent


class Bank:

    def __init__(self):
        self.my_invests = list()

    def add_invest(self, invest):
        self.my_invests.append(invest)

    def deposit(self):
        for invest in self.my_invests:
            period_in_months = invest.period * 12
            one_month = invest.percent / 12
            for i in range(1, period_in_months + 1):
                new_summa = invest.sum_inv + (invest.sum_inv * one_month) / 100
                invest.sum_inv = round(new_summa, 2)
            print(f'Summa will be {invest.sum_inv}')


investment = Investment(15000, 1, 10)
bank = Bank()
bank.add_invest(investment)
bank.deposit()
