'''
Банковский вклад.
Создайте класс инвестиция. Который содержит необходимые поля и методы,
например сумма инвестиция и его срок. Пользователь делает инвестиции
в размере N рублей сроком на R лет под 10% годовых
(инвестиция с возможностью ежемесячной капитализации - это означает,
что проценты прибавляются к сумме инвестиции ежемесячно).
Написать класс Bank, метод deposit принимает аргументы N и R,
и возвращает сумму, которая будет на счету пользователя.
'''


class Investments:

    def __init__(self, sum_invest: float, term_invest: int):
        self.sum_invest = sum_invest
        self.term_invest = term_invest


class Bank:
    def __init__(self, percent):
        self.percent = percent

    def deposit(self, investments: Investments):
        result = investment.sum_invest * pow((1 + self.percent / 1200),
                                             investment.term_invest)
        result = round(result, 2)
        print(f'Сумма депозита через {investment.term_invest} '
              f'месяц/а = {result}')

investment = Investments(1000, 12)
bank = Bank(10)
bank.deposit(investment)
