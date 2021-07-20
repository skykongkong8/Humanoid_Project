from ears import listen
from mouth import talk_kr, talk_en, talk_es
from mode import mode_selection, check_item
import RPi.GPIO as g #RUNS AT RASPBERRYPI

"""basic format"""
# AudioData = listen()
# talk_kr(AudioData[1])

global language
language = 1

def universal_talk(string, language):
    """Defined under language selection
        1 : KOREAN
        0 : ENGLISH
        2 : SPANISH
    """
    if language == 1:
        return talk_kr(string)
    elif language == 0:
        return talk_en(string)
    elif language == 2:
        return talk_es(string)

def action_kr(mode_number, master):
    if mode_number == -1:
        universal_talk('죄송해요, 무슨 말씀인지 잘 알아듣지 못했어요. 더욱 노력해서 다음 번엔 꼭 도와드리겠습니다.', language)
    elif mode_number == 1:
        universal_talk('안녕하세요, 무엇을 도와드릴까요?', language)
    elif mode_number == 2:
        universal_talk('죄송합니다. 아직 서비스 준비중입니다.', language)

def action_en(mode_number, master):
    if mode_number == -1:
        universal_talk('Sorry, I could not understand what you said. I will try harder next time.', language)
    elif mode_number == 1:
        universal_talk('Hello, how can I help you?', language)
    elif mode_number == 2:
        universal_talk('Sorry, requested service is not readied yet.', language)

def acton_es(mode_number, master):
    if mode_number == -1:
        universal_talk('Lo siento, no entendí bien lo que estabas diciendo. Haremos todo lo posible para ayudarle en la próxima vez.', language)
    elif mode_number == 1:
        universal_talk('¿Hola, en que puedo ayudarle?', language)
    elif mode_number == 2:
        universal_talk('Lo siento, el servicio solicitado aún no está listo.', language)

def language_inquiry(flag):
    if flag:
        universal_talk('Hello, please select your language', 2)
    language_selection = listen()
    if check_item(language_selection[0], 'english') or check_item(language_selection[0], 'English'):
        universal_talk('You have chosen English. Welcome.', 0)
        return 0
    elif check_item(language_selection[1], '한국어') or check_item(language_selection[1], '한국') or check_item(language_selection[0], 'korea') or check_item(language_selection[0], 'korean'):
        universal_talk('한국어를 선택하셨습니다. 만나서 반갑습니다.', 1)
        return 1
    elif check_item(language_selection[2], 'español') or check_item(language_selection[2], 'Español') or check_item(language_selection[1], '스페인어'):
        universal_talk('Usted he seleccionado español. Bienvenido!', 2)
        return 2
    else:
        universal_talk('Sorry, I could not understand what you said. Please tell your language again', 0)
        language(True)


"""실행 코드"""
if __name__ == "__main__":
    g.setmode(g.BCM)
    touch_sensor = 26
    g.setup(touch_sensor, g.IN)

    language = language_inquiry(False)

    try:
        while True:
            value = g.input(touch_sensor)
            if value == True:
                master = listen()[language]
                mode_number = mode_selection(master)
                action_kr(mode_number, master)
            else:
                pass
    except KeyboardInterrupt:
        print('Goodbye.')
    finally:
        g.cleanup()