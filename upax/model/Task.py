class Task:

    def __init__(self, dict):
        self.dict = dict

    def create(self):
        return {
            'idProyecto': self.dict['FIIDPROYECTO'],
            'idAsignacion': self.dict['FIIDASIGNACION'],
            'estatus': self.dict['FIIDESTATUS']
        }
