# voice_assistant.py

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        return command.lower()

def run_assistant():
    speak("Hello, how can I help you?")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hi there! How can I help you?")
        elif "time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time}")
        elif "date" in command:
            date = datetime.datetime.now().strftime('%B %d, %Y')
            speak(f"Today's date is {date}")
        elif "search" in command:
            speak("What do you want to search for?")
            query = listen()
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}")
        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I can search that for you.")
            url = f"https://www.google.com/search?q={command}"
            webbrowser.open(url)

if __name__ == "__main__":
    run_assistant()
