import speech_recognition as sr
from datetime import date
import webbrowser
import openfileandFolder as fff

recognizer = sr.Recognizer()



def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say")
        audio = recognizer.listen(source)

    try:
        #data = recognizer.recognize_sphinx(audio)
        data = recognizer.recognize_google(audio)
        data = data.lower()
        print("You said: " + data)
        if data == "time":
            print(date.today())
        if data.__contains__("youtube"):
            webbrowser.open(
                'https://www.youtube.com/results?search_query='+data, new=0)
        if data.__contains__("google"):
            webbrowser.open("https://www.google.com/search?q="+data, new=0)
        if data.__contains__("open"):
            fff.OpenFIleandFolder(data)
            #webbrowser.open("https://www.google.com/search?q=" + data, new=0)

        return data
        # or: return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""


data = ""
while data != 'exit':
    data = listen()
