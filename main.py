import speech_recognition as spr
import pyttsx3 as sp
import pyjokes
import wikipedia
import pywhatkit
import datetime

listener = spr.Recognizer()
speak_engine = sp.init()

# setting the voice to female
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voices', voices[0].id)

speak_engine.say("Hi! I am Alex at your service.")
print("Alex : Hi! I am Alex at your service.")

# to get text to speech form
def talk(text):
    speak_engine.say(text)
    speak_engine.runAndWait()


def take_command():
    try:
        with spr.Microphone() as source:
            voice = listener.listen(source)
            task = listener.recongnize_google(voice)
            task1 = task.lower()
            if 'alex' in task1:
                print("You : ", task)
                print()
                task1 = task1.replace('alex', '')

    except:
        print("Unable to hear your voice! Try Again.")

    return task1


def execute_task():
    command = take_command()

    if 'play' in command:
        song = command.replace('play', "")
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print("Alexa : ", time)
        talk("Current time is " + time)

    elif 'tell about' in command:
        title = command.replace('tell about', '')
        info = wikipedia.summary(title, 5)
        print('Alexa : ', info)
        talk(info)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print('Alexa : ', joke)
        talk(joke)


execute_task()
