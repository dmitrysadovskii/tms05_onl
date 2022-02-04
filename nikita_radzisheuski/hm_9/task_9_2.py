"""Создайте класс инвестиция. Который содержит необходимые поля и методы,
например сумма инвестиция и его срок. Пользователь делает инвестиция в размере
N рублей сроком на R лет под 10% годовых (инвестиция с возможностью ежемесячной
капитализации - проценты прибавляются к сумме инвестиции ежемесячно). Написать
класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму,
которая будет на счету пользователя.
"""


class Investment:
    def __init__(self, sum_in_rub, years):
        self.sum_in_rub = sum_in_rub
        self.years = years


class Bank:
    def __init__(self):
        self.investments = list()

    def add_investment(self, investment):
        self.investments.append(investment)

    def deposit(self):
        """Method deposit that takes arguements sum_in_rub and years quantity
        and calculates end sum of deposit. Firstly the method converts years in
        quantity of month and then calculates by the formula:
        Rub+(Rub*(10%/12month)/100. The final num is rounded for 3 symbols"""
        for investment in self.investments:
            period_in_months = investment.years * 12
            for i in range(1, period_in_months + 1):
                end_sum = investment.sum_in_rub +\
                          (investment.sum_in_rub * (10 / 12)) / 100
                investment.sum_in_rub = round(end_sum, 3)
            print(f'Sum is {investment.sum_in_rub}')


investment = Investment(7000, 3)
bank = Bank()
bank.add_investment(investment)
bank.deposit()
