import time
from datetime import datetime
from logger import debug, error


def getLocalTimeZoneOffset():
    try:
        timeZoneOffset = -time.timezone
        debug("timeZoneOffset", timeZoneOffset)
        return timeZoneOffset
    except Exception as e:
        error("getTimeZoneOffsetException", e)
        return None


def getLocalTimeCurrent():
    try:
        timeCurrent = time.mktime(datetime.today().timetuple())
        debug("timeCurrent", timeCurrent)
        return timeCurrent
    except Exception as e:
        error("getTimeCurrentException", e)
        return None
