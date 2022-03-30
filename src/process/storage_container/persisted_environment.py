import json

from src.process.storage_container.environment import Environment


class PersistedEnvironment(Environment):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def __enter__(self):
        with open(self.file_name, 'w') as f:
            data = f.read()

        data_dict = json.loads(data)
        for key, value in data_dict:
            self.set_value(key, value)

        self.file = open(self.file_name, 'w')

        return self

    def __exit__(self):
        self.file.write(json.dumps(self.get_all()))
        self.file.close()
