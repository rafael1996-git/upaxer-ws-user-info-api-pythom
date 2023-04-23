class UpaxometerTask:

    def __init__(self, idAsignacion, nombreProyecto, tipoProyecto, direccion, fechaVisita, idDetalleTarea, statusAudit):
        self.idAsignacion = idAsignacion
        self.nombreProyecto = nombreProyecto
        self.direccion = direccion
        self.fechaVisita = fechaVisita
        self.tipoProyecto = tipoProyecto
        self.idDetalleTarea = idDetalleTarea
        self.statusAudit = statusAudit
        self.upaxometerStatus = {
            '1': 'Sincronizando multimedia',
            '2': 'Terminada',
            '3': 'Calidad',
            '4': 'Pagada',
            '5': 'Rechazada',
            '6': 'Por rehacer'
        }

    def set_status(self, status):
        return {
            'idAsignacion': self.idAsignacion,
            'nombreProyecto': self.nombreProyecto,
            'tipoProyecto': self.tipoProyecto,
            'direccion': self.direccion,
            'fechaVisita': self.fechaVisita,
            'estatus': status,
            'estatusAuditoria': self.statusAudit,
            'descripcion': self.upaxometerStatus[str(status)],
            'idDetalleTarea': self.idDetalleTarea
        }
