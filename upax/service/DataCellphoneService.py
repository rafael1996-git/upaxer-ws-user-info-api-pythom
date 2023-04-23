from upax.dao.DataCellphoneDAO import DataCellphoneDAO
from upax.model.Response import Response


class DataCellphoneService:

    def __init__(self, request):
        self.request = request
        self.updateDataCellphoneDAO = DataCellphoneDAO()

    def update_data(self):
        dataExists = self.updateDataCellphoneDAO.validate_data(self.request['idUser'])

        if dataExists != 1:
            insert = self.updateDataCellphoneDAO.insert_data(self.request)
            if insert == 1:
                return Response('UPX211', True, None, None)
            if insert is None:
                return Response('UPX500', False, None, None)
            else:
                return Response('UPX212', False, None, None)
        else:
            return Response('UPX213', False, None, None)



