from organs.mouth import universal_talk
from application.covid import msg_handle, Daily_Patient
from application.timer import timer
from application.clock import clock

class Action():
    def __init__(self, language, master):
        """First-order clasfficiation of actions : by Language"""
        self.language = language
        self.master = master

    def action_en(self, mode_number):
        """ Task Key Dictionary
            -1 : Unknown Task Error
            0 : Greeting
            1 : Live Daily COVID Patient
            2 : Brightness Control
            3 : Volume Control
            4 : Clock
            5 : Timer
        """
        if mode_number == -1:
            universal_talk('Sorry, I could not understand what you said. I will try harder next time.', self.language)
        elif mode_number == 0:
            universal_talk('Hello, how can I help you?', self.language)
        elif mode_number == 1:
            universal_talk('Sorry, requested service is not readied yet.', self.language)
        elif mode_number == 2:
            universal_talk('Sorry, requested service is not readied yet.',self.language)
    
    def action_kr(self, mode_number):
        """ Task Key Dictionary
            -1 : Unknown Task Error
            0 : Greeting
            1 : Live Daily COVID Patient
            2 : Brightness Control
            3 : Volume Control
            4 : Clock
            5 : Timer
        """
        if mode_number == -1:
            universal_talk('죄송해요, 무슨 말씀인지 잘 알아듣지 못했어요. 더욱 노력해서 다음 번엔 꼭 도와드리겠습니다.', self.language)
        elif mode_number == 0:
            universal_talk('안녕하세요, 무엇을 도와드릴까요?', self.language)
        elif mode_number == 1:
            return KorAction(self.language, self.master).covid()
        elif mode_number == 2:
            universal_talk('죄송합니다. 아직 서비스 준비중입니다.',self.language)

    def action_es(self, mode_number):
        """ Task Key Dictionary
            -1 : Unknown Task Error
            0 : Greeting
            1 : Live Daily COVID Patient
            2 : Brightness Control
            3 : Volume Control
            4 : Clock
            5 : Timer
        """
        if mode_number == -1:
            universal_talk('Lo siento, no entendí bien lo que estabas diciendo. Haremos todo lo posible para ayudarle en la próxima vez.', self.language)
        elif mode_number == 0:
            universal_talk('¿Hola, en que puedo ayudarle?', self.language)
        elif mode_number == 1:
            universal_talk('Lo siento, el servicio solicitado aún no está listo.', self.language)
        elif mode_number == 2:
            universal_talk('Lo siento, el servicio solicitado aún no está listo.',self.language)

    def universal_action(self, mode_number):
        """Language Key Dictionary
            0 : English
            1 : Korean
            2 : Spanish
        """
        if self.language == 0:
            return self.action_en(mode_number)
        elif self.language == 1:
            return self.action_kr(mode_number)
        elif self.language == 2:
            return self.action_es(mode_number)

class KorAction(Action):
    def __init__(self, language, master):
        """Second-order classification of actions: by Tasks"""
        super().__init__(language, master)
    
    def covid(self):
        print('Press ctrl+C to quit')
        try:
            what_said = self.master
            if msg_handle(what_said)[0]:
                if msg_handle(what_said)[1] == 0:
                    universal_talk('죄송해요, 오늘, 어제, 그저께에 대한 정보만 지원하고 있습니다. 더 자세한 정보는 보건복지부 홈페이지를 참조하여 주세요.')
                elif msg_handle(what_said)[1] == 1:
                    universal_talk('오늘 코로나19 확진자 수는 {}명입니다.'.format(Daily_Patient()[-1]))
                elif msg_handle(what_said)[1] == 2:
                    universal_talk('어제 코로나19 확진자 수는 {}명입니다.'.format(Daily_Patient()[-2]))
                elif msg_handle(what_said)[1] == 3:
                    universal_talk('그저께 코로나19 확진자 수는 {}명입니다.'.format(Daily_Patient()[-3]))
            else:
                universal_talk('죄송해요, 코로나 확진자 수 알림 기능만을 지원하고 있습니다. 다른 답변은 드릴 수가 없네요.')

        except KeyboardInterrupt:
            print('Goodbye.')
    
    
    def brightness():
        pass

    def volume():
        pass

    def clock():
        pass

    def timer():
        pass 

class EngAction(Action):
    def __init__(self, language, master):
        """Second-order classification of actions: by Tasks"""
        super().__init__(language, master)
    def covid(self):
        print('Press ctrl+C to quit')
        try:
            what_said = self.master
            if msg_handle(what_said)[0]:
                if msg_handle(what_said)[1] == 0:
                    universal_talk('Sorry, I only know about today, yesterday, and day before yesterday. Search internet for more detailed information.')
                elif msg_handle(what_said)[1] == 1:
                    universal_talk('Reported COVID patient number for today is {}.'.format(Daily_Patient()[-1]))
                elif msg_handle(what_said)[1] == 2:
                    universal_talk('Reported COVID patient number for yesterday is {}.'.format(Daily_Patient()[-2]))
                elif msg_handle(what_said)[1] == 3:
                    universal_talk('Reported COVID patient number for day before yesterday is {}.'.format(Daily_Patient()[-3]))
            else:
                universal_talk('Sorry, I only know about COVID patient number, please search internet for more information.')

        except KeyboardInterrupt:
            print('Goodbye.')

    def brightness():
        pass

    def volume():
        pass

    def clock():
        pass

    def timer():
        pass 