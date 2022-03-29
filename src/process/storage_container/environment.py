class Environment:
    def __init__(self):
        self.store = {}

    def set_value(self, key, value):
        self.store[key] = value

    def get_value(self, key):
        return self.store[key]

    def get_keys(self):
        return self.store.keys()

    def get_all(self):
        return self.store
