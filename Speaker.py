import pyttsx3
import speech_recognition as sr
import datetime
#import face_recognition

engine = pyttsx3.init('sapi5')
engine. setProperty("rate", 165)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


'''def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")

    else:
        speak("Good Evening !")'''


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


'''def greets():
    ids = face_recognition.names[id]
    speak(ids)
    speak(", welcome to our Department Association Inauguration")


def greet():
    # robo name to be added
    speak("Welcomes to our Department Association Inauguration")

while True :
    speak("thanghavhel")'''

speak("Welcome you to vibes association Inaguration")
