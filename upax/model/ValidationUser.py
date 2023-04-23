class ValidationUser:

    def __init__(self, body):
        self.body = body

    def create(self):
        response = {
            'idUsuario': self.body['FIIDUSUARIO'] if self.body else None,
            'idExpediente': self.body['FIIDEXPEDIENTE'] if self.body else None,
            'perfil': self.body['FIIDPERFIL'] if self.body else None,
            'curp': self.body['FCCURP'] if self.body else None,
            'rfc': self.body['FCRFC'] if self.body else None,
            'cuentaDeposito': self.body['FCCUENTADEPOSITO'] if self.body else None,
            'tipoPago': self.body['FITIPOPAGO'] if self.body else None,
            'estatus': self.body['FIESTATUS'] if self.body else None,
            'descripcion': self.body['FCDESCRIPTION'] if self.body else None,
            'lastUpdate': self.body['LASTUPDATE'] if self.body else None
        }
        return response