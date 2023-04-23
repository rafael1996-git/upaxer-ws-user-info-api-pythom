class Upaxometer:

    def __init__(self, dict):
        self.dict = dict

    def create(self):
        return {
            'idPais': self.dict['IDPAIS'],
            'nombrePais': self.dict['NOMBREPAIS'],
            'idProyecto': self.dict['IDPROYECTO'],
            'nombreProyecto': self.dict['NOMBREPROYECTO'],
            'idTipoProyecto': self.dict['TIPOPROYECTO'],
            'tipoProyecto': self.dict['NOMBRETIPOPROYECTO'],
            'idTarea': self.dict['IDTAREA'],
            'nombreTarea': self.dict['NOMBRETAREA'],
            'idUsuario': self.dict['IDUSUARIO'],
            'idUbicacion': self.dict['IDUBICACION'],
            'idAsignacion': self.dict['FIIDASIGNACION'],
            'idDetalleTarea': self.dict['FIIDDETALLETAREA'],
            'estatus': self.dict['ESTATUSASIGNACION'],
            'auditoria': self.dict['ESTATUSAUDITORIA'],
            'confirma': self.dict['CONFIRMA'],
            'idPago': self.dict['IDPAGOS'],
            'monto': self.dict['MONTOPAGO'],
            'pago': self.dict['ESTATUSPAGO'],
            'nombreUbicacion': self.dict['NOMBREUBICACION'],
            'direccion': self.dict['DIRECCION'],
            'fechaVisita': self.dict['FECHAVISITA']
        }