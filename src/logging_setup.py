import logging
import sys

# use whatever format you want here (timestamp is already recorded in CloudWatch)
LOG_FORMAT = '%(name)s - %(levelname)s - %(message)s'

def get_logger(name):
    logger = logging.getLogger(name)

    # https://forum.serverless.com/t/python-lambda-logging-duplication-workaround/1585
    logging.getLogger().handlers = []

    h = logging.StreamHandler(sys.stdout)

    h.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(h)
    logger.setLevel(logging.INFO)

    return logger
