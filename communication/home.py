from action import Action
from organs.ears import Listen
from organs.mouth import universal_talk
from mode import universal_mode_selection, check_item, split_string
import os
import sys
import gc
if os.name == 'nt':
    import msvcrt
else:
    import tty
    import termios

#LANGUAGE CLASSFICATION
DEFAULT_LANGUAGE = 1
ENGLISH = 0
KOREAN = 1
ESPANOL = 2

""" __Simple Rules__
    1. Ask for language
    2. Listen
    3. Action
"""

"""basic format"""
# AudioData = listen()
# talk_kr(AudioData[1])

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
        universal_talk('한국어를 선택하셨습니다. 만나서 반갑습니다. 에스 키를 눌르면 활성화됩니다.', KOREAN)
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


"""Actual Home"""
if __name__ == "__main__":
    if len(sys.argv) != 1:
        if sys.argv[1] == '-korean':
            language = KOREAN
        elif sys.argv[1] == '-english':
            language = ENGLISH
        elif sys.argv[1] == '-spanish':
            language = ESPANOL
        else:
            print('Invalid language argument error! Set language to default.')
            language = DEFAULT_LANGUAGE
    else:
        language = language_inquiry(False)
    print("Press 's' key to make an order")
    try:
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