from action import Action
from organs.ears import Listen
from organs.mouth import universal_talk
from mode import universal_mode_selection, check_item, split_string
from dataclasses import dataclass
import os
import sys
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

"""basic format"""
# AudioData = listen()
# talk_kr(AudioData[1])

global language
language = 1

def language_inquiry(flag):
    """Ask for user's language"""
    if not flag:
        universal_talk('Hello, please tell me what language are you speaking in.', 0)
    try:
        language_selection = Listen().listen()
        ENG = split_string(language_selection[0])
        KOR = split_string(language_selection[1])
        ESP = split_string(language_selection[2])
    except:
        universal_talk('Sorry, there were some error during the process. In this case, language is automatically selected to Korean', 0)
        return 1
    if check_item(ENG, 'english') or check_item(ESP, 'ingles'):
        universal_talk('You chose English. Welcome.', 0)
        return 0
    elif check_item(KOR, '한국어') or check_item(KOR, '한국') or check_item(ENG, 'korea') or check_item(ENG, 'korean') or check_item(ESP, 'coreano'):
        universal_talk('한국어를 선택하셨습니다. 만나서 반갑습니다.', 1)
        return 1
    elif check_item(ESP, 'español') or check_item(KOR, '스페인어') or check_item(ENG, 'spanish'):
        universal_talk('Usted he seleccionado español. Bienvenido!', 2)
        return 2
    else:
        universal_talk('Sorry, I could not understand what you said. Please tell your language again.', 0)
        language_inquiry(True)

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


"""실행 코드"""
if __name__ == "__main__":
    language = language_inquiry(False)
    print("Press 's' key to start")
    try:
        while True:
            key = getKey()
            if key == 's':
                master = Listen().listen()[language]
                mode_number = universal_mode_selection(master)
                Action(language, master).universal_action(mode_number)
            else:
                pass
    except KeyboardInterrupt:
        print('Goodbye.')
    finally:
        """무언가 최종 작업을 하고 싶다면 여기에 코드를 추가하세요."""
        gc.collect(generation=2)
        pass