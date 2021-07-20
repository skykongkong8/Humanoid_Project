"""MOUTH MODULE FOR gTTS"""

from pygame import mixer
from gtts import gTTS

def talk_en(words):
        tts = gTTS(text = words, lang = 'en')
        tts.save('sample_1.mp3')
        mixer.init()
        mixer.load('sample_1.mp3')
        mixer.play()

def talk_kr(words):
        tts = gTTS(text = words, lang = 'ko')
        tts.save('sample_1.mp3')
        mixer.init()
        mixer.load('sample_1.mp3')
        mixer.play()

def talk_es(words):
        tts = gTTS(text = words, lang = 'es')
        tts.save('sample_1.mp3')
        mixer.init()
        mixer.load('sample_1.mp3')
        mixer.play()