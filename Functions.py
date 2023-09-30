import pyttsx3

engine = pyttsx3.init('SAPI5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()