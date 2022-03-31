from src.process.variable_storage.variable_storage import VariableStorage


class Environment(VariableStorage):
    def __init__(self):
        self.store = {}

    def set_value(self, key, value):
        self.store[key] = value

    def get_value(self, key):
        return self.store[key]

    def has_value(self, key):
        return key in self.store

    def get_keys(self):
        return self.store.keys()

    def get_all(self):
        return self.store
