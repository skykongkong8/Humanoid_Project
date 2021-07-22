from constant_variables import*
from mode import check_item, split_string
import urllib.parse
import requests
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

# covid.py
# COVID 19 for today, yesterday, and day before yesterday in Republic Of Korea
# 주석 처리된 부분은 추후 오류점검에 도움이 되므로, 구태여 지우지 말 것

def universal_msg_handle(string, language):
    if language == ENGLISH:
        return msg_handle_ENG(string)
    elif language == KOREAN:
        return msg_handle_KOR(string)
    elif language == ESPANOL:
        return msg_handle_ESP(string)

def msg_handle_KOR(string):
    """Sort for data, double check with isit_covid"""
    isit_covid = False
    day = 0 #(0: default, 1: 오늘, 2:어제, 3:그저께)
    my_list = split_string(string)
    print(string)
    #0 기본 언어 : 코로나, 확진자, 몇, 명
    if check_item(my_list, '코로나'):
        if check_item(my_list, '명') or check_item(my_list, '확진자') or check_item(my_list, '수'):
            isit_covid = True
    #1 오늘
    if check_item(my_list, '오늘'):
        day = 1
    #2 어제
    elif check_item(my_list, '어제'):
        day = 2
    #3 그저께
    elif check_item(my_list, '그저께') or check_item(my_list, '어저께'):
        day = 3
    else:
        print('무슨 말인지 알아들을 수 없습니다!')
    return [isit_covid, day]

def msg_handle_ENG(string):
    """Sort for data, double check with isit_covid"""
    isit_covid = False
    day = 0 #(0: default, 1: 오늘, 2:어제, 3:그저께)
    my_list = split_string(string)
    print(string)
    #0 기본 언어 : 코로나, 확진자, 몇, 명
    if check_item(my_list, 'corona') or check_item(my_list, 'covid'):
        isit_covid = True
    #1 오늘
    if check_item(my_list, 'today'):
        day = 1
    #2 어제
    elif check_item(my_list, 'yesterday'):
        day = 2
    #3 그저께
    elif check_item(my_list, 'before') and check_item(my_list, 'yesterday'):
        day = 3
    else:
        print('Invalid date input!')
    return [isit_covid, day]

def msg_handle_ESP(string):
    pass


def today_Patient():
    today = datetime.now()
    past = datetime.now()-timedelta(days=3)

    servicekey = "A%2FE1M5JtX4S60k6oQ5Es6fRclxobTZqXFE3YjgWiWcqH4O6888F9UclbkgxgwEEDTfhOzL8%2BFRgmmVX0hRPAxg%3D%3D"
    decoded_key = urllib.parse.unquote(servicekey)
    #print(decoded_key)

    service_url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson"
    #딕셔너리 저장할 때 사이트에 있는 파라미터 '그대로' 적을 것
    params = {
        "ServiceKey" : decoded_key,
        "pageNo" : "1",
        "numOfRows" : "10",
        "startCreateDt" : "{}{}{}".format(str(past.year), str(past.month).zfill(2), str(past.day).zfill(2)),
        "endCreateDt" : "{}{}{}".format(str(today.year), str(today.month).zfill(2), str(today.day).zfill(2))
    }
    resp = requests.get(service_url, params = params)
    # print(resp.content)
    resp = requests.get(service_url, params = params)
    root = ET.fromstring(resp.content)

    for element in root:
        #print(element.tag, element.attrib)
        if element.tag == 'header':
            header = list(element)
        elif element.tag == 'body':
            body = list(element)

    items = body[0]
    decideCnt = []
    # stateDt = []

    for item in items:
        for item_tag in item:
            #print(item_tag.tag)
            if item_tag.tag == 'decideCnt':
                decideCnt.append(int(item_tag.text))
            # if item_tag.tag == 'stateDt':
            #     stateDt.append(item_tag.text)
    decideCnt.reverse()
    daily_patient = []
    for i in range(1,len(decideCnt)):
        daily_patient.append(decideCnt[i]-decideCnt[i-1])
    return daily_patient

def past_Patient():
    yesterday = datetime.now()-timedelta(days=1)
    past = datetime.now()-timedelta(days=4)

    servicekey = "A%2FE1M5JtX4S60k6oQ5Es6fRclxobTZqXFE3YjgWiWcqH4O6888F9UclbkgxgwEEDTfhOzL8%2BFRgmmVX0hRPAxg%3D%3D"
    decoded_key = urllib.parse.unquote(servicekey)
    #print(decoded_key)

    service_url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson"
    #딕셔너리 저장할 때 사이트에 있는 파라미터 '그대로' 적을 것
    params = {
        "ServiceKey" : decoded_key,
        "pageNo" : "1",
        "numOfRows" : "10",
        "startCreateDt" : "{}{}{}".format(str(past.year), str(past.month).zfill(2), str(past.day).zfill(2)),# 날짜를 잘 조절할 것! --오늘이 3일이하면 :(
        "endCreateDt" : "{}{}{}".format(str(yesterday.year), str(yesterday.month).zfill(2), str(yesterday.day).zfill(2)) #날짜를 if문으로 조절하기
    }
    resp = requests.get(service_url, params = params)
    # print(resp.content)
    resp = requests.get(service_url, params = params)
    root = ET.fromstring(resp.content)

    for element in root:
        #print(element.tag, element.attrib)
        if element.tag == 'header':
            header = list(element)
        elif element.tag == 'body':
            body = list(element)

    items = body[0]
    decideCnt = []
    # stateDt = []

    for item in items:
        for item_tag in item:
            #print(item_tag.tag)
            if item_tag.tag == 'decideCnt':
                decideCnt.append(int(item_tag.text))
            # if item_tag.tag == 'stateDt':
            #     stateDt.append(item_tag.text)
    decideCnt.reverse()
    daily_patient = []
    for i in range(1,len(decideCnt)):
        daily_patient.append(decideCnt[i]-decideCnt[i-1])
    return daily_patient

def Daily_Patient():
    try:
        """오늘 확진자가 발표되었음"""
        return today_Patient()
    except:
        """오늘 확진자가 아직 발표되지 않았음"""
        return past_Patient()

# print(Daily_Patient())