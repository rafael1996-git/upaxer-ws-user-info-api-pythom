from flask import Flask, request
import logging
import json
from flask_cors import CORS, cross_origin
from upax.controller.UpaxController import UpaxController
from upax.controller.LogController import LogController
from upax.service.AppService import AppService
from upax.service.DataBankService import DataBankService
import upax.utils.properties as prop

logger = logging.getLogger()
logger.setLevel(logging.INFO)
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
url_path = '/' + prop.path


@app.route(url_path + '/update_data_bank', methods=['PUT'])
@cross_origin()
def update_data_bank():
    req = UpaxController().decrypt(request.data)
    data_bank_service = DataBankService(req)
    response = data_bank_service.update_data_bank()
    LogController().stream('user_info', 'update_data_bank', req, response.response)
    return UpaxController().encrypt(response.create())


@app.route(url_path + '/update_info_user', methods=['PUT'])
@cross_origin()
def user_update():
    req = UpaxController().decrypt(request.data)
    app_service = AppService(req)
    response = app_service.update_data_user()
    LogController().stream('user_info', 'update_info_user', req, response.response)
    return UpaxController().encrypt(response.create())


@app.route(url_path + '/get_user', methods=['POST'])
@cross_origin()
def user():
    req = UpaxController().decrypt(request.data)
    logger.info(req)
    app_service = AppService(req)
    response = app_service.get_user()
    LogController().stream('user_info', 'get_user', req, response.response)
    return UpaxController().encrypt(response.create())


@app.route(url_path + '/get_ranking', methods=['POST'])
@cross_origin()
def ranking():
    req = UpaxController().decrypt(request.data)
    app_service = AppService(req)
    response = app_service.get_ranking()
    LogController().stream('user_info', 'get_ranking', req, response.response)
    return UpaxController().encrypt(response.create())


@app.route(url_path + '/upaxometer', methods=['POST'])
@cross_origin()
def upaxometer():
    req = UpaxController().decrypt(request.data)
    app_service = AppService(req)
    response = app_service.upaxometer()
    LogController().stream('user_info', 'upaxometer', req, response.response)
    return UpaxController().encrypt(response.create())


@app.route(url_path + '/get_record_user', methods=['POST'])
@cross_origin()
def record_user():
    req = UpaxController().decrypt(request.data)
    logger.info(req)
    app_service = AppService(req)
    response = app_service.get_record_user()
    LogController().stream('user_info', 'get_user', req, response.response)
    return UpaxController().encrypt(response.create())


@app.route(url_path + '/get_user_info', methods=['POST'])
@cross_origin()
def user_info():
    req = UpaxController().decrypt(request.data)
    logger.info(req)
    app_service = AppService(req)
    response = app_service.get_user_info()
    LogController().stream('user_info', 'get_user', req, response.response)
    return UpaxController().encrypt(response.create())


if __name__ == '__main__':
    app.run()
