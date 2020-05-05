from past.builtins import basestring
from past.builtins import unicode
import logging

a = u'abc'
b = b'def'
assert (isinstance(a, basestring) and isinstance(b, basestring))
if(isinstance(a,basestring)):
    logging.error(isinstance(a, basestring))
else:
    logging.error(isinstance(b, basestring))