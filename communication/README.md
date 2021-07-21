# Artificial Intelligence Speaker
### This is upgraded, and organized version of [AI_device_with_raspberryPi](https://github.com/skykongkong8/AI_device_with_RaspberryPi)
### Supports Windows 10, Linux OS
### Supports Korean, English, Español (T.B.A.)
#### Required External Libraries: PyAudio, threading, speech_recognition, gtts, playsound, urllib, requests, xml.etree.ElementTree


## How to use
1. download the library by using:  
```
git clone https://github.com/skykongkong8/Artificial_Intelligence.git
```
3. move to [communication](https://github.com/skykongkong8/Artificial_Intelligence/tree/main/communication) directory
4. Prepare your microphone and speaker. Connect them with your PC.
5. Run home.py (Please check your libraries before running) 
> for Python 3.8 or above, PyAudio cannot be downloaded. However, you can download it by using [pipwin](https://pypi.org/project/pipwin/) instead of pip3.    
> *PyAudio is essential for speech_recognition. However, if you substitute it with other STT algorithm, you may neglect this condition.* 
6. Choose your language setting, press keyboard 's' to start, and say hi:
* Baisc sample functions:
    * LIVE Daily COVID 19 patients of Republic of Korea
        * you should get your own service key from [here](https://www.data.go.kr/) to get your own authorization from the Korean government.
    * Clock
    * Timer

## Description
from """Actual Home""",   
* `language = language_inquiry(False)` ask for your language.
* `key = getKey()` get your keyboard input.
* `master = Listen().listen()[language]` analyze your voice and transform into string under your language.
* `mode_number = universal_mode_selection(master)` classify language and task that you asked for.
* `Action(language, master).universal_action(mode_number)` actually implement the classified task.
