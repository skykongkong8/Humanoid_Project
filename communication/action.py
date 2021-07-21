from organs.mouth import universal_talk
from application.covid import msg_handle, Daily_Patient
from application.timer import timertime_KOR, timertime_ENG
from application.clock import clock
from application.brightness import brightness
from application.volume import volume
from time import sleep
# import threading

"""ACTION TASKS"""
UNKNOWN_ERROR = -1
GREETING = 0
COVID = 1
BRIGHTNESS = 2
VOLUME = 3
CLOCK = 4
TIMER = 5

class Action():
    def __init__(self, language, master):
        """First-order clasfficiation of actions : by Language"""
        self.language = language
        self.master = master
 
    def action_en(self, mode_number):
        if mode_number == UNKNOWN_ERROR:
            universal_talk('Sorry, I could not understand what you said. I will try harder next time.', self.language)
        elif mode_number == GREETING:
            universal_talk('Hello, how can I help you?', self.language)
        else:
            eng_action = EngAction(self.language, self.master)
            if mode_number == COVID:
                return eng_action.covid_ENG()
            elif mode_number == BRIGHTNESS:
                return eng_action.brightness_ENG()
            elif mode_number == VOLUME:
                return eng_action.volume_ENG()
            elif mode_number == CLOCK:
                return eng_action.clock_ENG()
            elif mode_number == TIMER:
                return eng_action.timer_ENG()
            else:
                universal_talk('Sorry, requested service is not readied yet.',self.language)
        
    def action_kr(self, mode_number):
        if mode_number == UNKNOWN_ERROR:
            universal_talk('죄송해요, 무슨 말씀인지 잘 알아듣지 못했어요. 더욱 노력해서 다음 번엔 꼭 도와드리겠습니다.', self.language)
        elif mode_number == GREETING:
            universal_talk('안녕하세요, 무엇을 도와드릴까요?', self.language)
        else:
            kor_action = KorAction(self.language, self.master)
            if mode_number == COVID:
                return kor_action.covid_KOR()
            elif mode_number == BRIGHTNESS:
                return kor_action.brightness_KOR()
            elif mode_number == VOLUME:
                return kor_action.volume_KOR()
            elif mode_number == CLOCK:
                return kor_action.clock_KOR()
            elif mode_number == TIMER:
                return kor_action.timer_KOR()
            else:
                return universal_talk('죄송해요, 요청하신 서비스는 아직 서비스 준비중입니다.', self.language)

    def action_es(self, mode_number):
        if mode_number == UNKNOWN_ERROR:
            universal_talk('Lo siento, no entendí bien lo que estabas diciendo. Haremos todo lo posible para ayudarle en la próxima vez.', self.language)
        elif mode_number == GREETING:
            universal_talk('¿Hola, en que puedo ayudarle?', self.language)
        elif mode_number == COVID:
            universal_talk('Lo siento, el servicio solicitado aún no está listo.', self.language)
        elif mode_number == BRIGHTNESS:
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



class EngAction(Action):
    def __init__(self, language, master):
        """Second-order classification of actions: by Tasks"""
        super().__init__(language, master)

    def covid_ENG(self):
        print('Press ctrl+C to quit')
        try:
            what_said = self.master
            if msg_handle(what_said)[0]:
                if msg_handle(what_said)[1] == 0:
                    universal_talk('Sorry, I only know about today, yesterday, and day before yesterday. Search internet for more detailed information.',self.language)
                elif msg_handle(what_said)[1] == 1:
                    universal_talk('Reported COVID patient number for today is {}.'.format(Daily_Patient()[-1]),self.language)
                elif msg_handle(what_said)[1] == 2:
                    universal_talk('Reported COVID patient number for yesterday is {}.'.format(Daily_Patient()[-2]),self.language)
                elif msg_handle(what_said)[1] == 3:
                    universal_talk('Reported COVID patient number for day before yesterday is {}.'.format(Daily_Patient()[-3]),self.language)
            else:
                universal_talk('Sorry, I only know about COVID patient number, please search internet for more information.',self.language)

        except KeyboardInterrupt:
            print('Goodbye.')

    def brightness_ENG(self):
        """Connect brightness regulating application function here"""
        # HERE
        # Tip: you can use self.master for determing brightness UP or DOWN
        brightness()
        universal_talk('Regulating the display brightness', self.language)
        pass

    def volume_ENG(self):
        """Connect volume regulating application function here"""
        # HERE
        # Tip: you can use self.master for determing volume UP or DOWN
        volume()
        universal_talk('Regulating the system volume', self.language)
        pass

    def clock_ENG(self):
        time_list = clock()
        month_dict = {
            1 : 'January',
            2 : 'Feburary',
            3 : 'March',
            4 : 'April',
            5 : 'May',
            6 : 'June',
            7 : 'July',
            8 : 'August',
            9 : 'September',
            10 : 'October',
            11 : 'November',
            12 : 'December'
        }
        day_dict = {
            1 : 'first',
            2 : 'second',
            3 : 'third',
            4 : 'fourth',
            5 : 'fifth',
            6 : 'sixth',
            7 : 'seventh'
        }
        if time_list[1] > 7:
            universal_talk('Today is {0} {1} {2} {3}'.format(month_dict[time_list[0]], time_list[1], time_list[2], time_list[3]), self.language)
        else:
            universal_talk('Today is {0} {1} {2} {3}'.format(month_dict[time_list[0]], day_dict[time_list[1]], time_list[2], time_list[3]), self.language)


    def _notification(self):
        for _ in range(3):
            universal_talk('Timer is over!', self.language)
    def timer_ENG(self):
        timer_seconds = timertime_ENG(self.master)
        try:
            if (timer_seconds >=0):
                universal_talk('your timer has just set. I will let you know for three times when it is done!', self.language)
                sleep(int(timer_seconds))
                self._notification()
                # threading.Timer(timer_seconds, self._notification()).start()
            else:
                universal_talk('Sorry, I could not understand your timer order. Please try it again.', self.language)
        except:
            universal_talk('Sorry, I could not understand your timer order. Please try it again.', self.language)



class KorAction(Action):
    def __init__(self, language, master):
        """Second-order classification of actions: by Tasks"""
        super().__init__(language, master)
    
    def covid_KOR(self):
        print('Press ctrl+C to quit')
        try:
            what_said = self.master
            if msg_handle(what_said)[0]:
                if msg_handle(what_said)[1] == 0:
                    universal_talk('죄송해요, 오늘, 어제, 그저께에 대한 정보만 지원하고 있습니다. 더 자세한 정보는 보건복지부 홈페이지를 참조하여 주세요.', self.language)
                elif msg_handle(what_said)[1] == 1:
                    universal_talk('오늘 코로나19 확진자 수는 {}명입니다.'.format(Daily_Patient()[-1]), self.language)
                elif msg_handle(what_said)[1] == 2:
                    universal_talk('어제 코로나19 확진자 수는 {}명입니다.'.format(Daily_Patient()[-2]), self.language)
                elif msg_handle(what_said)[1] == 3:
                    universal_talk('그저께 코로나19 확진자 수는 {}명입니다.'.format(Daily_Patient()[-3]), self.language)
            else:
                universal_talk('죄송해요, 코로나 확진자 수 알림 기능만을 지원하고 있습니다. 다른 답변은 드릴 수가 없네요.', self.language)

        except KeyboardInterrupt:
            print('Goodbye.')
    
    
    def brightness_KOR(self):
        """Connect brightness regulating application function here"""
        # Here
        # Tip: you can use self.master for determing brightness UP or DOWN
        brightness()
        universal_talk('화면 밝기를 조정합니다.', self.language)

    def volume_KOR(self):
        """Connect volume regulating application function here"""
        # Here
        # Tip: you can use self.master for determing volume UP or DOWN
        volume()
        universal_talk('시스템 볼륨을 조정합니다.', self.language)

    def clock_KOR(self):
        time_list = clock()
        universal_talk('오늘은 {0}월 {1}일 {2}시 {3}분 입니다.'.format(time_list[0], time_list[1], time_list[2], time_list[3]), self.language)
    
    def _notification(self):
        for i in range(3):
            universal_talk('타이머가 끝났습니다!', self.language)

    def timer_KOR(self):
        timer_seconds = timertime_KOR(self.master)
        try:
            if (timer_seconds >0):
                universal_talk('타이머가 설정되었습니다. 끝나면 세 번 알려드려요!'.format(timer_seconds), self.language)
                sleep(int(timer_seconds))
                self._notification()
                # threading.Timer(timer_seconds, self._notification()).start()
            else:
                universal_talk('잘못된 타이머 시간을 말씀하셨습니다. 타이머를 종료합니다.', self.language)
        except:
            universal_talk('죄송해요, 타이머 설정 시간을 잘 이해하지 못했습니다. 타이머를 종료합니다.', self.language)



class EspAction(Action):
    pass