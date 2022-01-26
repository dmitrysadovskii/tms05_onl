"""
Цветочница.
+ Определить иерархию и создать несколько цветов.
+ Собрать букет (можно использовать аксессуары) с определением его стоимости.
+ Определить время его увядания по среднему времени жизни всех цветов в букете.
+ Позволить сортировку цветов в букете на основе различных параметров
(свежесть/цвет/длина стебля/стоимость...)
+ Реализовать поиск цветов в букете по определенным параметрам.
+ Узнать, есть ли цветок в букете.
"""


class Flower:

    def __init__(self, country_of_origin, price, flower_name, kind_name,
                 color):
        self.country_of_origin = country_of_origin
        self.price = price
        self.flower_name = flower_name
        self.kind_name = kind_name
        self.color = color


class CutFlower(Flower):

    def __init__(self, country_of_origin, price, flower_name, kind_name, color,
                 cut_date, length, storage_temperature, life_time_days):
        super(CutFlower, self).__init__(country_of_origin, price, flower_name,
                                        kind_name, color)
        self.cut_date = cut_date
        self.length = length
        self.storage_temperature = storage_temperature
        self.life_time_days = life_time_days


class DriedFlower(Flower):

    def __init__(self, country_of_origin, price, flower_name, kind_name, color,
                 length, production_date, life_time_days):
        super(DriedFlower, self).__init__(country_of_origin, price,
                                          flower_name, kind_name, color)
        self.length = length
        self.production_date = production_date
        self.life_time_days = life_time_days


class PottedFlower(Flower):

    def __init__(self, country_of_origin, price, flower_name, kind_name, color,
                 height, width, length):
        super(PottedFlower, self).__init__(country_of_origin, price,
                                           flower_name, kind_name, color)
        self.height = height
        self.width = width
        self.length = length


class Accessories:

    def __init__(self, accessory_name, price, production_date, life_time_days,
                 material, height, width, length):
        self.accessory_name = accessory_name
        self.price = price
        self.production_date = production_date
        self.life_time_days = life_time_days
        self.material = material
        self.height = height
        self.width = width
        self.length = length


class Bouquet:

    num_of_bouquets = 0

    def __init__(self, customer_name, creation_date):
        self.customer_name = customer_name
        self.creation_date = creation_date
        self.items_in_bouquet = []
        Bouquet.num_of_bouquets += 1

    def add_item_to_bouquet(self, new_item):
        """
        Add new item to the list of which bouquet is made up.
        :param new_item: object of any class.
        :return: None.
        """
        self.items_in_bouquet.append(new_item)

    def calculate_price(self):
        """
        Calculate sum of money which a bouquet costs based on price of all the
        items in this bouquet if the item has a price.
        :return: total amount of money.
        """
        return sum([item.price for item in self.items_in_bouquet
                    if hasattr(item, 'price')])

    def check_item_in_bouquet(self, item_to_find):
        """
        For any single object check if it is present in bouquet or not.
        :param item_to_find: object of any class.
        :return: boolean.
        """
        return item_to_find in self.items_in_bouquet

    def check_flower_name_in_bouquet(self, flower_to_find):
        """
        Check if there is any item with flower name specified. Return True if
        there is at least one item with the same flower name.
        :param flower_to_find: flower name to find.
        :return: boolean.
        """
        flowers_list = []
        for item in self.items_in_bouquet:
            if isinstance(item, CutFlower) or isinstance(item, PottedFlower):
                item_check = item.flower_name.lower() == flower_to_find.lower()
                flowers_list.append(item_check)
        return any(flowers_list)

    def find_flowers_by_attribute(self, attribute_name, attribute_value):
        """
        Return list of flowers` names for which specified attribute has value
        equal to value being searched.
        :param attribute_name: attribute of the object
        :param attribute_value: value of the attribute for searching.
        :return: list of flowers` name which meet specified condition.
        """
        flowers_list = []
        for item in self.items_in_bouquet:
            # check if item has this attribute, otherwise > error:
            attr_is_present = hasattr(item, attribute_name)
            # check if item has flower_name, otherwise can not display it:
            name_is_present = hasattr(item, 'flower_name')
            # check if attribute value is equal to the target one:
            if attr_is_present:
                actual_value = getattr(item, attribute_name)
                name_is_valid = actual_value.lower() == attribute_value.lower()
                if attr_is_present and name_is_present and name_is_valid:
                    flowers_list.append(item.flower_name)
        return flowers_list

    def sort_flowers_by_attribute(self, attribute_name, ascending=True):
        """
        Get all values of the specified attribute and return them as a list of
        sorted values. Specify ascending=False to reverse sorting order.
        :param attribute_name: attribute from which to retrieve the values.
        :param ascending: boolean, True - ascending order, False - descending
        order.
        :return: list of sorted values.
        """
        items_list = [getattr(item, attribute_name)
                      for item in self.items_in_bouquet
                      if hasattr(item, attribute_name)]
        if ascending:
            return sorted(items_list)
        else:
            return sorted(items_list, reverse=True)

    def get_avg_lifetime(self):
        """
        Calculate average life-time of the bouquet based on life-time of all
        the items which have the attribute 'life_time_days'. If there is potted
        flower in the bouquet, then life-time can not be defined.
        :return: average life-time in days.
        """
        life_time_list = []
        for item in self.items_in_bouquet:
            if isinstance(item, PottedFlower):
                return 'Life time is not limited.'
            elif hasattr(item, 'life_time_days') and isinstance(item, Flower):
                life_time_list.append(getattr(item, 'life_time_days'))
        return round(sum(life_time_list) / len(life_time_list))
