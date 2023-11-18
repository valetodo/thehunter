import os


class Pruebas(object):

    def __init__(self):
        self.API_HOSTS = {
            "test": "http://localhost:10004/wp-json/wc/v3/",
            "dev": "",
            "prod": ""
        }
        self.env = os.environ.get('hola', 'test')
        self.base_url = self.API_HOSTS[self.env]
        print(self.base_url)


p = Pruebas()
