import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Honey. Please tell me how I can help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def search_wikipedia(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def open_website(url):
    webbrowser.open(url)

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            search_wikipedia(query)
        elif 'open youtube' in query:
            speak("Opening YouTube...")
            open_website("youtube.com")
        elif 'open google' in query:
            speak("Opening Google...")
            open_website("google.com")
        elif 'open stackoverflow' in query:
            speak("Opening Stack Overflow...")
            open_website("stackoverflow.com")
        elif 'geeks' in query:
            speak("Opening geeks for geeks")
            open_website("https://www.geeksforgeeks.org/python-programming-language-tutorial/")
        elif 'bye' in query or 'quit' in query:
            speak("Goodbye!")
            break