from builtins import object
import logging

#creating an object
logger = logging.getLogger()

class AllOrNothing(object):
    def __init__(self, l):
        self.l = l
    def __bool__(self):
        return all(self.l)

container = AllOrNothing([0, 100, 200])
logger.warning(container)
assert bool (container)
