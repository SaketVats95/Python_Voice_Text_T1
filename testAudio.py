import speech_recognition as sr
from datetime import date
import webbrowser
import pyttsx3

import testYoutube

def speak(audioString):
    speakEng=pyttsx3.init()
    speakEng.say(audioString)
    speakEng.runAndWait()

def showOptions(obj):
    count=0
    for i in range(len(obj)):
        checkContinue='y'
        if((i+1)%5==0):
            checkContinue=input("Enter [y] in you want to get more result: other wise [n]")
        if(checkContinue=='n'):
            break
        #print(type(i))
        speachString="Enter "+str(i)+" for : "+obj[i][0]
        print(speachString)
        speak(speachString)
    option=int(input("Enter the option"))
    openLink(obj[option-1][1])
        #option=listen()


def openLink(link):
    webbrowser.open(link)

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
        speak(data)

        if data == "time":
            print(date.today())
        if data.__contains__("open youtube"):
            search_query = data[(data.index("search for")+11):]
            # webbrowser.open(
            #    'https://www.youtube.com/results?search_query='+data, new=0)
            speak("Opening Youtube")
            elementsList=testYoutube.OpenYotube(search_query)
            showOptions(elementsList)
        if data.__contains__("google"):
            webbrowser.open("https://www.google.com/search?q="+data, new=0)
        # if data.__contains__("open"):
         #   fff.OpenFIleandFolder(data)
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
