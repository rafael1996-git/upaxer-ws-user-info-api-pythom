class UserRanking:

    def __init__(self, dict):
        self.dict = dict

    def create(self):
        return {
            'idUsuario': self.dict['FIIDUSUARIO'],
            'ranking': self.dict['FIRANKING'],
            'fechaRanking': self.dict['FDFECHARANKING']
        }