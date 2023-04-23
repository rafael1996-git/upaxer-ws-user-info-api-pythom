import time

class Validation:

    def __init__(self, body, value):
        self.body = body
        self.value = value

    def build(self):
        last_update = int(time.mktime(time.strptime(self.body['lastUpdate'], '%d/%m/%Y %H:%M:%S'))) if not self.body['lastUpdate'] == None else None
        response = {
            'status': 0 if self.body['estatus'] == None else self.body['estatus'],
            'value': self.value,
            'description': self.body['descripcion'],
            'lastUpdate': last_update
        }
        return response