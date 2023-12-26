import os
import logging
import jsonpickle
import boto3
#from aws_xray_sdk.core import xray_recorder
#from aws_xray_sdk.core import patch_all

logger = logging.getLogger()
logger.setLevel(logging.INFO)
#patch_all()

#client = boto3.client('lambda')
#client.get_account_settings()

def lambda_handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES\r' + jsonpickle.encode(dict(**os.environ)))
    logger.info('## EVENT\r' + jsonpickle.encode(event))
    logger.info('## CONTEXT\r' + jsonpickle.encode(context))
    input = event["body"]
    total  = sum(input)
    return total
def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total