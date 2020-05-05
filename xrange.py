from builtins import range
import logging

logging.basicConfig(level=logging.DEBUG)

# Creating an object
logger = logging.getLogger()

for i in range(10):
    logger.debug(i)