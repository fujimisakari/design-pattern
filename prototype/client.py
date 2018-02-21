

class Client():

    def __init__(self):
        self.prototype_map = {}

    def regist(self, key, prototype):
        self.prototype_map[key] = prototype

    def create(self, key):
        prototype = self.prototype_map[key]
        return prototype.create_clone()
