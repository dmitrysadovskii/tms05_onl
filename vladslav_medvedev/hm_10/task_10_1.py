'''
Цветочница.
Определить иерархию и создать несколько цветов.
Собрать букет (можно использовать аксессуары) с определением его стоимости.
Определить время его увядания по среднему времени жизни всех цветов в букете.
Позволить сортировку цветов в букете на основе различных параметров
(свежесть/цвет/длина стебля/стоимость...)
Реализовать поиск цветов в букете по определенным параметрам.
Узнать, есть ли цветок в букете.
'''
import operator


class Flowers:

    def __init__(self, name, country, color, lifetime, price):
        self.name = name
        self.country = country
        self.color = color
        self.lifetime = lifetime
        self.price = price


class Roses(Flowers):
    pass


class Chamomile(Flowers):
    pass


class Peony(Flowers):
    pass


class Bouquet:

    def __init__(self, fl, count):
        self.fl = fl
        self.count = count

    def price_of_bouquet(self):
        price_list = []
        for flower in self.fl:
            each_price = self.count[self.fl.index(flower)] * flower.price
            price_list.append(each_price)
        print(f"The price of the bouquet is {sum(price_list)}")

    def life_times(self):
        lifetime = []
        for flower in self.fl:
            lifetime.append(flower.lifetime)
        lifetime = round(sum(lifetime) / len(self.fl), 1)
        print(f"The  lifetime of the bouquet is {lifetime} hours")

    def search_option(self, option, value):
        assert isinstance(option, str), "Option should be str"
        assert len(option), "Please enter an option"
        assert option in ['life_time', 'price', 'length', 'color', 'fresh'], \
            f"There is no such option {option}"
        assert isinstance(value, int), "Value should be int"
        assert value > 0, "Value must be positive"
        flower_list = []
        for el in self.fl:
            if operator.attrgetter(option)(el) == value:
                flower_list.append(el.name)
        if len(flower_list) > 0:
            name_list_search = ", ".join(flower_list)
            print(name_list_search)
        else:
            print('There is no such flower in the bouquet')

    def search_flower(self, el):
        assert isinstance(el, str), "The name of a flower should be str"
        assert len(el), "Please enter the name of a flower"
        if el in [flower.name for flower in self.fl]:
            print(f"{el} is in the bouquet")
        else:
            print(f"{el} is not in the bouquet")


roses = Roses(name='Rose', country='Holand', color='red', lifetime=70, price=25)
chamomile = Chamomile(name='Chamomile', country='Russia', color='white', lifetime=35, price=15)
peony = Peony(name='Peony', country='Croatia', color='scarlet', lifetime=96, price=30)
flowers = [roses, chamomile, peony]
count = [3, 4, 5]
bouquet = Bouquet(flowers, count)
bouquet.price_of_bouquet()
bouquet.life_times()
bouquet.search_option('price', 25)
bouquet.search_flower('Chamomile')
