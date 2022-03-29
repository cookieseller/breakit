import json

from src.process.storage_container.environment import Environment


class PersistedEnvironment:
    def __init__(self, file_name):
        self.environment = Environment()
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self):
        self.file.write(json.dumps(self.environment.get_all()))
        self.file.close()
