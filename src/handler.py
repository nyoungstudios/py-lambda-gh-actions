import requests
from src.logging_setup import get_logger

def lambda_handler(event, context):
    logger = get_logger('test')

    logger.info('Starting lambda function...')

    output = requests.get('https://api.github.com')

    logger.info(output)

    logger.info('end of lambda function')

    return True
