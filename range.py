import logging
from future.utils import lrange
from past.builtins import range

# Creating an object
logger = logging.getLogger()

mylist = [lrange(5)]
logger.critical(mylist)
assert mylist == [0,1,2,3,4]
