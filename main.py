import pyttsx3    # pip install pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good morning")

    elif hour>=12 and hour<=18:
        speak("Good afternoon")

    else:
        speak("good night")

    speak("i am your assistant how can i help you")

if __name__ == '__main__':
    greetings()
