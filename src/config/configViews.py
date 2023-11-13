import json

class Configuracion():
    def __init__(self, config_file='src/util/infoView.json'):
        with open(config_file,'r') as file:
            self.config = json.load(file) 