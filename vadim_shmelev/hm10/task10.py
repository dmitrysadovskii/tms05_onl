import operator


class Flower:

    def __init__(self, name, life_time=1, color="color",
                 fresh=True, length=1, price=1):
        self.life_time = life_time
        self.color = color
        self.fresh = fresh
        self.length = length
        self.price = price
        self.name = name


class Orcid(Flower):
    pass


class Rose(Flower):
    pass


class Iris(Flower):
    pass


class CollectBouquet:

    def __init__(self, fl, counts):
        self.fl = fl
        self.counts = counts

    def price_of_bouquet(self):
        price_list = []
        for flower in self.fl:
            each_price = self.counts[self.fl.index(flower)] * flower.price
            price_list.append(each_price)
        print(f"The bouquet price is {sum(price_list)}")

    def withering_time(self):
        lifetime = []
        for flower in self.fl:
            lifetime.append(flower.life_time)
        lifetime = round(sum(lifetime) / len(self.fl), 1)
        print(f"The life-time  is {lifetime} days")

    def sort_option(self, option):
        assert isinstance(option, str), "Option should be str"
        assert len(option), "Enter an option"
        assert option in ['life_time', 'price', 'length', 'color', 'fresh'], \
            f"There is no such option {option}"
        option_dict = {}
        for el in self.fl:
            option_dict[el.name] = operator.attrgetter(option)(el)
        sorted_dict = sorted(option_dict.items(), key=lambda fl: fl[1])
        for element in sorted_dict:
            print(element[0], element[1])

    def search_option(self, option, value):
        assert isinstance(option, str), "Enter a str"
        assert len(option), "Enter an option"
        assert option in ['life_time', 'price', 'length', 'color', 'fresh'], \
            f"There is no such option {option}"
        assert isinstance(value, int), "Enter must be int"
        assert value > 0, "Value must be positive"
        flower_list = []
        for el in self.fl:
            if operator.attrgetter(option)(el) == value:
                flower_list.append(el.name)
        if len(flower_list) > 0:
            name_list_search = ", ".join(flower_list)
            print(name_list_search)
        else:
            print('No such flower in the bouquet')

    def search_flower(self, el):
        assert isinstance(el, str), "А flower must be str"
        assert len(el), "Enter flower name"
        if el in [flower.name for flower in self.fl]:
            print(f"{el} is in the bouquet")
        else:
            print(f"{el}  not in the bouquet")


orcid = Orcid(name='Orcid', life_time=3, color='pink', price=6)
iris = Iris(name='Iris', color='purple', fresh=False, length=2)
rose = Rose(name='Rose', life_time=6, color='red', length=5)
flowers = [orcid, iris, rose]
counts = [11, 2, 3]
collect_bouquet = CollectBouquet(flowers, counts)
collect_bouquet.price_of_bouquet()
collect_bouquet.withering_time()
collect_bouquet.search_option('length', 5)
collect_bouquet.search_flower('Iris')
