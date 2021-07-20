def check_item(my_list, word):
    flag = False
    for token in my_list:
        if word in token:
            flag = True
            break
    return flag

def mode_selection(string):
    """Determine mode with strings"""
    my_list = list(string.lower().split(' '))

    if check_item(my_list, '안녕'):
        return 0
    elif check_item(my_list, '코로나') or check_item(my_list, '확진자'):
        return 1
    else:
        return -1