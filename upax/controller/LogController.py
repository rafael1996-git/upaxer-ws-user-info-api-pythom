import boto3
from json import dumps
from datetime import datetime
import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class LogController():

    def stream(self, path, service_name, request, response):
        logger.info("Request: " + str(request))
        logger.info("Response: " + str(response))
        client = boto3.client('firehose', region_name='us-east-1')
        event = {}
        event['os'] = request['os']
        if 'idUser' in request:
            event['idUser'] = request['idUser']
            del request['idUser']
        else:
            event['idUser'] = 'LOGIN'
        del request['os']
        event['request'] = dumps(request)
        event['response'] = dumps(response)
        event['path'] = path
        event['service'] = service_name
        event[u'EventTime'] = datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S.%fZ')

        response = client.put_record(
            DeliveryStreamName = 'LOGS_UPXSLS',
            Record = {
                'Data': dumps(event)
            }
        )

        print(response)