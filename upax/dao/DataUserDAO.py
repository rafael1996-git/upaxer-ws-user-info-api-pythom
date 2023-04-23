import json

from upax.db.DBPool import DBPool
from upax.model.User import User
from upax.model.Upaxometer import Upaxometer
from upax.model.ValidationUser import ValidationUser
from upax.model.Record import Record
import upax.utils.dbpackages as db
import os

os.environ["NLS_LANG"] = "SPANISH_SPAIN.UTF8"

class DataUserDAO:

    def get_status(self, idUser):
        cx = DBPool()
        if cx.is_alive():
            function_name = 'UPAXER.PAUSUARIO.FNGETSTATUS'
            paParams = {
                'paIdUser': idUser
            }
            return int(DBPool().execute('FN', function_name, 'numeric', paParams)['data'])
        else:
            return None

    def update_data(self, data):
        if DBPool().is_alive():
            paParams = {
                "paIdUser": data['idUser'],
                "paBirthDate": data['birthDate'],
                "paGender": data['gender'],
                "paModifiedUser": data['modifiedUser']
            }
            return int(DBPool().execute('FN', db.USUARIO_UPDATE_EXP, 'numeric', paParams)['data'])
        else:
            return None



    def update_data_user(self, data):
        if DBPool().is_alive():
            paParams = {
                "paUsrId": data['idUser'],
                "paDireccion": data['address'],
                "paGenero": data['gender'],
                "paFechaNacimiento": data['dateBirth'],
                "paCorreo": data['email'],
                "paCodigoPostal": data['cp'],
                "paUsrModifico": data['modifiedUser'],
                "paNombre": data['name'],
                "paApellidopPaterno": data['firstName'],
                "paApellidoMaterno" : data['lastName'],
                "paCurp" : data['curp']
            }
            return int(DBPool().execute('FN', db.USUARIO_UPDATE_USER, 'numeric', paParams)['data'])
        else:
            return None

    def get_data_user(self, idUser):
        user = {}
        cx = DBPool()
        if cx.is_alive():
            paParams = {
                'paUsrId': idUser
            }
            data = cx.execute('FN', db.USUARIO_GET_DATA, 'cursor', paParams)
            for userData in json.loads(data['data']):
                user = User(userData).create()
        return user

    def get_data_upaxometer(self, idUser):
        upaxometer = list()
        cx = DBPool()
        if cx.is_alive():
            paParams = {'PAIDUSUARIO': idUser}
            data = cx.execute('FN', db.UPAXOMETER_GET_DATA, 'cursor', paParams)
            for d in json.loads(data['data']):
                upaxometer.append(Upaxometer(d).create())
        return upaxometer

    def get_validation_data(self, id_user, subitem):
        response = ValidationUser(None).create()
        cx = DBPool()
        function_name = 'UPAXER.PAVALIDACIONEXPEDIENTES.FNGETVALIDATIONDATA'
        payload = {
            'paIdUser': id_user,
            'paSubitemId': subitem
        }
        data = cx.execute('FN', function_name, 'cursor', payload)
        for d in json.loads(data['data']):
            response = ValidationUser(d).create()
        return response

    def get_multimedia_file(self, id_user, id_table, type_document, id_registry, order):
        cx = DBPool()
        function_name = 'UPAXER.PAUSUARIO.FNGETPICTUREUSER'
        payload = {
            'paIdUsuario': id_user,
            'paIdTabla': id_table,
            'paIdTipoDocumento': type_document,
            'paIdRegistro': id_registry,
            'paIdOrden': order
        }
        response = cx.execute('FN', function_name, 'cursor', payload)
        return json.loads(response['data'])


    def get_user_profile(self, id_user):
        cx = DBPool()
        function_name = 'UPAXER.PAUSUARIO.FNGETUSERPROFILE'
        payload = {
            'paIdUsuario': id_user
        }
        response = cx.execute('FN', function_name, 'numeric', payload)
        return int(response['data'])

    def get_user_record(self, id_user):
        cx = DBPool()
        response = {}
        function_name = 'UPAXER.PAUSUARIO.FNGETRECORDUSER'
        payload = {
            'paIdUsuario': id_user
        }
        data = cx.execute('FN', function_name, 'cursor', payload)
        for d in json.loads(data['data']):
            response = Record(d).build()
        return response

    def get_total_task(self, id_user):
        cx = DBPool()
        function_name = 'UPAXER.PAASIGNACION.FNGETTOTALTASK'
        payload = {
            'PAUSER': id_user
        }
        response = cx.execute('FN', function_name, 'numeric', payload)
        return int(response['data'])

    def get_total_payments(self, id_user):
        cx = DBPool()
        function_name = 'UPAXER.PAAUDITORIAPAGOS.FNGETTOTALPAYMENTS'
        payload = {
            'PAUSER': id_user
        }
        response = cx.execute('FN', function_name, 'numeric', payload)
        return int(response['data'])

    def get_data_user_info(self, userId):
        user = {}
        cx = DBPool()
        if cx.is_alive():
            paParams = {
                'paUsuario': userId
            }
            data = cx.execute('FN', db.GET_USER_DATA, 'cursor', paParams)
            for userData in json.loads(data['data']):
                user = User(userData).create_user()
        return user

    def get_photo_user(self, userId):

        cx = DBPool()
        if cx.is_alive():
            paParams = {
                'paUserId': userId
            }
            data = cx.execute('FN', db.GET_PHOTO_USER, 'cursor', paParams)
            photosUser = list()
            for photo in json.loads(data['data']):
                photosUser.append(User(photo).create_photo())
        return photosUser

    def get_exists_curp(self, curp):
        cx = DBPool()
        payload = {
            'paCURP': curp
        }
        response = cx.execute('FN', db.GET_EXISTS_CURP, 'numeric', payload)
        return int(response['data'])










