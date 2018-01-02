import abc


class MenuComponent(abc.ABC):

    @abc.abstractmethod
    def add(self, menu_item):
        pass

    @abc.abstractmethod
    def remove(self, menu_item):
        pass

    @abc.abstractmethod
    def get_memu_item(self, idx):
        pass

    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass

    @abc.abstractmethod
    def get_price(self):
        pass

    @abc.abstractmethod
    def is_vegetarian(self):
        pass

    @abc.abstractmethod
    def output(self):
        pass
