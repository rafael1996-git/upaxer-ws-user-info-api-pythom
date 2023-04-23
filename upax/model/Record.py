class Record:

    def __init__(self, body):
        self.body = body

    def build(self):
        response = {
            'curp': self.body['FCCURP'],
            'rfc': self.body['FCRFC'],
            'tipoPago': self.body['FITIPOPAGO'],
            'cuentaDeposito': self.body['FCCUENTADEPOSITO']
        }
        return response