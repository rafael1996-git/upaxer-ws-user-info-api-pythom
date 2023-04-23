import datetime
from upax.dao.RankingDAO import RankingDAO
from upax.model.Response import Response


class RankingService:

    def __init__(self, request):
        self.request = request
        self.rankingDAO = RankingDAO()

    def get_rank(self):

        exists = self.rankingDAO.exists_assignment(self.request['idUser'])

        if exists == 1:
            ranking = self.rankingDAO.get_rank(self.request['idUser'])
            return Response('UPX200', True, ranking, None)
        elif exists == 0:
            return Response('UPX200', True, "5.0", None)
        elif exists is None:
            return Response('UPX500', True, None, None)

    def get_ranking(self):
        points = 3
        try:
            rankingData = self.rankingDAO.get_ranking(self.request['idUser'])
            evalMonth = (datetime.datetime.now().replace(day=1) - datetime.timedelta(days=1)).month
            if rankingData['fechaRanking']:
                rankingMonth = datetime.datetime.utcfromtimestamp(rankingData['fechaRanking']['$date'] * 0.001).month
            else:
                rankingMonth = 0
            if not evalMonth == rankingMonth: #or actualMonth == rankingMonth:
                tasks = self.rankingDAO.get_tasks(self.request['idUser'])
                #conektaPoint = 0.5
                proyects = list()
                complete = 0
                canceled = 0
                for task in tasks:
                    if not task['idProyecto'] in proyects:
                        proyects.append(task['idProyecto'])
                    if task['estatus'] == 3:
                        complete += 1
                    if task['estatus'] == 4 or task['estatus'] == 5:
                        canceled += 1
                    if task['estatus'] == 6:
                        points -= 0.5

                if len(tasks) > 0:
                    points = points +  (0.5 if len(proyects) >= 2 else 0) + (0.5 if complete/len(tasks) >= 0.8 else 0) + (0.5 if len(tasks) >= 6 else 0) - (0.5 if canceled >= 2 else 0)
                else:
                    points = 3.0
                self.rankingDAO.update_ranking(self.request['idUser'], points)
            else:
                points = rankingData['ranking']

            return Response('UPX200', True, {'idUser': self.request['idUser'], 'ranking': points}, None)

        except Exception as e:
            return Response('UPX500', False, None, 'Something went wrong: ' + str(e))





