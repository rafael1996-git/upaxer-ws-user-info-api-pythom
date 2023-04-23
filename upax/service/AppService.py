from upax.service.DataBankService import DataBankService
from upax.service.DataCellphoneService import DataCellphoneService
from upax.service.DataUserService import DataUserService
from upax.service.RankingService import RankingService


class AppService:

    def __init__(self, request):
        self.request = request

    def update_data_cellphone(self):
        return DataCellphoneService(self.request).update_data()

    def get_rank(self):
        return RankingService(self.request).get_rank()

    def update_data(self):
        return DataUserService(self.request).update_data()

    def update_data_bank(self):
        return DataBankService(self.request).data_bank()

    def update_data_user(self):
        return DataUserService(self.request).update_data_user()

    def get_user(self):
        return DataUserService(self.request).get_user()

    def get_ranking(self):
        return RankingService(self.request).get_ranking()

    def upaxometer(self):
        return DataUserService(self.request).upaxometer()

    def get_record_user(self):
        return DataUserService(self.request).get_record_user()

    def get_user_info(self):
        return DataUserService(self.request).get_user_info()
