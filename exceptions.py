import logging

#Create an object
logger = logging.getLogger()

try:
    test = [1,2,3]
except Exception as e:
    logger.error("Exception error")
