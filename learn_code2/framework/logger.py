import logging
import os.path
import time

class Log(object):

    def __init__(self,log):
        self.log=logging.getLogger(log)
        self.log.setlevel(logging.DEBUG)

        rq=time.strftime('%Y%m%d:%H%M%S'),time.localtime()











