class User:

    def __init__(self, dict):
        self.dict = dict

    def create(self):
        return {
            'address': self.dict['FCDIRECCION'],
            'genero': self.dict['FIIDGENERO'],
            'age': self.dict['FDFECHANACIMIENTO'],
            'email': self.dict['FCCORREO'],
            'curp': self.dict['FCCURP']
        }

    def create_user(self):
        return {
            'name': self.dict['FCNOMBRE'],
            'firstName': self.dict['FCAPELLIDOPATERNO'],
            'lastName': self.dict['FCAPELLIDOMATERNO'],
            'gender': self.dict['FCDESCRIPCIONGENERO'],
            'cellphone': self.dict['FCCELULAR'],
            'postalCode': str(self.dict['FIIDCODIGOPOSTAL']),
            'email': self.dict['FCCORREO'],
            'curp': self.dict['FCCURP'],
            'status': self.dict['FIIDESTATUS']
        }

    def create_photo(self):
        return {
            'repositoryId': self.dict['FIIDREPOSITORIOMULTIMEDIA'],
            'recordId': self.dict['FIIDREGISTRO'],
            'typeDocument': self.dict['FIIDTIPODOCUMENTO'],
            'finalRoute': self.dict['FCRUTAFINAL'],

        }
