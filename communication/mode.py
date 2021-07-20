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
    """Determine mode with EXTREMELY primitive NLP"""
    my_list = split_string(string)

    if check_item(my_list, 'hello'):
        return 0
    elif check_item(my_list, 'corona') or check_item(my_list, 'covid'):
        return 1
    elif check_item(my_list, 'brightness') or (check_item(my_list, 'light') and (check_item(my_list, 'down') or check_item(my_list, 'up'))):
        return 2
    else:
        return -1

def mode_selection_kor(string):
    """Determine mode with EXTREMELY primitive NLP"""
    my_list = split_string(string)

    if check_item(my_list, '안녕'):
        return 0
    elif check_item(my_list, '코로나') or check_item(my_list, '확진자'):
        return 1
    elif check_item(my_list, '밝기') or (check_item(my_list, '화면이') and (check_item(my_list, '밝아') or check_item(my_list, '어두워'))):
        return 2
    else:
        return -1

def mode_selection_esp(string):
    """Determine mode with EXTREMELY primitive NLP"""
    my_list = split_string(string)

    if check_item(my_list, 'hola'):
        return 0
    elif check_item(my_list, 'corona') or check_item(my_list, 'virus') or check_item(my_list, 'covid'):
        return 1
    else:
        return -1

def universal_mode_selection(string, language):
    if language == 0:
        return mode_selection_eng(string)
    elif language == 1:
        return mode_selection_kor(string)
    elif language == 2:
        return mode_selection_esp(string)