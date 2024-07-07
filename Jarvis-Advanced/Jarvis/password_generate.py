import random
import pyttsx3
import datetime
import speech_recognition

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
def pass_generate(l,s,n):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    num=['0','1','2','3','4','5','6','7','8','9']
    sym= ['!','#','$','%','&','*']

    # print("Welcome to password generator")
    # l=int(input("Enter the number of letters in password\n"))
    # s=int(input("Enter the number of symbols in password\n"))
    # n=int(input("Enter the number of numbers in password\n"))

    password_list = []

    for char in range(1, l + 1):
        password_list.append(random.choice(letters))

    for char in range(1, s + 1):
        password_list += random.choice(sym)

    for char in range(1, n + 1):
        password_list += random.choice(num)

    print(password_list)
    random.shuffle(password_list)
    print(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your password is: {password}")
    speak(f"Your password is {password}")
    
    return password
