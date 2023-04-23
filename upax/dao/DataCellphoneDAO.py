from upax.db.DBPool import DBPool


class DataCellphoneDAO:

    def validate_data(self, idUser):
        if DBPool().is_alive():
            paParams = {
                'paUsrID': idUser
            }
            return int(DBPool().execute('FN', 'PADISPOSITIVOS.FNCONTEODISPOSITIVOSUSR', 'numeric', paParams)['data'])
        else:
            return None

    def insert_data(self, data):
        if DBPool().is_alive():
            paParams = {
                'paUsrId': data['idUser'],
                'paCelular': data['cellphone'],
                'paImei': data['imei'],
                'paOperador': data['operator'],
                'paIDVersionSW': data['idVersionSW'],
                'paSerialNumber': data['serialNumber'],
                'paSimOperator': data['simOperator'],
                'paSuscriberID': data['idSuscriber'],
                'paBrand': data['brand'],
                'paFingerPrint': data['fingerPrint'],
                'paVersionRelease': data['versionRelease'],
                'paVersionSDK': data['versionSDK'],
                'paModel': data['model'],
                'paTotalMemory': data['totalMemory'],
                'paToken': data['token'],
                'paUsrModifico': data['userModified']
            }
            return int(DBPool().execute('FN', 'PADISPOSITIVOS.FNINSERT', 'numeric', paParams)['data'])
        else:
            return None
