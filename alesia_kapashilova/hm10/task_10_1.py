import operator


class Flower:

    def __init__(self, name, life_time=10, color='white', fresh=True,
                 length=6, price=10):
        self.life_time = life_time
        self.color = color
        self.fresh = fresh
        self.length = length
        self.price = price
        self.name = name


class Chamomile(Flower):
    pass


class Rose(Flower):
    pass


class Gerbera(Flower):
    pass


class Orchid(Flower):
    pass


class Tulip(Flower):
    pass


class Bouquet:

    def __init__(self, flow, counts):
        self.flow = flow
        self.counts = counts

    def price_of_bouquet(self):
        price_list = []
        for flower in self.flow:
            each_price = self.counts[self.flow.index(flower)] * flower.price
            price_list.append(each_price)
        print(f"The price of the bouquet is {sum(price_list)}")

    def withering_time(self):
        lifetime = []
        for flower in self.flow:
            lifetime.append(flower.life_time)
        lifetime = round(sum(lifetime) / len(self.flow), 1)
        print(f"The withering time of the bouquet is {lifetime} days")

    def sort_option(self, option):
        assert isinstance(option, str), "Option should be str"
        assert len(option), "Please enter an option"
        assert option in ['life_time', 'price', 'length', 'color', 'fresh'], \
            f"There is no such option {option}"
        option_dict = {}
        for flower in self.flow:
            option_dict[flower.name] = operator.attrgetter(option)(flower)
        sorted_dict = sorted(option_dict.items(), key=lambda fl: fl[1])
        for element in sorted_dict:
            print(element[0], element[1])

    def search_option(self, option, value):
        assert isinstance(option, str), "Option should be str"
        assert len(option), "Please enter an option"
        assert option in ['life_time', 'price', 'length', 'color', 'fresh'], \
            f"There is no such option {option}"
        assert isinstance(value, int), "Value should be int"
        assert value > 0, "Value must be positive"
        flower_list = []
        for flower in self.flow:
            if operator.attrgetter(option)(flower) == value:
                flower_list.append(flower.name)
        if len(flower_list) > 0:
            name_list_search = ", ".join(flower_list)
            print(name_list_search)
        else:
            print('There is no such flower in the bouquet')

    def search_flower(self, flowers):
        assert isinstance(flowers, str), "The name of a flower should be str"
        assert len(flowers), "Please enter the name of a flower"
        if flowers in [flower.name for flower in self.flow]:
            print(f"{flowers} is in the bouquet")
        else:
            print(f"{flowers} is not in the bouquet")
