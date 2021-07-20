from EARS import listen
from MOUTH import talk_kr, talk_en, talk_es
from MODE import mode_selection
import RPi.GPIO as g #RUNS AT RASPBERRYPI

#AudioData = listen()
#talk_kr(AudioData[1])

global language
language = 1

def universal_talk(string, language):
    """Defined under language selection
        1 : KOREAN
        2 : ENGLISH
        3 : SPANISH
    """
    if language == 1:
        return talk_kr(string)
    elif language == 0:
        return talk_en(string)
    elif language == 2:
        return talk_es(string)

def check_item(my_list, word):
    flag = False
    for token in my_list:
        if word in token:
            flag = True
            break
    return flag

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


"""실행 코드"""
g.setmode(g.BCM)
touch_sensor = 26
g.setup(touch_sensor, g.IN)

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