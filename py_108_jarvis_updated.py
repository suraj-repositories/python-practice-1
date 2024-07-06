import pyttsx3
import speech_recognition as sr
import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return ""

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return "NONE"
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return "NONE"

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("Hi, I am Jarvis. How can I help you, sir?")

def main():
    wish_me()
    while True:
        user_input = listen()
        if "exit" in user_input.lower():
            speak("Goodbye!")
            break
        else:
            response = "You said: " + user_input
            print(response)
            speak(response)

if __name__ == "__main__":
    main()
