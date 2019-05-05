import speech_recognition as sr
from datetime import date
recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say")
        audio = recognizer.listen(source)

    try:
        #data = recognizer.recognize_sphinx(audio)
        data = recognizer.recognize_google(audio)
        print("You said: " + data)
        if data == "time":
            print(date.today())
        return data
        # or: return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""


data = listen()
