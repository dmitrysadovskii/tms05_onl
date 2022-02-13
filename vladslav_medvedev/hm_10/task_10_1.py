'''
Цветочница.
Определить иерархию и создать несколько цветов.
Собрать букет (можно использовать аксессуары) с определением его стоимости.
Определить время его увядания по среднему времени жизни всех цветов в букете.
Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость...)
Реализовать поиск цветов в букете по определенным параметрам.
Узнать, есть ли цветок в букете.
'''


class Flowers:

    def __init__(self, name, country, color, long, lifetime, price):
        self.name = name
        self.country = country
        self.color = color
        self.long = long
        self.lifetime = lifetime
        self.price = price


class Roses(Flowers):

    def __init__(self):
        self.name = 'Rose'
        self.country = 'Holand'
        self.color = "red"
        self.long = 70
        self.lifetime = 70
        self.price = 25


class Chamomile(Flowers):

    def __init__(self):
        self.name = 'Chamomile'
        self.country = 'Russia'
        self.color = "white"
        self.long = 20
        self.lifetime = 35
        self.price = 15

class Iris(Flowers):

    def __init__(self):
        self.name = 'Iris'
        self.country = 'Ukraine'
        self.color = "blue"
        self.long = 25
        self.lifetime = 32
        self.price = 17


class Peony(Flowers):

    def __init__(self):
        self.name = 'Peony'
        self.country = 'Croatia'
        self.color = "pink"
        self.long = 60
        self.lifetime = 96
        self.price = 30

class Bouquet:

    def __init__(self,):
        count_roses_in_the_bouquet = range(0, 5)
        count_chamomile_in_the_bouquet = range(0, 5)
        count_iris_in_the_bouquet = range(0, 5)
        count_peon_in_the_bouquet = range(0, 5)
        count_flowers_in_the_bouquet = count_roses_in_the_bouquet + count_chamomile_in_the_bouquet + count_iris_in_the_bouquet + count_peon_in_the_bouquet

    def count(self, count_flowers_in_the_bouquet):
        if Bouquet.count_flowers_in_the_bouquet % 2 == 0:
            pass
        else:
            print(f"Не красиво дарить нечетное количество цветов: {count_flowers_in_the_bouquet}")

    def price_of_bouquet(self,count_roses_in_the_bouquet, count_chamomile_in_the_bouquet, count_iris_in_the_bouquet, count_peon_in_the_bouquet):

        price_rose = count_roses_in_the_bouquet * Roses.price
        price_chamomile = count_chamomile_in_the_bouquet * Chamomile.price
        price_iris = count_iris_in_the_bouquet * Iris.price
        price_peon = count_peon_in_the_bouquet * Peony.price

        sum = price_rose + price_chamomile + price_iris + price_peon
        print(f'Цена букета равна {sum}')

    def lifetime(self,count_roses_in_the_bouquet, count_chamomile_in_the_bouquet, count_iris_in_the_bouquet, count_peon_in_the_bouquet ):
        pass


bouquet = Bouquet()
print(bouquet)



