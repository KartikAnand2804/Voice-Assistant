# import tensorflow
import pygame  # import using - pip install pygame
import pyttsx3 # import using - pyttsx3
import datetime # inbuilt module
import speech_recognition as sr #import using - pip install SpeechRecognition 
import wikipedia  #import using - pip install wikipedia
import webbrowser # inbuilt module
import os   # inbuilt module
import time  # inbuilt module
import random  # inbuilt module
from PIL import Image, ImageGrab  #import using - pip install pillow
import urllib.request
import requests
import json
import operator
# from tkinter import *
import cv2
import smtplib
import roman
from urllib.request import urlopen
import pyjokes
import ctypes
import subprocess 
import win32com.client as wincl
import winshell 
from twilio.rest import Client
import wolframalpha 
import pywhatkit as kit
from googletrans import Translator 
from gtts import gTTS

#display modules
import tkinter as tk
from PIL import ImageTk, Image

# from ecapture import ecapture as ec

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voice)
engine.setProperty('voice', voices[1].id)
q = 'null'
def speak(audio):
     # This is the speaking settings
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    # this takes our voice as takecommand
    a = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        a.adjust_for_ambient_noise(source)
        a.pause_threshold = 1
        a.energy_threshold = 600                                   
        audio = a.listen(source)
    try:
        print("Recognizing...")
        query = a.recognize_google(audio, language='en-in')
        print(f"{query}\n")
    except Exception:
        print("SAY AGAIN")
        return "NONE"
    return query
def greeting():
    #this is used to greet user
    hour = int(datetime.datetime.now().hour)
    if 5 < hour < 8:
        speak("Can I sleep for some more hours!")
        speak("Leave! wait 2 sec let me drink my coffee")
        speak("Okay! Ready to assist you!") 
    elif  8 <= hour < 12:
        speak("Today is a new day a new opportunity! Give me some task")
    elif 12 <= hour < 14:
        speak("I got bored when you are not around me! Now can we talk")
    elif 14 <= hour < 17:
        speak("Someone just eat the lunch. I can smell it")
        speak("I think its yummy! Oh! Do you need any assist")
    elif 17<= hour <=20:
        speak("Good evening Sir.")
    elif 21<= hour <=23:
        speak("It is quite a long day! But I am boosted up on seeing you")
    else:
        speak("It is quite late now but I can still help you!")
def connect(host='http://google.com'):
        try:
            urllib.request.urlopen(host)
            a = True
        except:    
            a = False
        return a
def takescreenshot():   
    #this is for taking screenshot
    image = ImageGrab.grab()
    image.show()
def updatecontact():
    d = {}  
    speak("please enter the contact name and then press enter")
    keys = input() # here i have taken keys as strings
    speak("please enter the contact number and then press enter")
    values = int(input()) # here i have taken values as integers
    d[keys] = values
    print(d)
    f = open("contact.txt","w")
    f.write( str(d) )
    f.close()
    speak("Contact Saved!")
def todaynews(): 
    # BBC news api 
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=c2d72a4ef82d4304a5aa8eff2bf67a90"
  
    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_bbc_page["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
          
    for i in range(len(results)): 
          
        # printing all trending news 
        print(i + 1, results[i]) 
  
    #to read the news out loud for us 
    from win32com.client import Dispatch 
    # speak = Dispatch("SAPI.Spvoice") 
    speak('Showing top news')
    print(results)
def weather():
    res = requests.get("https://ipinfo.io/")
    res = res.json()
    
    # URL = "https://api.openweathermap.org/data/2.5/weather?appid=7e9e32bd98adc9cfd67239ea281ee407&q=Noida&mode=json&units=metric"
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=7e9e32bd98adc9cfd67239ea281ee407&q='
    url = api_address + res['region']
    url = url + str("&mode=json&units=metric")
    # URL = "https://api.openweathermap.org/data/2.5/weather?appid=7e9e32bd98adc9cfd67239ea281ee407&q=Noida&mode=json&units=metric"
    # HTTP request
    response = requests.get(url)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format        
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        # print(f"{CITY:-^30}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {report[0]['description']}")
        speak(f"You are in {res['region']} city")
        speak(f"and the temperature is {temperature} degree celcius! The whether report are saying {report[0]['description']}")
    else:
     # showing the error message
      speak("Do you live in dark dimension! I can't figure out your wheather")  
def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('airodragon@gmail.com', 'Mihir@1919') # email id - use any email id whose security/privacy is off
    server.sendmail('airodragon1919@gmail.com', to, content)
    server.close()
def calculator():
    r = sr.Recognizer()
    my_mic_device = sr.Microphone(device_index=1)
    with my_mic_device as source:
        speak("Say what you want to calculate, example: 3 plus 3")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        my_string=r.recognize_google(audio)
        speak(my_string)
    try:
        def get_operator_fn(op):
            return {
                'sum' : operator.add,
                'subtract' : operator.sub,
                'add' : operator.add,
                'multiply' : operator.mul,
                '+' : operator.add,
                '-' : operator.sub,
                'x' : operator.mul,
                'divided' :operator.__truediv__,
                'Mod' : operator.mod,
                'mod' : operator.mod,
                '^' : operator.xor,
                }[op]

        def eval_binary_expr(op1, oper, op2):
            op1,op2 = int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)
        print(eval_binary_expr(*(my_string.split())))
        speak('is')
        speak(eval_binary_expr(*(my_string.split())))
    except:
        speak("i am not able to calulate this")
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('mihir190801@gmail.com', 'dhwbjkzhjpkfzdol')
    server.sendmail('mihir190801@gmail.com', to, content)
    server.close()

def voiceassistant():
    if __name__ == "__main__":
        os.system('cls')
        print("Welcome Sir!")
        speak("Hey Boss! Let me check where is my body")
        a = connect("http://google.com")
        if a == True:
            speak("Oh! It's here! Now I am ready to work!")
            greeting() 
            while True:
                query =takecommand().lower()    
                if 'exit' in query:
                    speak("See you later")
                    break 
                elif 'weather' in query:
                    weather()
                elif 'say hello' in query:
                    speak('Hello Everyone! My self Helen! I am a creation of Mihir')
                elif 'send a mail' in query:
                    try:
                        speak("What should I say?")
                        content = takecommand()
                        speak("whome should i send")
                        to = input()    
                        sendEmail(to, content)
                        speak("Email has been sent !")
                    except Exception as e:
                        print(e)
                        speak("I am not able to send this email")
                elif 'time' in query:
                    strTime= datetime.datetime.now().strftime("%H:%M:%S")
                    strdate =datetime.date.today()
                    print(strTime,strdate)
                    speak(f"It is {strdate}")
                    speak(f"AND THE TIME IS {strTime}")   
                elif 'write a note' in query: 
                    speak("What should i write, sir") 
                    note = takecommand() 
                    file = open('notes.txt','a') 
                    # speak("Sir, Should i include date and time") 
                    # snfm = takecommand() 
                    # if 'yes' in snfm or 'sure' in snfm: 
                    #     # strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                    #     # file.write(strTime) 
                    #     file.write(" :- ") 
                    #     file.write(note) 
                    # else: 
                    file.write(note) 
                elif 'joke' in query:
                    t = 0
                    t = pyjokes.get_joke() 
                    print(t)
                    speak(t)
                elif "show note" in query: 
                    speak("Showing Notes") 
                    file = open("notes.txt", "r")  
                    print(file.read()) 
                    speak(file.read(6)) 
                elif 'news' in query:    
                    todaynews()
                elif 'lock window' in query: 
                    speak("locking the device") 
                    ctypes.windll.user32.LockWorkStation()
                    exit() 
                elif 'lock the window' in query: 
                    speak("locking the device") 
                    ctypes.windll.user32.LockWorkStation()
                    exit()
                elif 'shutdown' in query: 
                    speak("Hold On a Sec ! Your system is on its way to shut down") 
                    subprocess.call('shutdown / p /f')
                elif "who i am" in query: 
                    speak("If you talk then definately your human.")
                elif 'how are you' in query: 
                    speak("I am fine, Thank you") 
                    speak("How are you, Sir") 
                elif 'fine' in query or "good" in query: 
                    speak("It's good to know that your fine")
                elif 'empty recycle bin' in query: 
                    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
                    speak("Recycle Bin is now empty") 
                elif "will you be my gf" in query or "will you be my bf" in query or"will you be my girlfriend" in query or"will you be my boyfriend" in query:    
                    speak("Being in a relationship with you is my pleasure.") 
                elif "how are you" in query: 
                    speak("I'm fine, glad you ask that") 
                elif "i love you" in query: 
                    speak("I love you too!")
                elif "what is" in query or "who is the" in query or "where" in query:  
                    client = wolframalpha.Client("ETWHT8-RA48WJY76T") 
                    res = client.query(query) 
                    # try: 
                    #     print (next(res.results).text)  
                    #     speak (next(res.results).text) 
                    # except Exception as uvM: 
                    #         print(uvM)
                    #         print ("No results")
                    if res['@success']=='true':
                        pod0=res['pod'][0]['subpod']['plaintext']
                        # print(pod0)
                        pod1=res['pod'][1]
                    if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
                        result = pod1['subpod']['plaintext']
                        print(result)
                        speak(result)
                    else:
                         print("No answer returned")
                elif'who is' in query:
                    query = query.replace("who is","")  #so that the 'who is' get removed from takecommand for better search
                    try:
                        results = wikipedia.summary(query,sentences=1)  # it will take 2 sentence 
                        speak("ACCORDING TO DATABASE")
                        print(results) 
                        speak(results)
                    except Exception:
                        query = query.replace("who is","")
                        speak("can't find it in database.showing you google results")
                        webbrowser.open(f"https://www.google.com/search?q={query}")         
                elif "restart" in query: 
                    subprocess.call(["shutdown", "/r"])   
                elif "hibernate" in query or "sleep" in query: 
                    speak("Hibernating") 
                    subprocess.call("shutdown / h") 
                    exit()
                elif "log off" in query or "sign out" in query: 
                    speak("Make sure all the application are closed before sign-out") 
                    time.sleep(5) 
                    subprocess.call(["shutdown", "/l"]) 
                    exit()
                elif 'open youtube' in query: 
                    speak("Here you go to Youtube\n") 
                    webbrowser.open("youtube.com") 
                elif 'open google' in query: 
                    speak("Here you go to Google\n") 
                    webbrowser.open("google.com")        
                elif "don't listen"in query: 
                    speak("for how much seconds you want to stop me from listening commands") 
                    a = int(takecommand()) 
                    time.sleep(a) 
                    print(a)
                elif "do not listen" in query: 
                    speak("for how much seconds you want to stop me from listening commands") 
                    a = int(takecommand()) 
                    time.sleep(a) 
                    print(a)  
                elif "stop listening"in query: 
                    speak("for how much seconds you want to stop me from listening commands") 
                    a = int(takecommand()) 
                    time.sleep(a) 
                    print(a)          
                elif "purpose of you" in query:
                    speak("I am Helen an assistant.I was made as a mini project.I will help you with basic things on computer.")
                elif "introduce yourself" in query or "who are you" in query:
                    speak("Hello to Everyone I am Helen an assistant created  by Mihir and his team! I was made as a mini project.")
                elif "you do" in query:
                    speak("I can play music from youtube, tell you jokes, today weather.")
                    speak("To know all my functions! Check the readme file.")
                elif 'open chrome' in query:
                    chromepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(chromepath)
                elif 'screenshot' in query:
                    time.sleep(1)
                    takescreenshot()
                elif 'open gmail' in query:
                    speak("OPENING your gmail")
                    webbrowser.open("www.gmail.com")
                    break
                elif 'play' in query:
                    query = query.replace("play","")
                    kit.playonyt(query)
                    exit()
                elif 'message' in query:
                    hour=int(datetime.datetime.now().strftime("%H"))
                    minute=int(datetime.datetime.now().strftime("%M"))
                    speak("please enterthe phone number whom you want to send the message")
                    print(hour)
                    print(minute)
                    query = str(input())
                    speak("what message do you want to send")
                    query1 = takecommand().lower()
                    kit.sendwhatmsg('+91'+ query,query1,hour,minute+2,wait_time=5)
                elif 'update contacts' in query:
                    updatecontact()
                elif 'add contacts' in query:
                    updatecontact()
                elif 'add a contact' in query:
                    updatecontact()
                elif 'add a contacts' in query:
                    updatecontact()
                elif 'add contact' in query:
                    updatecontact()
                elif 'update contact' in query:
                    updatecontact()
                elif 'update a contact' in query:
                    updatecontact()
                elif 'update a contacts' in query:
                    updatecontact()
                elif 'hello' in query:
                    speak("Hello there!")
                elif 'open instagram' in query:
                    webbrowser.open("www.instagram.com/")         
                elif 'made you' in query:
                    speak("I have been created by Mihir and his team as a mini project!") 
                elif 'help' in query:
                    speak("How can I help you!")
                elif 'calculate' in query:
                    calculator()
                elif 'calculator' in query:
                    calculator()
                elif 'rock paper scissor' in query:
                    l1 = ['rock','paper','scissor']
                    while 1:
                        l2 = random.choice(l1)
                        speak("ROCK PAPER SCISSOR")
                        x = takecommand().lower()
                        if l2 == 'rock':
                            if 'rock' in x:
                                print("I CHOOSED ROCK")
                                speak("I CHOOSED ROCK")
                                print("IT IS A DRAW")
                                speak("IT IS A DRAW")
                            elif 'scissor' in x:
                                print("I CHOOSED ROCK")
                                speak("I CHOOSED ROCK")
                                print("YOU LOOSE THE GAME")
                                speak("YOU LOOSE THE GAME")
                            elif 'paper' in x:
                                print("I CHOOSED ROCK")
                                speak("I CHOOSED ROCK")
                                print("YOU WON THE GAME")
                                speak("YOU WON THE GAME")
                            elif 'exit' in x:
                                speak("OK SIR")
                                break
                            else:
                                print("PLEASE CHOOSE A VALID OPTION") 
                                speak("PLEASE CHOOSE A VALID OPTION") 
                        elif l2 == 'paper':
                            if 'rock' in x:
                                print("I CHOOSED PAPER")
                                speak("I CHOOSED PAPER")
                                print("YOU HAVE LOOSE")
                                speak("YOU HAVE LOOSE")
                            elif 'scissor' in x:
                                print("I CHOOSED PAPER")
                                speak("I CHOOSED PAPER")
                                print("YOU WON THE GAME")
                                speak("YOU WON THE GAME")
                            elif 'paper' in x:
                                print("I CHOOSED PAPER")
                                speak("I CHOOSED PAPER")
                                print("IT IS A DRAW")
                                speak("IT IS A DRAW")
                            elif 'exit' in x:
                                speak("OK SIR")
                                break
                            else:
                                print("PLEASE CHOOSE A VALID OPTION") 
                                speak("PLEASE CHOOSE A VALID OPTION") 
                        elif l2 == 'scissor':
                            if 'rock' in x:
                                print("I CHOOSED SCISSOR")
                                speak("I CHOOSED SCISSOR")
                                print("YOU HAVE WON THE GAME")
                                speak("YOU HAVE WON THE GAME")
                            elif 'scissor' in x:
                                print("I CHOOSED SCISSOR")
                                speak("I CHOOSED SCISSOR")
                                print("IT IS A DRAW")
                                speak("IT IS A DRAW")
                            elif 'paper' in x:
                                print("I CHOOSED SCISSOR")
                                speak("I CHOOSED SCISSOR")
                                print("YOU HAVE LOOSE THE GAME")
                                speak("YOU HAVE LOOSE THE GAME")
                            elif 'exit' in x:
                                speak("OK SIR")
                                break
                            else:
                                print("PLEASE CHOOSE A VALID OPTION")                         
                                speak("PLEASE CHOOSE A VALID OPTION") 
                else:
                    speak("I can't help with it right now. My creaters are upgrading me everyday")         
        else:   
                speak("Oh no! I think i lost my body! Can you please connect to internet and reopen me to help in finding it")
                exit

# display 
root = tk.Tk()
root.title("voice assistant")
buttonText = "Get Started."
HEIGHT = 300
WIDTH = 600
labeltext = "HELEN VOICE ASSISTANT"
creatorLabelText = "<Created by>\n KARTIK, MIHIR, HIMANI"

img = Image.open("mic.png")
img = img.resize((50,50), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)


def runningMsg():
    labelgreet = tk.Label(frame, text='voice assistant is running.', bg='black', fg='white', justify='center')
    labelgreet.pack()
    voiceassistant()

#background window
canvas = tk.Canvas(root, height= HEIGHT, width= WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='black')
frame.place(relwidth=1, relheight=1)

#introductory label
label = tk.Label(frame, text=labeltext, bg='black', fg='white')
label.config(font= ("Courier", 32))
label.pack()

#creator label
creLabel = tk.Label(frame, text= creatorLabelText, bg='black', fg='white', font='Times')
creLabel.config(font= ("Courier", 16))
creLabel.pack()

#action button
button = tk.Button(frame, text=buttonText, bg='white', image= photoImg,  activebackground='pink', highlightcolor='red', command=runningMsg, compound='top')
button.config(font= ("Courier", 16))
button.pack()

# exit button
exit_button = tk.Button(frame, text="exit frame", bg='white', command=root.quit)
exit_button.pack()

#information from the user

root.mainloop()