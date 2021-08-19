# Importing the libraries

import pyttsx3 #pip install pyttsx3 (For Speak)
import datetime 
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui (For Screenshot)
import psutil #pip install pustil
import pyjokes #pip install pyjokes
import random
import operator
import json
import wolframalpha
from urllib.request import urlopen
import requests
import time

# Setting up commands
        
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
ss_count = 0

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour clock
    print("the current time for 24 hour clock is {}".format(Time))
    speak("the current time for 24 hour clock is ")
    speak(Time)
    Time=datetime.datetime.now().strftime("%I:%M:%S") # for 12-hour clock
    print("the current time for 12 hour clock is {}".format(Time))
    speak("the current time for 12 hour clock is ")
    speak(Time)
def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    print("the current date is {}/{}/{}".format(date, month, year))
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
def wishme():
    print("Welcome back Boss")
    speak("Welcome back Boss")
    time_()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        print("Good Morning Sir")
        speak("Good Morning Sir")
    elif hour >=12 and hour<18:
        print("Good Afternoon Sir!")
        speak("Good Afternoon Sir!")
    elif hour >=18 and hour <24:
        print("Good Evening Sir!")
        speak("Good Evening Sir!")
    else:
        print("Good Night Sir!")
        speak("Good Night Sir!")
    print("Pandora at your service. Please tell me how can I help you?")
    speak("Pandora at your service. Please tell me how can I help you?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(query)
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail 
    server.login('Your email', 'Your password')
    server.sendmail('Your email', to, content)
    server.close()
def screenshot():
    img = pyautogui.screenshot()
    img.save("screenshot"+str(ss_count)+".jpg")
    ss_count = ss_count+1
def cpu():
    usage = str(psutil.cpu_percent())
    response = 'CPU is at'+ usage
    print(response)
    speak(response)
    battery = psutil.sensors_battery()
    response = battery.percent
    print("Battery is at {}".format(response))
    speak("Battery is at")
    speak(response)
def jokes():
    response = pyjokes.get_joke()
    print(response)
    speak(response)

def Introduction():
    response = '''I am Pandora 1.0 , Personal AI assistant ,
I am created by Moses and Sakthi, 
I can help you in various regards , 
I can search for you on the Internet , 
I can also provide information any subject you are looking, 
In layman terms , I can try to make your life a bed of roses , 
and I am a Trained AI for Humanoid conversations, 
Where you just have to command me , and I will do it for you , '''
    print(response)
    speak(response)

def Creator():
    response = '''Moses and Sakthi are extra-ordinary people ,
They have a passion for Robotics, Artificial Intelligence and Machine Learning ,
They are very co-operative ,
If you are facing any problem regarding the 'Pandora', They will be glad to help you '''
    print(response)
    speak(response)




    
if __name__ == '__main__':


    clear = lambda: os.system('cls') 
	
	# This Function will clean any 
	# command before execution of this python file
    clear()

    wishme()
    
    
    while True:
        query = TakeCommand().lower()
            
        #quit
        if 'offline' in query or "go to sleep" in query:
            speak("going Offline")
            break
        
        elif 'who are you' in query or 'tell me about yourself' in query or 'about yourself' in query:
            Introduction()
        elif 'who is your creator' in query or 'tell me about your creator' in query or 'about your creator' in query:
            Creator()
            
        elif 'time' in query:
            time_()
        elif 'date' in query:
            date()
        elif 'how are you' in query:
            print("I am fine, Sir Thanks for asking"+"\n"+"How are you Sir?")
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            if 'fine' in query or "good" in query: 
                print("It's good to know that your fine")
                speak("It's good to know that your fine")
            else:
                print("I hope you get well soon.")
                speak("I hope you get well soon.")
        
        elif 'about' in query:
            speak("Searching...")
            query = query.split("about")[1]
            try:
                result = wikipedia.summary(query, sentences=3)
                speak("According to Pandora")
                print(result)
                speak(result)
            except Exception as e:
                result = "Sorry I Do not understand that"
                print(result)
                speak(result)
        
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            print(query)
            try:
                result = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(result)
                speak(result)
            except Exception as e:
                result = "Sorry I Do not understand that"
                print(result)
                speak(result)
            
            
        
        
        elif 'open youtube' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            speak("Here we go to Youtube\n")
            wb.open("https://www.youtube.com/results?search_query="+Search_term)
            time.sleep(5)
        elif 'search google' in query or "search on google" in query or "search something on google" in query or "search something for me on google" in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            wb.open('https://www.google.com/search?q='+Search_term)
        
        #elif 'search' in query: 
            #query = query.replace("query","")
            #wb.open(query)
        
        elif "who am i" in query:
            print("If you can talk, then definitely you are a human")
            speak("If you can talk, then definitely you are a human")
        elif "why you came to this world" in query:
            print("Thanks to Moses and Sakthi. further it is a secret")
            speak("Thanks to Moses and Sakthi. further it is a secret")
        elif 'word' in query:
            speak("opening MS Word")
            word = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word'
            os.startfile(word)

        elif 'what is love' and 'tell me about love' in query:
            response = '''It is 7th sense that destroy all other senses , 
And I think it is just a mere illusion , 
It is waste of time'''
            print(response)
            speak(response)

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled") 

        elif 'send email' in query:
            try:
                print("What should I say?")
                speak("What should I say?")
                content = TakeCommand()
                print("Who is the Reciever?")
                speak("Who is the Reciever?")
                reciept = input("Enter recieptant's name: ")
                to = (reciept)
                sendEmail(to,content)
                speak(content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the email.")
        elif 'search in chrome' in query:
            print("What should I search ?")
            speak("What should I search ?")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        
        
        elif 'play songs' in query or 'play video' in query or 'play movie' in query:
            video ='C:\\Users\\Welcome\\Desktop\\movie'
            audio = 'Songs path'
            print("What songs should i play? Audio or Video")
            speak("What songs should i play? Audio or Video")
            ans = (TakeCommand().lower())
            while(ans != 'audio' and ans != 'video'):
                print("I could not understand you. Please Try again.")
                speak("I could not understand you. Please Try again.")
                ans = (TakeCommand().lower())
        
           # if 'audio' in ans:
            #        songs_dir = audio
            #        songs = os.listdir(songs_dir)
            #        print(songs)
            #        print("select a random number")
            #        speak("select a random number")
            #       and = (TakeCommand().lower())
               # while('number' not in rand and rand != 'random'):                       #used while loop to keep the jarvis on the speak command untill req. command is given.
                # print("I could not understand you. Please Try again.")
                # speak("I could not understand you. Please Try again.")          #first used 'rand' before while then again after, so that rand is already defind, and Input is taken and then checked if it is according to reuirement or not. And if it is not which means while loop is true, then commands under 'while loop' will execute untill desired approach.As it will again ask the user for input in the same block. 
                # rand = (TakeCommand().lower())

           # if 'number' in rand:
                 #   rand = int(rand.replace("number ",""))
                 #   os.startfile(os.path.join(songs_dir,songs[rand]))
                 #   continue                                                    #'continue' is used, so that after executing the commands in 'if' or 'elif' block, it will move to the next part of execution (or code). but in this case as this is the last execution of related function then it will move to the next function (i.e. in this code, it will be TakeCommand() )
            #elif 'random' in rand:
              #      rand = random.randint(1,219)
             #   os.startfile(os.path.join(songs_dir,songs[rand]))
            #       continue
            elif 'video' in ans:
                    songs_dir = video
                    songs = os.listdir(songs_dir)
                    print(songs)

            #elif 'movie' in ans:
            #        songs_dir = video
             #       songs = os.listdir(songs_dir)
             #       print(songs) 

           
                
            
        elif 'remember that' in query:
            print("What should I remember ?")
            speak("What should I remember ?")
            memory = TakeCommand()
            print("You asked me to remember that"+memory)
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            response = remember.read()
            print("You asked me to remeber that"+response)
            speak("You asked me to remeber that"+response)
        
        
        elif "write a note" in query:
            print("What should i write, sir")
            speak("What should i write, sir")
            note = TakeCommand()
            file = open('note.txt', 'w')
            print("Sir, Should i include date and time")
            speak("Sir, Should i include date and time")
            dt = TakeCommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
            else:
                file.write(note)
                
        elif "show note" in query:
            print("Showing Notes")
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read()) 

        elif "weather" in query: 
			
			# Google Open weather website 
			# to get API of Open weather
            api_key = "open weather api"
            base_url = "http://api.openweathermap.org/data /2.5/weather?q="
            speak(" City name ")
            print("City name : ")
            city_name = TakeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
            
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                
            else:
                speak(" City Not Found ") 





        elif 'news' in query:
            
            try:

                jsonObj = urlopen('''news api link''')
                data = json.load(jsonObj)
                i = 1
                print('here are some top news from the times of india')
                speak('here are some top news from the times of india')
                print('''=============== TOP HEADLINES ============'''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    
            except Exception as e:
                print(str(e)) 


                
        
        elif 'take screenshot' in query or 'take a screenshot' in query or 'take a snap' in query:
            screenshot()
            print("Done!")
            speak("Done!")    
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        
        
        #show location on map
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            print("User asked to Locate")
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            print("I'm not sure about that ")
            speak("I'm not sure about that ")
            
        elif "i love you" in query:
            print("It's hard to understand, I am still trying to figure this out.")
            speak("It's hard to understand, I am still trying to figure this out.")
        

        #calculation
        elif "calculate" in query:
            
            app_id = "wolfram alpha api"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer) 

        



        #General Questions
        elif "what is" in query or "who is" in query: 
			
    			
            client = wolframalpha.Client("A72XP6-2W682VLXWU")
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results") 




        #sleep-time
        elif "don't listen" in query or "stop listening" in query:
            print("for how much seconds you want me to stop listening commands")
            speak("for how much seconds you want me to stop listening commands")
            a = int(TakeCommand().split()[0])
            time.sleep(a)
            print(a)

        else:
            print("I am sorry, I don't understand that")
            speak("I am sorry, I don't understand that")
