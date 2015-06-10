import os.path
import json

class ProbabilityLoader:
    def __init__(self, data_dir):
        self._data_dir = data_dir

    def load(self, name):
        path_to_data_file = os.path.join(self._data_dir, name + '.json')
        if not os.path.isfile(path_to_data_file):
            return None

        with open(path_to_data_file) as f:
            data = json.loads(f.read())

        return data

