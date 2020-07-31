import json


class Logger:
    def __init__(self, path):
        self.__data = ''
        self.__path = path
        self.load_data()

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def load_data(self):
        data = open(self.__path)
        if json:
            self.__data = data
        else:
            self.__data = dict()

    def save(self):
        data = self.__data
        with open(self.__path, 'w+') as fdin:
            fdin.write(data)

    def get_last(self, key, default=None):
        data = self.__data[0]
        if key in data:
            return data[key]
        else:
            return default

