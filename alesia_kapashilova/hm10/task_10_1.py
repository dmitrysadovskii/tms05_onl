import operator


class Flower:

    def __init__(self):
        self.life_time = 10
        self.color = 'white'
        self.fresh = True
        self.length = 6
        self.price = 10


class Chamomile(Flower):

    def __init__(self):
        self.name = 'Chamomile'
        super().__init__()
        self.life_time = 7
        self.color = 'White'
        self.lenght = 50
        self.price = 61


class Rose(Flower):

    def __init__(self):
        self.name = 'Rose'
        super().__init__()
        self.life_time = 15
        self.color = 'Black'
        self.lenght = 70
        self.price = 64
        self.fresh = False


class Gerbera(Flower):

    def __init__(self):
        self.name = 'Gerbera'
        super().__init__()
        self.life_time = 14
        self.color = 'Pink'
        self.length = 50
        self.price = 39


class Orchid(Flower):

    def __init__(self):
        self.name = 'Orchid mini'
        super().__init__()
        self.life_time = 21
        self.color = 'Blue'
        self.length = 30
        self.price = 52


class Tulip(Flower):

    def __init__(self):
        self.name = 'Tulip'
        super().__init__()
        self.life_time = 9
        self.color = 'Yellow'
        self.length = 20
        self.price = 15
        self.fresh = False


class Bouquet:

    def __init__(self, flow, counts):
        self.flow = flow
        self.counts = counts

    def price_of_bouquet(self):
        price_list = []
        for flower in self.flow:
            each_price = self.counts[self.flow.index(flower)] * flower.price
            price_list.append(each_price)
        new_price_list = sum(price_list)
        print(f"The price of the bouquet is {new_price_list}")

    def withering_time(self):
        lifetime = []
        for flower in self.flow:
            lifetime.append(flower.life_time)
        lifetime = round(sum(lifetime) / len(self.flow), 1)
        print(f"The withering time of the bouquet is {lifetime} days")

    def sort_option(self, option):
        assert isinstance(option, str), "Option should be str"
        assert len(option) != 0, "Please enter an option"
        assert option in ['life_time', 'price', 'length', 'color', 'fresh'], \
            f"There is no such option {option}"
        result = ''
        result += option_to_sort(option, self.flow)
        print(f"{result}")

    def search_option(self, option, value):
        assert isinstance(option, str), "Option should be str"
        assert len(option) != 0, "Please enter an option"
        assert option in ['life_time', 'price', 'length', 'color', 'fresh'], \
            f"There is no such option {option}"
        assert isinstance(value, int), "Value should be int"
        assert value > 0, "Value must be positive"
        result = ''
        result += option_to_search(option, value, self.flow)
        print(f"{result}")

    def search_flower(self, elem):
        assert isinstance(elem, str), "The name of a flower should be str"
        assert len(elem) != 0, "Please enter the name of a flower"
        if elem in [flower.name for flower in self.flow]:
            print(f"{elem} is in the bouquet")
        else:
            print(f"{elem} is not in the bouquet")


def option_to_sort(option, flow):
    option_dict = {}
    sorted_option = {}
    strings = []
    for elem in flow:
        if option == "life_time":
            option_dict[elem.name] = elem.life_time
        elif option == "length":
            option_dict[elem.name] = elem.length
        elif option == "price":
            option_dict[elem.name] = elem.price
        elif option == "color":
            option_dict[elem.name] = elem.color
        elif option == "fresh":
            option_dict[elem.name] = elem.fresh
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


def search_logic(option, value, flow, names_list):
    if value in [operator.attrgetter(option)(elem) for elem in flow]:
        for elem in flow:
            if operator.attrgetter(option)(elem) == value:
                names_list.append(elem.name)
            else:
                continue
        name_list_search = ", ".join(names_list)
        return f"{name_list_search} with the option {option} with the value" \
               f" {value} in the bouquet "
    else:
        return f"There is no such option {option} with the value {value} in " \
               f"the bouquet "


def option_to_search(option, value, flow):
    names_list = []
    if option != 'fresh':
        return search_logic(option, value, flow, names_list)
    elif option == 'fresh':
        if value:
            for elem in flow:
                if elem.fresh:
                    names_list.append(elem.name)
                else:
                    continue
            name_list_search = ", ".join(names_list)
            return f"{name_list_search} with the option fresh with the value" \
                   f" {value} in the bouquet "
        if not value:
            for elem in flow:
                if not elem.fresh:
                    names_list.append(elem.name)
                else:
                    continue
            name_list_search = ", ".join(names_list)
            return f"{name_list_search} with the option fresh with the value" \
                   f"{value} in the bouquet"
