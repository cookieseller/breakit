import json
from json import JSONDecodeError

from src.process.variable_storage.environment import Environment


class PersistedEnvironment(Environment):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def __enter__(self):
        with open(self.file_name, 'w+') as f:
            data = f.read()

        try:
            data_dict = json.loads(data)
            for key, value in data_dict:
                self.set_value(key, value)
        except JSONDecodeError:
            data_dict = {}

        return self

    def __exit__(self):
        file = open(self.file_name, 'w')
        file.write(json.dumps(self.get_all()))
        file.close()
