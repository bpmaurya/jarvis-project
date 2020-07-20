import audioop
import os
from urllib.parse import quote_plus
import pyttsx3
import datetime
import wikipedia
import webbrowser
import sys
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak(" Hi! i am jarvis! speed one terabite version 2.0. Sir! Please tell me how i help you")


def takeCommand():
    # it take your voice command
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("user said: \n", query)
    except Exception as e:
        # print(e)
        print("say again please")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        #logics
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentence=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Tejprakash\\Music\\A.K. MUSIC\\My Music\\Jhankar Beats'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'i love you' in query:
            speak("but i do not love you")    

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir , the time is {strtime}")
        
        elif 'quit' in query:
            sys.exit()