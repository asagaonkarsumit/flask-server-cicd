import calendar
import time

from flask import request
from werkzeug.exceptions import Forbidden


def get_time(): return calendar.timegm(time.gmtime())
