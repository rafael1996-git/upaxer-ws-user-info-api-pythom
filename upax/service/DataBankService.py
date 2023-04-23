from upax.dao.DataBankDAO import DataBankDAO
from upax.dao.DataUserDAO import DataUserDAO
from upax.model.Response import Response
from upax.model.UserBank import UserBank
from upax.utils.constants import SUCCESS_CODE, SUCCESS_MESSAGE, ERROR_CODE, INVALID_USER_CODE, INVALID_USER_MESSAGE, ERROR_UPDATING_MESSAGE


class DataBankService:

    def __init__(self, request):
        self.request = request
        self.dataBankDAO = DataBankDAO()
        self.dataUserDAO = DataUserDAO()

    def update_data_bank(self):
        try:
            id_user = self.request['idUser']
            userStatus = self.dataUserDAO.get_status(id_user)
            if userStatus != 4 and userStatus != 5 and userStatus != -1:
                id_bank = self.request['idBank']
                account = None if self.request['depositAccount'] == "" else self.request['depositAccount']
                clabe = None if self.request['clabe'] == "" else self.request['clabe']
                card_number = None if self.request['cardNumber'] == "" else self.request['cardNumber']
                paypal_account = None if self.request['paypalAccount'] == "" else self.request['paypalAccount']
                user_who_modified = self.request['userModified']
                userDataBank = UserBank(idUser=id_user, idBank=id_bank, depositAccount=account, clabe=clabe,
                                        paypalAccount=paypal_account, cardNumber=card_number,
                                        userModified=user_who_modified)
                response = self.dataBankDAO.update_info_bank(userDataBank)
                if response:
                    return Response(code=SUCCESS_CODE, success=True, response=None, message=SUCCESS_MESSAGE)
                else:
                    return Response(code=ERROR_CODE, success=False, response=None, message=ERROR_UPDATING_MESSAGE)
            else:
                return Response(code=INVALID_USER_CODE, success=False, response=None, message=INVALID_USER_MESSAGE)
        except Exception as e:
            return Response(code=ERROR_CODE, success=False, response=None, message=str(e))