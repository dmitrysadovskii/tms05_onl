"""
    2. Банковский вклад
Создайте класс инвестиция. Который содержит необходимые поля и методы,
например сумма инвестиция и его срок.
Пользователь делает инвестиция в размере N рублей сроком на R лет под 10%
годовых (инвестиция с возможностью ежемесячной капитализации - это означает,
что проценты прибавляются к сумме инвестиции ежемесячно).
Написать класс Bank, метод deposit принимает аргументы N и R, и возвращает
сумму, которая будет на счету пользователя.
"""


class Investment:

    def __init__(self, amount: (float, int)):
        self.amount = amount


class Bank:

    @staticmethod
    def deposit(investment: Investment, deposit_period_month: int,
                deposit_rate: int) -> (float, int):
        """
        Calculate amount which will be available by the end of deposit
        placement period using monthly capitalization of interest income.
        :param investment: object of class Investment.
        :param deposit_period_month: number of months of placement.
        :param deposit_rate: rate for calculating interest income.
        :return: total amount with capitalized percents.
        """
        total_amount = investment.amount
        for month in range(deposit_period_month):
            total_amount *= (1 + deposit_rate/100)
        return total_amount


first_investment = Investment(100)
new_bank = Bank()
print(first_investment.amount)
print(new_bank.deposit(Investment(100), 3, 5))
