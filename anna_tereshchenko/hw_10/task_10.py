class Decoration:
    def __init__(self, name: str, cost: int):
        self.name = name
        self.cost = cost

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value:
            raise AttributeError('Name must not be empty')
        self._name = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value: int):
        if value <= 0:
            raise AttributeError('Cost must be > 0')
        self._cost = value


class Flower:
    def __init__(self, name: str, lifetime: int, color: str,
                 stem_length: int, cost: int):
        self.name = name
        self.lifetime = lifetime
        self.color = color
        self.stem_length = stem_length
        self.cost = cost

    def __getitem__(self, __name: str):
        return getattr(self, __name, None)

    def __str__(self):
        return f'{self.name}, {self.lifetime} days of lifetime,' \
               f'{self.color} color, {self.stem_length} cm, {self.cost}$'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value:
            raise AttributeError('Name must not be empty')
        self._name = value

    @property
    def lifetime(self):
        return self._lifetime

    @lifetime.setter
    def lifetime(self, value: int):
        if value <= 0:
            raise AttributeError('Lifetime must be > 0')
        self._lifetime = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value: str):
        if not value:
            raise AttributeError('Color must not be empty')
        self._color = value

    @property
    def stem_length(self):
        return self._stem_length

    @stem_length.setter
    def stem_length(self, value: int):
        if value <= 0:
            raise AttributeError('Stem length must be > 0')
        self._stem_length = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value: int):
        if value <= 0:
            raise AttributeError('Cost must be > 0')
        self._cost = value


class Bouquet:
    def __init__(self, flowers: list, accessories: list):
        self.flowers = flowers
        self.accessories = accessories

    @property
    def flowers(self):
        return self._flowers

    @flowers.setter
    def flowers(self, value: list):
        if len(value) == 0:
            raise AttributeError('A bouquet must have at least one flower')
        for fl in value:
            if not isinstance(fl, Flower):
                raise AttributeError('A bouquet must have only'
                                     'Flowers and Decor')
        self._flowers = value

    @property
    def accessories(self):
        return self._accessories

    @accessories.setter
    def accessories(self, value: list):
        for accessor in value:
            if not isinstance(accessor, Decoration):
                raise AttributeError('A bouquet must have only'
                                     'Flowers and Decor')
        self._accessories = value

    def get_bouquet_cost(self):
        total_flowers_cost = sum([flower.cost for flower in self.flowers])
        total_accessories_cost = sum([accessor.cost
                                      for accessor in self.accessories])
        total_bouquet_cost = total_flowers_cost + total_accessories_cost
        print(f'The bouquet cost = {total_bouquet_cost}')

    def get_bouquet_lifetime(self):
        bouquet_lifetime_sum = sum([flower.lifetime
                                    for flower in self.flowers])
        bouquet_lifetime = round(bouquet_lifetime_sum / len(self.flowers))
        print(f'The bouquet lifetime = {bouquet_lifetime} days')

    def sort_by(self, sort_by: str):
        if not self.flowers[0][sort_by]:
            print('There is no such property in flower')
        else:
            sorted_flowers = sorted(self.flowers,
                                    key=lambda flower: flower[sort_by])
            for fl in sorted_flowers:
                print(fl)

    def is_flower_in_bouquet(self, flower_name: Flower):
        if flower_name in self.flowers:
            print(f'There is a {flower_name.name} in the bouquet')
        else:
            print(f'There is no {flower_name.name} in the bouquet')

    def get_flower_by_param(self, param: str, value):
        filtered_flowers = list(filter(lambda fl: fl[param] == value,
                                       self.flowers))
        if len(filtered_flowers) == 0:
            print('There are no flowers in the bouquet with specified params')
        else:
            for fl in filtered_flowers:
                print(fl)


vase = Decoration('vase', 40)
craft_paper = Decoration('craft paper', 3)
decorative_ribbon = Decoration('decorative ribbon', 5)
red_rose = Flower('Red rose', 20, 'red', 99, 50)
white_rose = Flower('White rose', 14, 'white', 40, 2)
black_rose = Flower('Black rose', 10, 'black', 45, 4)
blue_rose = Flower('Blue rose', 9, 'blue', 45, 5)
flowers = [white_rose, red_rose, white_rose]
decor = [vase, craft_paper]
white_red_white_roses = Bouquet(flowers, decor)
white_red_white_roses.get_bouquet_cost()
white_red_white_roses.get_bouquet_lifetime()
white_red_white_roses.sort_by('cost')
white_red_white_roses.get_flower_by_param('color', 'white')
white_red_white_roses.is_flower_in_bouquet(red_rose)
