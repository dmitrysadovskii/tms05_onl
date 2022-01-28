class Flowers:

    def __init__(self, flower_name: str, flower_color: str,
                 freshness: int, stem_length: int, price: float):
        self.flower_name = flower_name
        self.flower_color = flower_color
        self.freshness = freshness
        self.stem_length = stem_length
        self.price = price

    def __getitem__(self, __flower_name: str):
        return getattr(self, __flower_name, None)

    def __str__(self):
        return f'{self.flower_name}, {self.freshness} days of lifetime,' \
               f'{self.flower_color} color, {self.stem_length} cm, ' \
               f'{self.price}$'

    @property
    def flower_name(self):
        return self._flower_name

    @flower_name.setter
    def flower_name(self, value: str):
        if not value:
            raise AttributeError("Missing flower names")
        self._flower_name = value

    @property
    def flower_color(self):
        return self._flower_color

    @flower_color.setter
    def flower_color(self, value: str):
        if not value:
            raise AttributeError('Flower color name missing')
        self._flower_color = value

    @property
    def freshness(self):
        return self._freshness

    @freshness.setter
    def freshness(self, value: int):
        if value <= 0:
            raise AttributeError('The lifetime must be > 0')
        self._freshness = value

    @property
    def stem_length(self):
        return self._stem_length

    @stem_length.setter
    def stem_length(self, value: int):
        if value <= 0:
            raise AttributeError('The stem length must be > 0')
        self._stem_length = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise AttributeError('The price must be > 0')
        self._price = value


class Accessories:
    def __init__(self, accessory_name: str, price: float):
        self.accessory_name = accessory_name
        self.price = price

    @property
    def accessory_name(self):
        return self._accessory_name

    @accessory_name.setter
    def accessory_name(self, value: str):
        if not value:
            raise AttributeError('Missing accessory name')
        self._accessory_name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise AttributeError('The price must be > 0')
        self._price = value


class Bouquet:
    def __init__(self, flowers: list, accessory: list):
        self.flowers = flowers
        self.accessory = accessory

    @property
    def flowers(self):
        return self._flowers

    @flowers.setter
    def flowers(self, value: list):
        if len(value) == 0:
            raise AttributeError('The bouquet must contain'
                                 ' at least one flower ')
        for flow in value:
            if not isinstance(flow, Flowers):
                raise AttributeError('A bouquet must have only'
                                     ' flowers and decor')
        self._flowers = value

    @property
    def accessory(self):
        return self._accessory

    @accessory.setter
    def accessory(self, value: list):
        for decor in value:
            if not isinstance(decor, Accessories):
                raise AttributeError('A bouquet must have only'
                                     'flowers and decor')
        self._accessory = value

    def get_bouquet_price(self):
        flowers_price = sum([flower.price for flower in self.flowers])
        accessory_price = sum([decor.price for decor in self.accessory])
        bouquet_price = flowers_price + accessory_price
        print(f'The bouquet price = {bouquet_price}')

    def get_bouquet_freshness(self):
        bouquet_freshness_sum = sum([flower.freshness
                                    for flower in self.flowers])
        bouquet_freshness = round(bouquet_freshness_sum / len(self.flowers))
        print(f'The bouquet lifetime = {bouquet_freshness} days')

    def get_sort_flower(self, sort_flower: str):
        if not self.flowers[0][sort_flower]:
            print('There is no such parameter in the database.'
                  ' Please enter a different one ')
        else:
            sorted_flowers = sorted(self.flowers,
                                    key=lambda flower: flower[sort_flower])
            for flow in sorted_flowers:
                print(flow)

    def flower_in_bouquet(self, name_flowers: Flowers):
        if name_flowers in self.flowers:
            print(f'There is a {name_flowers.flower_name} in the bouquet')
        else:
            print(f'There is no {name_flowers.flower_name} in the bouquet')

    def get_flower_by_param(self, param: str, value):
        filtered_flowers = list(filter(lambda flowe: flowe[param] == value,
                                       self.flowers))
        if len(filtered_flowers) == 0:
            print('There are no such parameters in the database.'
                  ' Please enter a different one')
        else:
            for flow in filtered_flowers:
                print(flow)


fl_1 = Flowers('Rose', 'Pink', 4, 55, 100.33)
fl_2 = Flowers('Rose', 'White', 5, 45, 103.05)
fl_3 = Flowers('Chrysanthemum ', 'Green', 10, 70, 80.27)
fl_4 = Flowers('Chrysanthemum ', 'Blue', 10, 70, 81.65)
dec_1 = Accessories('White box', 20.55)
dec_2 = Accessories('Colorful ribbons ', 1.87)
dec_3 = Accessories('Floral sponge', 2.02)
bouquet = [fl_1, fl_2, fl_3]
decoring = [dec_1, dec_2, dec_3, dec_2]
composition = Bouquet(bouquet, decoring)
composition.get_bouquet_price()
composition.flower_in_bouquet(fl_4)
composition.flower_in_bouquet(fl_3)
composition.get_bouquet_freshness()
composition.get_sort_flower('freshness')
composition.get_flower_by_param('flower_color', "Pink")
composition.get_flower_by_param('flower_color', "Blue")
