class FileBank:

    def __init__(self, dict):
        self.dict = dict

    def create(self):
        return {
            'idFile': self.dict['FIIDEXPEDIENTE'],
            'idUser': self.dict['FIIDUSUARIO'],
            'idLevelStudy': self.dict['FIIDGRADOESTUDIOS'],
            'idGender': self.dict['FIIDGENERO'],
            'idBank': self.dict['FIIDBANCO'],
            'idCompanyRH': self.dict['FIIDCOMPANIARH'],
            'depositAccount': self.dict['FCCUENTADEPOSITO'],
            'clabe': self.dict['FCCLABE'],
            'rfc': self.dict['FCRFC'],
            'curp': self.dict['FCCURP'],
            'dateBirth': self.dict['FDFECHANACIMIENTO'],
            'contractProject': self.dict['FCPROYCONTRATO'],
            'lastDateModification': self.dict['ULTIMA_MODIFICACION'],
            'modificationUser': self.dict['USUARIO_MODIFICO'],
            'letter': self.dict['FICARTA'],
            'contract': self.dict['FICONTRATO'],
            'dateDocuments': self.dict['FDFECHADOCUMENTOS'],
            'idEncuTareaCero': self.dict['FIIDENCUTAREACERO'],
            'paypalAccount': self.dict['FCCUENTAPAYPAL'],
            'cardNumber': self.dict['FCNUMEROTARJETA']

        }
