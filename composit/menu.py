from .menu_component import MenuComponent


class Menu(MenuComponent):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.menu_items = []

    def add(self, menu_item):
        self.menu_items.add(menu_item)

    def remove(self, menu_item):
        self.menu_items.remove(menu_item)

    def get_memu_item(self, idx):
        return self.menu_items[idx]

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        pass

    def is_vegetarian(self):
        pass

    def output(self):
        menu_title = '\n{} {}---------------------'.format(self.name, self.description)
        print(menu_title)

        for menu_item in self.menu_items:
            print(menu_item.output())
