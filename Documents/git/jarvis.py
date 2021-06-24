from math import perm
from urllib.parse import quote_from_bytes
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import shutil
import pyjokes
import smtplib
import json
# from ecapture import ecapture as ec

from wikipedia.wikipedia import random

engine = pyttsx3.init('sapi5')  # to receive voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir! Whats up?")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!! Whats up?")
    else:
        speak("Good evening Sir!! Whats up?")
    
    speak("I Am Your Personal assistant Disha")
    


def uname():
    speak("What Should i call you?")
    uname = takeCommand()
    speak(f"hello {uname} Please Tell me what I can do for you ?")
    

def takeCommand():

    #it takes mic input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        # r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
        
    except Exception as e:
        # print(e)

        speak("Sorry I was not able to understand...")
        return"None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(input(), input())
    server.sendmail(input(), to, content)
    server.close

if __name__ == "__main__":
    # write all functions here 
    wishMe()
    uname()
    while True:
    # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching in Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'open amazon' in query:
            speak("opening amazon")
            webbrowser.open("amazon.in")

        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.open("facebook.com")    
        
        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")

        elif 'open gmail' in query:
            speak("opening gmail")
            webbrowser.open("gmail.com")    
        
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")

        elif 'play music' in query or 'play song' in query:
            music_dir = 'E:\\video edit\\music for videos' 
            songs = os.listdir(music_dir)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"The Time is: {strTime}")

        elif 'open browser' in query or 'open edge' in query or 'open microsoft edge' in query:
            speak('opening Browser')
            edgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            
            os.startfile(edgePath)

        elif 'tell me a joke' in query:
            speak("Here you go")
            speak(pyjokes.get_joke())
        
        
        elif 'send an email' in query or 'send mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my freind, I am not able to send the email")    
    
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")     

        elif 'fine' in query or 'good' in query or 'great' in query or 'awesome' in query:
            speak("It's good to know that your fine")

        elif 'what is your name' in query or 'whats your name' in query:
            speak("My Name is Disha")
        
        
        elif 'who made you' in query:
            speak("I was made by Prashant wadhwa")  

        

        elif 'How old are you' in query:
            speak("I was created in 2021")

        elif 'where do you live' in query or 'where you live' in query:
            speak("I live in your heart")

        elif 'when is your birthday' in query:
            speak("I try to live every day like it’s my birthday")

        elif 'f*** you' in query:
            speak("i am sorry you felt so, but please dont talk to me like that")
        
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)

        elif "why you came to world" in query:
            speak("Thanks to Prashant. by the way It's a secret")


        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("You asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        # elif 'camera' in query or 'open camera' in query or 'take a photo' in query:
        #     ec.capture(0, "Jarvis Camera ", "img.jpg")

        # elif 'weather' in query or 'what is the weather today' in query:
        #     # Google Open weather website
        #     # to get API of Open weather
        #     api_key = "Api key"
        #     base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
        #     speak("City name: ")
        #     print("City name: ")
        #     city_name = takeCommand()
        #     complete_url = base_url + "appid =" + api_key + "&q =" + city_name

        elif "will you be my girlfreind" in query:
                speak("I'm not sure about, may be you should give me some time")

        elif 'exit' in query:
            speak("Thanks for giving me your time, it was great talking to you!!")
            break        
        # breaks wrks here only