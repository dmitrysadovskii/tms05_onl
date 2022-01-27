import operator


def option_to_sort(option, fl):
    option_dict = {}
    sorted_option = {}
    strings = []
    for el in fl:
        if option == 'life_time':
            option_dict[el.name] = el.life_time
        elif option == 'length':
            option_dict[el.name] = el.length
        elif option == 'price':
            option_dict[el.name] = el.price
        elif option == 'color':
            option_dict[el.name] = el.color
        elif option == 'fresh':
            option_dict[el.name] = el.fresh
    sorted_keys = sorted(option_dict, key=option_dict.get)
    for key in sorted_keys:
        sorted_option[key] = option_dict[key]
    for key, item in sorted_option.items():
        if option == 'fresh':
            if not item:
                strings.append(f"{key}: not fresh")
            elif item:
                strings.append(f"{key}: fresh")
        else:
            strings.append(f"{key}: {item}")
    result = ", ".join(strings)
    return f"{result} with the sorted option {option} in the bouquet"


def search_logic(option, value, fl, names_list):
    if value in [operator.attrgetter(option)(el) for el in fl]:
        for el in fl:
            if operator.attrgetter(option)(el) == value:
                names_list.append(el.name)
            else:
                continue
        name_list_search = ", ".join(names_list)
        return f"{name_list_search} with the option {option} " \
               f"with the value {value} in the bouquet"
    else:
        return f'There is no such option {option} ' \
               f'with the value {value} in the bouquet'


def option_to_search(option, value, fl):
    names_list = []
    if option != 'fresh':
        return search_logic(option, value, fl, names_list)
    elif option == 'fresh':
        if value:
            for el in fl:
                if el.fresh:
                    names_list.append(el.name)
                else:
                    continue
            name_list_search = ", ".join(names_list)
            return f"{name_list_search} with the option fresh " \
                   f"with the value {value} in the bouquet"
        if not value:
            for el in fl:
                if not el.fresh:
                    names_list.append(el.name)
                else:
                    continue
            name_list_search = ", ".join(names_list)
            return f"{name_list_search} with the option fresh " \
                   f"with the value {value} in the bouquet"


class Flower:

    def __init__(self):
        self.life_time = 10
        self.color = 'white'
        self.fresh = True
        self.length = 6
        self.price = 10


class RedRose(Flower):

    def __init__(self):
        self.name = 'Red Rose'
        super().__init__()
        self.life_time = 3
        self.color = 'red'
        self.price = 40


class Marigold(Flower):

    def __init__(self):
        self.name = 'Marigold'
        super().__init__()
        self.life_time = 5
        self.color = 'orange'
        self.fresh = False
        self.length = 4
        self.price = 25


class Tulip(Flower):

    def __init__(self):
        self.name = 'Tulip'
        super().__init__()
        self.color = 'yellow'


class CollectBouquet:

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


red_rose = RedRose()
tulip = Tulip()
marigold = Marigold()
flowers = [red_rose, tulip, marigold]
counts = [2, 3, 4]
collect_bouquet = CollectBouquet(flowers, counts)
collect_bouquet.price_of_bouquet()
collect_bouquet.withering_time()
collect_bouquet.sort_option('color')
collect_bouquet.sort_option('fresh')
collect_bouquet.search_option('length', 3)
collect_bouquet.search_flower('White Rose')
