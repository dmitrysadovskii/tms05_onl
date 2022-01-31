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


class Charomile(Flowers):

    def __init__(self):
        self.name = 'Charomile'
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

    def __init__(self, fl, counts):
        self.fl = fl
        self.counts = counts

    def price_of_bouquet(self):
        price_list = []
        for flower in self.fl:
            each_price = self.counts[self.fl.index(flower)] * flower.price
            price_list.append(each_price)
        new_price_list = sum(price_list)
        print(f"The price of the bouquet is {new_price_list}")

    def withering_time(self):
        lifetime = []
        for flower in self.fl:
            lifetime.append(flower.life_time)
        lifetime = round(sum(lifetime) / len(self.fl), 1)
        print(f"The withering time of the bouquet is {lifetime} days")

    def sort_option(self, option):
        assert isinstance(option, str), "Option should be str"
        assert len(option) != 0, "Please enter an option"
        assert option in ['life_time', 'price', 'length', 'color', 'fresh'], \
            f"There is no such option {option}"
        result = ''
        result += option_to_sort(option, self.fl)
        print(f"{result}")

    def search_option(self, option, value):
        assert isinstance(option, str), "Option should be str"
        assert len(option) != 0, "Please enter an option"
        assert option in ['life_time', 'price', 'length', 'color', 'fresh'], \
            f"There is no such option {option}"
        assert isinstance(value, int), "Value should be int"
        assert value > 0, "Value must be positive"
        result = ''
        result += option_to_search(option, value, self.fl)
        print(f"{result}")

    def search_flower(self, el):
        assert isinstance(el, str), "The name of a flower should be str"
        assert len(el) != 0, "Please enter the name of a flower"
        if el in [flower.name for flower in self.fl]:
            print(f"{el} is in the bouquet")
        else:
            print(f"{el} is not in the bouquet")




