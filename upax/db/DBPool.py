import json
import cx_Oracle
#from bson import json_util
import os
#from upax.config.RemoteConfig import RemoteConfig
from upax.utils.Secret import get_secret

oracle_Types = {
    'cursor': cx_Oracle.CURSOR,
    'numeric': cx_Oracle.NUMBER,
    'string': cx_Oracle.STRING
}


class DBPool:
    validar_lib = True

    def __init__(self):

        ambiente_local = False
        if ambiente_local:
            self.server = "bdupaxerdev.cvwnpg9hzinn.us-east-1.rds.amazonaws.com"
            self.port = 1521
            self.service_name = "UPAXDEV"
            self.user = "TSTUPAXER"
            self.password = "UpaXER2022@"
        else:
            self.access_data = get_secret(os.environ['SECRET_ORACLE'])  # RemoteAccessData().get()
            self.server = self.access_data['server']
            self.port = self.access_data['port']
            self.service_name = self.access_data['service']
            self.user = self.access_data['user']
            self.password = self.access_data['password']

        url = self.user + "/" + self.password + "@" + self.server + ":" + str(self.port) + "/" + self.service_name

        if ambiente_local:
            if DBPool.validar_lib:
                cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_8")
                DBPool.validar_lib = False

        self.conn = cx_Oracle.connect(url)
        self.cursor = self.conn.cursor()

    def is_alive(self):
        self.cursor.execute("select 1 from DUAL")
        if (self.cursor.fetchall()):
            return True
        else:
            return False

    def execute(self, method, name, type, params):

        db_dto = {}
        data = []

        if (method == 'FN'):
            try:
                db_execute = self.cursor.callfunc(name, oracle_Types[type],
                                                  keywordParameters=params) if params != None else self.cursor.callfunc(
                    name, oracle_Types[type])
                if type == 'cursor':
                    columns = [field[0] for field in db_execute.description]
                    rows = db_execute.fetchall()
                    data = [dict(zip(columns, row)) for row in rows]
                    for d in data:
                        for key, value in d.items():
                            if isinstance(d[key], cx_Oracle.LOB):
                                d[key] = json.loads(str(value))
                    db_dto = {
                        "hasError": False,
                        "data": json.dumps(data)
                        #"data": json.dumps(data, default=json_util.default)
                    }
                else:
                    db_dto = {
                        "hasError": False,
                        "data": db_execute
                    }
            except Exception as e:
                db_dto = {
                    "hasError": True,
                    "data": str(e)
                }
            self.conn.close()
            return db_dto
        elif (method == 'SP'):
            result = self.cursor.var(oracle_Types[type])
            params.append(result)
            self.conn.close()
            return self.cursor.callproc(name, params)