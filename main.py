import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import sys
import random
import pyautogui
from tkinter import *
import time


root = Tk()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Defining functions

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().strftime('%H'))

    if hour <= 12:
        text = 'Good Morning'
    elif hour <= 17:
        text = 'Good Afternoon'
    else:
        text = 'Good Evening'
    
    print(f'{text}, How may I help you ?')
    speak(text)
    speak('How may I help you ?')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold = 400
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'You said: {query}\n')

    except Exception as e:
        print(e)
        
        print('Say that again please...')
        speak('Say that again please...')

        return 'None'

    return query

def get_val():
    PSWD = passwordvalue.get()
    CONF_PSWD = conf_passwordvalue.get()
    return PSWD, CONF_PSWD


def takePassword():
    with open ("jarvis_pass.txt", 'r') as f:
        JARVIS_password = f.read()

    root.mainloop()
    return_val = False
    value = get_val()
    if value[0] == value[1]:  
        if value[0] == JARVIS_password:
            return_txt = 'Your password login was successfull !'
            return_val = True
        else:
            return_val = False
            return_txt = "Sorry, your password did not matched !"
    else:
        return_val = False
        return_txt = "Sorry, PASSWORD and CONFIRM PASSWORD should match !"

    return return_val, return_txt
    
    


'''
functions done -

wikipedia
youtube
google
stack overflow
website opening
password taking
password changing
exitting
timer/stopwatch

'''

# Creating window
root.geometry('500x250')
root.minsize(500, 250)
root.maxsize(500, 250)

# Creating Lables
Label(root, text = 'PLEASE ENTER', font = 15).place(x = 70, y = 20)
Label(root, text = 'J.A.R.V.I.S', font = 15, foreground = "red").place(x = 225, y = 20)
Label(root, text = 'PASSWORD', font = 15).place(x = 335, y = 20)
Label(root, text = 'Password:', font = 10).place(x = 20, y = 80)
Label(root, text = 'Confirm Password:', font = 10).place(x = 20, y = 120)

# Creating Input variables
passwordvalue = StringVar()
conf_passwordvalue = StringVar()

# Creating Entries
password = Entry(root, textvariable = passwordvalue).place(x = 120, y = 85)
conf_password = Entry(root, textvariable = conf_passwordvalue).place(x = 200, y = 125)
 
# Creating Buttons
btn = Button(text = 'ENTER', foreground = 'white', background = 'red', command = get_val).place(x = 200, y = 180, width = 70, height = 30)
btn1 = Button(text = 'ENTER', foreground = 'white', background = 'red', command = root.destroy).place(x = 200, y = 220, width = 70, height = 30)

if __name__ == "__main__":
    start = takePassword()
    wait = False
    if start[0] == True:
        greet()
        while True:
            
            
            # if 'hi jarvis' in query:
            #     index = random.randint(0, 18)
            #     print(hello[index] + ", that's hello in " + hello_cont[index])
            #     speak(hello[index] + ", that's hello in " + hello_cont[index])

            if wait == False:
                query = takeCommand().lower()

                hello = ['hola', 'prannam', 'vandanalu', 'annyeong', 'nggoleki', 'hallo', 'sat srī akāl', 'kon’nichiwa', 'privet', 'hyālō', 'olá', 'marhabaan', 'namaste', 'ahoj', 'mhoro', 'yasou', 'ciao', 'bonjour', 'xin chào']

                hello_cont = ['Spanish', 'Bhojpuri', 'Telegu', 'Korean', 'Javanese', 'German', 'Punjabi', 'Japanese', 'Russian', 'Bengali', 'Portuguese', 'Arabic', 'Hindi', 'Czech', 'Zimbabwe', 'Greek', 'Italy', 'French', 'Vietnamese']


            elif 'hi jarvis' in query:
                index = random.randint(0, 18)
                print(hello[index] + ", that's hello in " + hello_cont[index])
                speak(hello[index] + ", that's hello in " + hello_cont[index])
            elif 'hi' in query:
                index = random.randint(0, 18)
                print(hello[index] + ", that's hello in " + hello_cont[index])
                speak(hello[index] + ", that's hello in " + hello_cont[index])
            elif 'hey' in query:
                index = random.randint(0, 18)
                print(hello[index] + ", that's hello in " + hello_cont[index])
                speak(hello[index] + ", that's hello in " + hello_cont[index])
            elif 'hay' in query:
                index = random.randint(0, 18)
                print(hello[index] + ", that's hello in " + hello_cont[index])
                speak(hello[index] + ", that's hello in " + hello_cont[index])
            elif 'hello' in query:
                index = random.randint(0, 18)
                print(hello[index] + ", that's hello in " + hello_cont[index])
                speak(hello[index] + ", that's hello in " + hello_cont[index])

            elif 'how are you' in query:
                print("I am fine, and you ?")
                speak("I am fine, and you ?")
            elif "what's up" in query:
                print("I am fine, and you ?")
                speak("I am fine, and you ?")

            elif 'created jarvis' in query:
                print("I was created by some god-like humans")
                speak("I was created by some god-like humans")
            elif 'created you' in query:
                print("I was created by some god-like humans")
                speak("I was created by some god-like humans")

            elif 'thanks' in query:
                print("My pleasure !")
                speak("My pleasure !")
            elif 'thank you' in query:
                print("My pleasure !")
                speak("My pleasure !")

            elif 'open wikipedia' in query:
                speak('opening wikipidia')
                print('Opening wikipedia')
                speak('What do you want to search in wikipedia \n')

                query = takeCommand().lower()
                query = query.replace('jarvis', '')
                query = query.replace('search', '')
                query = query.replace('open', '')

                speak(f'Searching {query} in wikipedia')
                try:
                    result = wikipedia.summary(query, sentences = 4)
                    speak('According to wikipedia:')
                    print(result)
                    speak(result)
                except Exception as e:
                    print('Sorry, your query is not available in wikipedia')
                    speak('Sorry, your query is not available in wikipedia')

            elif 'play game' in query:
                print("Select a game  to play")
                speak("Select a game  to play")

            elif 'change password' in query:
                while query != 'yes':

                    speak('Please speak your new password')
                    query = takeCommand().lower()
                    password = query
                    print(f'So your new password is {password}')
                    speak(f'So your new password is {password}')
                    speak('Is that ok !')
                    query = takeCommand().lower()
                    if query == 'yes':
                        with open ("jarvis_pass.txt", 'w') as w:
                            w.write(password)

                        print('Ok your password is updated')
                        speak('ok your password is updated')
                    elif query == 'no':
                        no = 'no'

            elif 'what' and 'time' in query:
                print(datetime.datetime.now().strftime('%H hours %M minutes and %S seconds'))
                speak(datetime.datetime.now().strftime('%H hours %M minutes and %S seconds'))

            elif 'open youtube' in query:
                speak('opening Youtube')
                webbrowser.open('youtube.com')
                quit()

            elif 'open stack overflow' in query:
                speak('opening stack overflow')
                webbrowser.open('stackoverflow.com')
                quit()

            elif 'open google' in query:
                speak('opening google')
                webbrowser.open('google.com')
                quit()

            elif 'open website' in query:
                speak('which website do you want to open')
                query = takeCommand().lower()
                query = query.replace('open', '')
                speak(f'opening {query}')
                webbrowser.open(query)
                quit()

            elif 'write' in query:
                speak('Speak the text to be written')
                query = takeCommand().lower()
                pyautogui.write(query)

            elif 'exit' in query:
                speak('adios, amigo')
                speak('quitting this session')
                quit()
                
            elif 'close' in query:
                speak('aadios, amigo')
                speak('quitting this session')
                quit()

            elif 'bye' in query:
                speak('aadios amigo')
                speak('quitting this session')
                quit()
                
            elif 'timer' in query or 'stopwatch' in query:
                    speak("For how many minutes?")
                    local_time = takeCommand().lower()
                    local_time = local_time.replace('for', '')
                    local_time = local_time.replace('minutes', '')
                    local_time = local_time.replace('minute', '')
                    local_time = local_time.replace('in', '')

                    local_time = float(local_time)
                    local_time = local_time * 60
                    speak(f'I will remind you in {local_time} seconds')

                    time.sleep(local_time)
                    speak('Your time has been finished sir')
                    
            else:
                if query != 'none':
                    search = query
                    print("Here's what I found on the web")
                    speak("Here's what I found on the web")
                    wait = True
                    webbrowser.open('https://google.com/?#q=' + search)

    else:
        print(start[1])
        speak(start[1])
        quit()
