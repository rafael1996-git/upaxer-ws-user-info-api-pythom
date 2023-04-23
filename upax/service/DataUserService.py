from upax.dao.DataUserDAO import DataUserDAO
from upax.model.Response import Response
from upax.model.UpaxometerTask import UpaxometerTask
from upax.model.Validation import Validation
from upax.utils.constants import regex_email, SUCCESS_CODE, SUCCESS_MESSAGE, ERROR_CODE
import datetime
from datetime import datetime
import re


class DataUserService:

    def __init__(self, request):
        self.request = request
        self.dataUserDAO = DataUserDAO()

    def update_data_user(self):
        try:
            userId = self.request['idUser']
            user = self.dataUserDAO.get_data_user_info(userId)

            if user['status'] == 1:
                if 'curp' in self.request:
                    curp = self.dataUserDAO.get_exists_curp(self.request['curp'])
                    if curp != -1:
                        if user['curp'] != self.request['curp']:
                            return Response('UPX233', False, None, "CURP already exists")
                if 'email' in self.request and self.request['email'] is not None:
                    if not bool(re.search(regex_email, self.request['email'])):
                        return Response('UPX231', False, None, "Wrong email format")
                try:
                    datetime.strptime(self.request['dateBirth'], "%d/%m/%Y")
                except ValueError:
                    return Response('UPX232', False, None, "Wrong birthDate format")


                userTemp = {
                    'idUser': userId,
                    'name': self.request['name'] if 'name' in self.request else user['name'],
                    'firstName': self.request['firstName'] if 'firstName' in self.request else user[
                        'firstName'],
                    'lastName': self.request['lastName'] if 'lastName' in self.request else user['lastName'],
                    'curp': self.request['curp'] if 'curp' in self.request else user['curp'],
                    'address': self.request['address'],
                    'gender': self.request['gender'],
                    'dateBirth': self.request['dateBirth'],
                    'email': self.request['email'],
                    'cp': self.request['cp'],
                    'modifiedUser': self.request['modifiedUser']
                }



                userUpdate = self.dataUserDAO.update_data_user(userTemp)
                if userUpdate == 1:
                    return Response('UPX200', True, None, None)
                else:
                    return Response('UPX215', False, None, "Error updating user")

            elif user['status'] == -1:
                return Response('UPX205', False, None, "User does not exists")
            else:
                return Response('UPX214', False, None, "Invalid user status")

        except Exception as e:
            return Response(code=ERROR_CODE, success=False, response=None, message=str(e))

    def get_user(self):
        try:

            id_user = self.request['idUser']
            user_record = self.dataUserDAO.get_user_record(id_user=id_user)
            # ESTADO DE CUENTA
            # validation_account_data = self.dataUserDAO.get_validation_data(id_user=id_user, subitem=1)
            #account = user_record['cuentaDeposito']
            # INE
            validation_id_data = self.dataUserDAO.get_validation_data(id_user=id_user, subitem=2)
            curp = user_record['curp']
            # RFC
            validation_rfc_data = self.dataUserDAO.get_validation_data(id_user=id_user, subitem=3)
            rfc = user_record['rfc']
            # FOTO FRONTAL ID
            frontal_photo = self.get_multimedia_file(id_user=id_user, id_table=4, type_document=1, id_registry=1,
                                                     order=0)
            # FOTO REVERSO ID
            reverse_photo = self.get_multimedia_file(id_user=id_user, id_table=4, type_document=1, id_registry=2,
                                                     order=0)
            # FOTO ESTADO CUENTA
            account_photo = self.get_multimedia_file(id_user=id_user, id_table=1, type_document=3, id_registry=3,
                                                     order=0)
            user_profile = self.dataUserDAO.get_user_profile(id_user=id_user)
            user_type = user_record['tipoPago']
            user_app = True if user_profile != 9 else False
            response = {
                'userType': user_type,
                'userApp': user_app,
                'userData': {
                    'curp': Validation(body=validation_id_data, value=curp).build(),
                    'rfc': Validation(body=validation_rfc_data, value=rfc).build(),
                    'frontalIDPicture': Validation(body=validation_id_data, value=frontal_photo).build(),
                    'reverseIDPicture': Validation(body=validation_id_data, value=reverse_photo).build()
                }
            }
            '''response = {
                'userType': user_type,
                'userApp': user_app,
                'userData': {
                    'curp': Validation(body=validation_id_data, value=curp).build(),
                    'rfc': Validation(body=validation_rfc_data, value=rfc).build(),
                    'account': Validation(body=validation_account_data, value=account).build(),
                    'frontalIDPicture': Validation(body=validation_id_data, value=frontal_photo).build(),
                    'reverseIDPicture': Validation(body=validation_id_data, value=reverse_photo).build(),
                    'bankAccountPicture': Validation(body=validation_account_data, value=account_photo).build()
                }
            }'''
            """
            response = {
                "userProfile": 9,
                "userType": 2,
                "userData": {
                    "curp": {
                        "status": 3,
                        "value": "GORH920214HDFNVG06",
                        "description": "Pendiente",
                        "lastUpdate": int(datetime.now().timestamp())
                    },
                    "rfc": {
                        "status": 3,
                        "value": "GORH9202141C1",
                        "description": "Pendiente",
                        "lastUpdate": int(datetime.now().timestamp())
                    },
                    "account": {
                        "status": 3,
                        "value": "10301193152",
                        "description": "Pendiente",
                        "lastUpdate": int(datetime.now().timestamp())
                    },
                    "frontalIDPicture": {
                        "status": 3,
                        "value": "https://firebasestorage.googleapis.com/v0/b/upaxer/o/PAX%2F16994%2FPAX16994_20_06_2018_08_00_07_1529499612606.jpg?alt=media&token=c3bf3115-53c0-4f26-8b6d-24daba7962aa",
                        "description": "Pendiente",
                        "lastUpdate": int(datetime.now().timestamp())
                    },
                    "reverseIDPicture": {
                        "status": 3,
                        "value": "https://firebasestorage.googleapis.com/v0/b/upaxer/o/PAX%2F16994%2FPAX16994_20_06_2018_08_00_14_1529499618117.jpg?alt=media&token=7fd763d3-3e91-4dd7-870b-1f0040543a9a",
                        "description": "Pendiente",
                        "lastUpdate": int(datetime.now().timestamp())
                    },
                    "bankAccountPicture": {
                        "status": 3,
                        "value": "https://firebasestorage.googleapis.com/v0/b/upaxer-dev.appspot.com/o/PAX%2F96827%2F96827_1583913390229.png?alt=media&token=9234b547-81b6-4a95-8e7d-4cca81260a25",
                        "description": "Pendiente",
                        "lastUpdate": int(datetime.now().timestamp())
                    }
                }
            }
            """
            return Response(code=SUCCESS_CODE, success=True, response=response, message=SUCCESS_MESSAGE)
        except Exception as e:
            return Response(code=ERROR_CODE, success=False, response=None, message=str(e))

    def upaxometer(self):

        tasks = list()
        user_tasks = self.dataUserDAO.get_data_upaxometer(self.request['idUser'])
        assigns = list()
        for task in user_tasks:
            upaxometerTask = UpaxometerTask(
                task['idAsignacion'],
                task['nombreProyecto'],
                task['tipoProyecto'],
                task['direccion'],
                task['fechaVisita'],
                task['idDetalleTarea'],
                task['auditoria']
            )
            if not task['idAsignacion'] in assigns:
                if task['pago'] == 2:
                    tasks.append(upaxometerTask.set_status(4))
                    assigns.append(task['idAsignacion'])
                elif task['auditoria'] == 3 and task['confirma'] == 1:
                    tasks.append(upaxometerTask.set_status(5))
                    assigns.append(task['idAsignacion'])
                elif task['auditoria'] == 2 and task['confirma'] == 1:
                    tasks.append(upaxometerTask.set_status(3))
                    assigns.append(task['idAsignacion'])
                elif task['auditoria'] == 11:
                    tasks.append(upaxometerTask.set_status(6))
                    assigns.append(task['idAsignacion'])
                elif task['estatus'] == 3 or task['estatus'] == 5:
                    tasks.append(upaxometerTask.set_status(2))
                    assigns.append(task['idAsignacion'])
                elif task['estatus'] == 12:
                    tasks.append(upaxometerTask.set_status(1))
                    assigns.append(task['idAsignacion'])
            else:#Si esta en assigns
                #Si el estatus es igual en reasignada
                if task['auditoria'] == 11:
                    #Si esta en assigns y si tiene estatus 11 (por rehacer)
                    # Buscar el lugar en assigns de la existente, para remplazarla
                    lugar = assigns.index(task['idAsignacion'])
                    #remover existente
                    tasks.pop(lugar)
                    #insertar existente, en el mismo lugar
                    tasks.insert(lugar, upaxometerTask.set_status(6))
                    #insertar existente, en ultimo lugar
                    #tasks.append(upaxometerTask.set_status(6))

        return Response('UPX200', True, tasks, None)

    def get_multimedia_file(self, id_user, id_table, type_document, id_registry, order):
        id_user = str(id_user)
        response = self.dataUserDAO.get_multimedia_file(id_user=str(id_user), id_table=id_table,
                                                        type_document=type_document, id_registry=id_registry,
                                                        order=order)
        if response:
            return response[0]['FCRUTAFINAL']
        else:
            return None

    def get_record_user(self):
        try:
            id_user = self.request['idUser']
            # TOTAL PAYMENT
            total_payment = self.dataUserDAO.get_total_payments(id_user=id_user)
            # TOTAL TASK
            total_task = self.dataUserDAO.get_total_task(id_user=id_user)

            response = {
                'totalPayment': total_payment,
                'totalTask': total_task
            }
            return Response(code=SUCCESS_CODE, success=True, response=response, message=SUCCESS_MESSAGE)
        except Exception as e:
            return Response(code=ERROR_CODE, success=False, response=None, message=str(e))

    def get_user_info(self):
        try:
            user_id = self.request['userId']
            selfi_photo = None
            frontal_photo = None
            reverse_photo = None
            user_record = self.dataUserDAO.get_data_user_info(user_id)
            user_photos = self.dataUserDAO.get_photo_user(user_id)

            for photo in user_photos:
                if photo['typeDocument'] == 9:
                    selfi_photo = photo['finalRoute']
                elif photo['typeDocument'] == 1 and photo['recordId'] == 1:
                    frontal_photo = photo['finalRoute']
                elif photo['typeDocument'] == 1 and photo['recordId'] == 2:
                    reverse_photo = photo['finalRoute']
            user_profile = self.dataUserDAO.get_user_profile(id_user=user_id)
            user_app = True if user_profile != 9 else False
            response = {
                'name': user_record['name'],
                'firstName': user_record['firstName'],
                'lastName': user_record['lastName'],
                'gender': user_record['gender'],
                'cellphone': user_record['cellphone'],
                'postalCode': user_record['postalCode'],
                'email': user_record['email'],
                'curp': user_record['curp'],
                'profilePicture': selfi_photo,
                'frontalIDPicture': frontal_photo,
                'reverseIDPicture': reverse_photo,
                'userApp': user_app
            }

            return Response(code=SUCCESS_CODE, success=True, response=response, message=SUCCESS_MESSAGE)
        except Exception as e:
            return Response(code=ERROR_CODE, success=False, response=None, message=str(e))
