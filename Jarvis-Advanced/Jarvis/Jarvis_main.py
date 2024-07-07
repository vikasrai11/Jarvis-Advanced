import datetime
from email import message
import webbrowser
import pyttsx3
import speech_recognition
import requests
from requests import get
from bs4 import BeautifulSoup
import os
import pyautogui
import random
from plyer import notification
from pygame import mixer
import pywhatkit as kit
import qr_code
from password_generate import pass_generate
from link_shortner import shorten_link
from video_download import get_video_details_and_download
from image_gen import img_gen
import closeapp
import time
from eye_ctrl import eye_controlled_mouse


from INTRO import play_gif
play_gif
pyautogui.sleep(1)
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query




if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break 
                
               

                elif "schedule my day" in query:
                    tasks = [] 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%I:%M %p")
                    speak(f"Time is {strTime}")
                elif "date" in query:
                    strDate=datetime.datetime.now().strftime("%m/ %d/ %y")
                    speak(f"Date is {strDate}")
                
                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )
                

                elif "open" in query:   
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    speak(f"Launching {query}")
                    pyautogui.press("enter")  
                elif "close" in query:
                    query=query.replace("close","")
                    query = query.replace("jarvis","")
                    st=[query]
                    closeapp.close(st[0])
                    
                elif "launch" in query and "new" in query and "tab" in query:
                    pyautogui.hotkey('ctrl','n')
                    speak("New Tab launched")
                elif "launch" and "incognito" in query:
                    pyautogui.hotkey('ctrl','shift','n')
                    speak("Incognito Tab launched")
                elif "minimize" in query or "minimise" in query:
                    pyautogui.hotkey("alt","space")
                    time.sleep(1)
                    pyautogui.press("n")
                    speak("Window Minimized...." )
                    
                elif "maximize" in query:
                    pyautogui.hotkey("alt","space")
                    time.sleep(1)
                    pyautogui.press("x")
                    speak("Window Maximized...." )
                    
                elif "history" in query or "histry" in query:
                    pyautogui.hotkey('ctrl','h')
                    
                elif "downloads" in query:
                    speak("Launching Downloads...." )
                    pyautogui.hotkey('ctrl','j')   
                    
                elif "previous" in query and "tab" in query:
                    pyautogui.hotkey('ctrl','shift','tab')
                    
                elif "next" in query and "tab" in query:
                    pyautogui.hotkey('ctrl','tab')

                elif 'ip address' in query:
                    ip= get('https://api.ipify.org').text
                    print(f"Your IP address is {ip}")
                    speak(f"your IP address is {ip}")    
                elif 'location' in query:
                    ip= get('https://api.ipify.org').text
                    url="https://get.geojs.io/v1/ip/geo/" +ip +".json"
                    geo=requests.get(url)
                    geo_data=geo.json()
                    print(geo_data)
                    city=geo_data["city"]
                    state=geo_data["region"]
                    internet=geo_data["organization"]
                    print(f"City={city}\nState={state}\nInternet provider={internet}")
                    speak(f"Your city is {city}.")
                                 

                elif "screenshot" in query:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                     speak(f"Screenshot Captured!")
                
                elif "qr" in query and "code" in query:
                    speak("Enter the link which you want to convert into QR code")
                    data=input("Enter the link\n")
                    qr_code.generate_qr(data)
                    speak(f"QR code generated.")

                elif "generate" in query and "password" in query:
                    speak("Enter the number of alphabets in password")
                    l=int(input("Enter the number of alphabets in password\n"))
                    speak("Enter the number of symbols in password")
                    s=int(input("Enter the number of symbols in password\n"))
                    speak("Enter the number of numbers in password")
                    n=int(input("Enter the number of numbers in password\n"))
                    pass_generate(l,s,n)
                    
                elif "url" in query or "link" in query and "shortener" in query:
                    speak("please enter the link to shorten")
                    link=input("Enter the link to shorten\n")
                    shorten_link(link)
                    speak("here is your shortened link,sir.")
                    
                # elif "eye" in query and "control" in query:
                #     speak("Eye control is activated")
                #     eye_controlled_mouse()
                    
                elif "click my photo" in query:
                    speak(f"launching Camera !!")
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                    speak(f"Pictured clicked.")
                    
                elif "download" in query and "video" in query:
                    speak("sure sir, enter the url of video you want to download")
                    url=input("Enter the url\n")
                    get_video_details_and_download(url,download=True)
                    speak(f"Video downloades successfully.")
                    
                elif "generate" in query and "image" in query:
                    speak("Enter the prompt to generate the image")
                    prompt=input("Enter the prompt\n")
                    speak("Enter the output file name with extension")
                    output=input("Enter the output filename with extension\n")
                    img_gen(prompt,output)
                    speak(f"Image generated with name{output}")

                elif "start" in query or 'ai' in query and "chat" in query:
                    from gradio_client import Client
                    gradio_client=Client("Your mistral AI API")
                    speak("Launching AI chat...!! ")
                    choice="yes"
                    while True:
                        user_query=input("Enter ur message:\n")
                        chat_response=gradio_client.predict(
                            user_query ,
                            0.8, #control randomness of response
                            1024, #limit length of generated response
                            0.9, #set probability threshold for word selection
                            1.1, #penalise repeated phrase in response
                            api_name="/chat"
                        )
                        print(f"CHAT RESPONSE:{chat_response}")
                        print("Do you want to continue...")
                        choice=input("enter yes or no\n")
                        if choice=="no":
                            break
               
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                
                elif "tired" in query:
                    speak("Playing your favourite song, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("{Youtube video url}")
                    elif b==2:
                        webbrowser.open("{Youtube video url}")
                    elif b==3:
                        webbrowser.open("{Youtube video url}")

                elif 'play a song on youtube' in query:
                    speak("Which song would you listen?")
                    query = takeCommand().lower()
                    kit.playonyt({query})
                    speak(f"playing {query}")

                elif 'open stack overflow' in query:
                    webbrowser.open("www.stackoverflow.com")
                elif 'instagram profile' in query or 'profile on instagram' in query:
                    speak("Enter username to search")
                    name=input("Enter username: ")
                    webbrowser.open(f"www.instagram.com/{name}")
                    

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("Video unmuted")


                elif "volume" in query and "up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume" in query and "down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()


                elif "whatsapp message" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                

                elif "temperature" in query:
                    search = "temperature in mumbai"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                
                           
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "sleep" in query:
                    speak("Going to sleep,sir")
                    exit()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())

                elif "shutdown system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break

                




                


 