from .menu_component import MenuComponent


class MenuItem(MenuComponent):

    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def add(self, menu_item):
        pass

    def remove(self, menu_item):
        pass

    def get_memu_item(self, idx):
        pass

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def is_vegetarian(self):
        return self.vegetarian

    def output(self):
        if self.vegetarian:
            return '  {}(v), {}     -- {}'.format(self.name, self.price, self.description)
        return '  {}, {}     -- {}'.format(self.name, self.price, self.description)
