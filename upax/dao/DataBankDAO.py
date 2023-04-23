import json

from upax.db.DBPool import DBPool
from upax.model.FileBank import FileBank


class DataBankDAO:

    def update_info_bank(self, UserBank):
        cx = DBPool()
        if cx.is_alive():
            function_name = 'UPAXER.PAEXPEDIENTE.FNUPDATEDATABANK'
            paParams = {
                "paIdUser": UserBank.idUser,
                "paModifiedUser": UserBank.userModified
            }

            if not UserBank.depositAccount == None:
                paParams['paDepositAccount'] = UserBank.depositAccount
                paParams['paClabe'] = UserBank.clabe
                paParams['paIdBank'] = UserBank.idBank
            elif not UserBank.cardNumber == None:
                paParams['paIdBank'] = UserBank.idBank
                paParams['paCardNumber'] = UserBank.cardNumber
            elif not UserBank.paypalAccount == None:
                paParams['paPaypalAccount'] = UserBank.paypalAccount

            file = DBPool().execute('FN', function_name, 'numeric', paParams)['data']

            if file == 1.0:
                return int(file)
            else:
                if "ORA-00001" in file:
                    return 0

    def update_status_user(self, idUser):
        if DBPool().is_alive():
            paParams = {
                "paIdUser": idUser,
                "paIdStatus": 1
            }
            return int(DBPool().execute('FN', 'PAUSUARIO.FNCHANGESTATUS', 'numeric', paParams)['data'])
        else:
            return None

    def get_data_bank(self, idUser):
        cx = DBPool()
        paParams = {
            "paIdUser": idUser
        }
        if cx.is_alive():
            fileBank = cx.execute('FN', 'PAEXPEDIENTE.FNUSERDATABANK', 'cursor', paParams)
            for bank in json.loads(fileBank['data']):
                file = FileBank(bank).create()
        return file
