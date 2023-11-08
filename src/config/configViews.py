import json

class Configuracion():
    def __init__(self, config_file='agenda-contactos/src/util/infoView.json'):
        with open(config_file,'r') as file:
            self.config = json.load(file) 