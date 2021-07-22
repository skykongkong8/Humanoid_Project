################################################################################################################
# mode.py
# Originally, mode selection should be done by NLP, analyzing the given sentence by syntax. 
# However in this case, since the system is simple enough, we just use classification function like following...



from home import ENGLISH, ESPANOL, KOREAN

"""ACTION TASKS"""
UNKNOWN_ERROR = -1
GREETING = 0
COVID = 1
BRIGHTNESS = 2
VOLUME = 3
CLOCK = 4
TIMER = 5
JOKE = 6

HOUSE_PARTY_PROTOCOL = 999

def check_item(my_list, word):
    flag = False
    for token in my_list:
        if word in token:
            flag = True
            break
    return flag

def split_string(string):
    """split and lower the string"""
    return string.lower().split(' ')

def mode_selection_eng(string):    
    my_list = split_string(string)

    if check_item(my_list, 'hello') or check_item(my_list, 'hi') or (check_item(my_list, 'meet') and check_item(my_list, 'nice') and check_item(my_list, 'you')):
        return GREETING
    elif check_item(my_list, 'corona') or check_item(my_list, 'covid'):
        return COVID
    elif check_item(my_list, 'brightness') or (check_item(my_list, 'light') and (check_item(my_list, 'down') or check_item(my_list, 'up'))):
        return BRIGHTNESS
    elif check_item(my_list, 'volume'):
        return VOLUME
    elif (check_item(my_list, 'time') and check_item(my_list, 'what')) or check_item(my_list, 'clock'):
        return CLOCK
    elif check_item(my_list, 'timer'):
        return TIMER
    elif check_item(my_list, 'joke') or check_item(my_list, 'jokes') or (check_item(my_list, 'funny') and (check_item(my_list, 'story') or check_item(my_list, 'stories'))):
        return JOKE
    elif check_item(my_list, 'protocol') and (check_item(my_list, 'house') or check_item(my_list, 'party'), check_item(my_list, 'final')):
        return HOUSE_PARTY_PROTOCOL

    else:
        return UNKNOWN_ERROR

def mode_selection_kor(string):
    my_list = split_string(string)

    if check_item(my_list, '안녕'):
        return GREETING
    elif check_item(my_list, '코로나') or check_item(my_list, '확진자'):
        return COVID
    elif check_item(my_list, '밝기') or (check_item(my_list, '화면이') and (check_item(my_list, '밝아') or check_item(my_list, '어두워'))):
        return BRIGHTNESS
    elif check_item(my_list, '볼륨') or check_item(my_list, '소리'):
        return VOLUME
    elif check_item(my_list, '시간') or (check_item(my_list, '몇') and check_item(my_list, '시')) or check_item(my_list, '시계'):
        return CLOCK
    elif check_item(my_list, '타이머') or (check_item(my_list, '후에') and check_item(my_list, '알려줘')):
        return TIMER
    elif check_item(my_list, '농담') or ((check_item(my_list, '재미있는') or check_item(my_list, '재밌는')) and (check_item(my_list, '이야기') or check_item(my_list, '얘기'))):
        return JOKE
    elif (check_item(my_list, '전부') or check_item(my_list, '다')) and check_item(my_list, '보여줘'):
        return HOUSE_PARTY_PROTOCOL
    else:
        return UNKNOWN_ERROR

def mode_selection_esp(string):
    """Determine mode with EXTREMELY primitive NLP"""
    my_list = split_string(string)

    if check_item(my_list, 'hola'):
        return GREETING
    elif check_item(my_list, 'corona') or check_item(my_list, 'virus') or check_item(my_list, 'covid'):
        return COVID
    else:
        return UNKNOWN_ERROR

def universal_mode_selection(string, language):
    """First order mode selection: by Language

        Language Key Dictionary
        0 : English
        1 : Korean
        2 : Spanish

    """
    if language == ENGLISH:
        return mode_selection_eng(string)
    elif language == KOREAN:
        return mode_selection_kor(string)
    elif language == ESPANOL:
        return mode_selection_esp(string)