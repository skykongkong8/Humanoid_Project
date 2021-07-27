from constant_variables import*
import re

def universal_timertime(master, language):
    if language == ENGLISH:
        return timertime_ENG(master)
    elif language == KOREAN:
        return timertime_KOR(master)
    elif language == ESPANOL:
        return timertime_ESP(master)

def timertime_KOR(master)->float:
    """extract time property from master order"""
    p = re.compile('(\d)+')
    q = re.compile('분|초|시간|중지|정지|그만')
    m = p.search(master)
    n = q.search(master)
    try:
        t = float(m.group())
        s = n.group()
        if s == '초':
            pass
        elif s == '분':
            t*=60
        elif s == '시간':
            t*=3600
        elif s == '중지' or '정지' or '그만':
            t = -2
    except:
        t = -1
    return t     

def timertime_ENG(master)->float:
    """extract time property from master order"""
    p = re.compile('(\d)+')
    q = re.compile('minutes|seconds|hours|stop|done|minute|hour')
    m = p.search(master)
    n = q.search(master)
    try:
        t = float(m.group())
        s = n.group()
        if s == 'seconds':
            pass
        elif s == 'minute' or s == 'minutes':
            t*=60
        elif s == 'hours' or s == 'hour':
            t*=3600
        elif s == 'stop' or 'done':
            t = -2
    except:
        t = -1
    return t     

def timertime_ESP(master):
    pass