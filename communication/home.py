from action import Action
from organs.ears import Listen
from organs.mouth import universal_talk
from mode import universal_mode_selection, check_item, split_string
from constant_variables import*
import socket
import sys
import os
import gc
if os.name == 'nt':
    import msvcrt
else:
    import tty
    import termios



""" __Simple Rules__
    1. Ask for language
    2. Listen
    3. Action
"""

def language_inquiry(flag)->int:
    """Ask for user's language"""
    if not flag:
        universal_talk('Hello, please tell me what language are you speaking in.', ENGLISH)
    try:
        language_selection = Listen().listen()
        Eng = split_string(language_selection[ENGLISH])
        Kor = split_string(language_selection[KOREAN])
        Esp = split_string(language_selection[ESPANOL])
    except:
        universal_talk('Sorry, there were some error during the process. In this case, language is automatically selected to default. Current default language is Korean', ENGLISH)
        return DEFAULT_LANGUAGE
    if check_item(Eng, 'english') or check_item(Esp, 'ingles'):
        universal_talk('You chose English. Welcome. Please press s key to make me alert.', ENGLISH)
        return ENGLISH
    elif check_item(Kor, '한국어') or check_item(Kor, '한국') or check_item(Eng, 'korea') or check_item(Eng, 'korean') or check_item(Esp, 'coreano'):
        universal_talk('한국어를 선택하셨습니다. 만나서 반갑습니다. 에스 키를 누르면 활성화됩니다.', KOREAN)
        return KOREAN
    elif check_item(Esp, 'español') or check_item(Kor, '스페인어') or check_item(Eng, 'spanish'):
        universal_talk('Usted he seleccionado español. Bienvenido!', ESPANOL)
        return ESPANOL
    else:
        universal_talk('Sorry, I could not understand what you said. We only support English, Korean, and Spanish. Please tell me your language again.', ENGLISH)
        return language_inquiry(True)

def getKey():
    if os.name == 'nt':
        """for windows"""
        if sys.version_info[0] >= 3:
            return msvcrt.getch().decode()
        else:
            return msvcrt.getch()
    else:
        pass
        """For linux or mac"""
        tty.setraw(sys.stdin.filno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

def check_internet_connection()->bool:
    address = socket.gethostbyname(socket.gethostname())
    if address == "127.0.0.1":
        print("Internet Unavailable")
        return False
    else:
        print("Internet available to: " + address)
        return True

def language_selection(argument)->int:
    """language by argument, or manual input"""
    if len(argument) == 2:
        if argument[1] == '-korean':
            return KOREAN
        elif argument[1] == '-english':
            return ENGLISH
        elif argument[1] == '-spanish':
            return ESPANOL
        else:
            print('Invalid language argument error! Set language to default.')
            return DEFAULT_LANGUAGE
    elif len(argument) > 2:
        print('Multiple language input error! Set language to default.')
        return DEFAULT_LANGUAGE
    else:
        return language_inquiry(False)

"""Actual Home"""
if __name__ == "__main__":
    if check_internet_connection():
        try:
            language = language_selection(sys.argv)
            print("Press 's' key to make an order")
            while True:
                key = getKey()
                if key == 's':
                    master = Listen().listen()[language]
                    mode_number = universal_mode_selection(master, language)
                    Action(language, master).universal_action(mode_number)
                if key == 'e':
                    break
                else:
                    pass
        except KeyboardInterrupt:
            print('Keyboard interrupt abort')
        finally:
            """Add code here if you want to order any final tasks"""
            gc.collect(generation=2)
            try:
                os.remove('sample_1.mp3')
            except:
                pass
            print('Goodbye.')
            pass
    else:
        """Offline Condition: use 'vosk'"""
        print('Offline version: T.B.A.')
        pass