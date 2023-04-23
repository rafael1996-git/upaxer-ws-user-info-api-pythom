import json

from upax.db.DBPool import DBPool
from upax.model.Task import Task
from upax.model.UserRanking import UserRanking
import upax.utils.dbpackages as db


class RankingDAO:

    def get_tasks(self, idUser):
        tasks = []
        cx = DBPool()
        if cx.is_alive():
            paParams = {'PAIDUSUARIO': idUser}
            data = cx.execute('FN', db.RANKING_GETDATA, 'cursor', paParams)
            tasks = [Task(d).create() for d in json.loads(data['data'])]
        return tasks

    def update_ranking(self, idUser, points):
        update = 0
        cx = DBPool()
        if cx.is_alive():
            paParams = {
                'paIdUser': idUser,
                'paranking': points,
                'paModifiedUser': 'UPAXER'
            }
            update = cx.execute('FN', db.RANKING_UPDATERANKING, 'numeric', paParams)['data']
        return update

    def get_ranking(self, idUser):
        data = {}
        cx = DBPool()
        if cx.is_alive():
            paParams = {'paIdUser': idUser}
            info = cx.execute('FN', db.RANKING_GET, 'cursor', paParams)
            for i in json.loads(info['data']):
                data = UserRanking(i).create()
        return data



