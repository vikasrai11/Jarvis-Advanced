import subprocess
from difflib import get_close_matches as find
from os import system
import pyttsx3
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

program=[]
progid=[]
progdict={}
cmd='powershell "gps |where mainwindowtitle |select Description'
cmd1='powershell "gps |where mainwindowtitle |select id'

proc=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
proc1=subprocess.Popen(cmd1,shell=True,stdout=subprocess.PIPE)

for line in proc.stdout:
    st=str(line.decode().rstrip())
    program.append(st)

for line in proc1.stdout:
    st=str(line.decode().rstrip())
    progid.append(st)


for i in range(0,len(progid)):
    progdict[program[i]]=progid[i]


def close(c):
    global program,progid,progdict
    q=find(c,program)
    if q==[]:
        speak("app is not found to close")
    else:
        for key,value in progdict.items():
            if key==q[0]:
                speak(f"{key} is closing")
                system("taskkill /im  "+ str(value))
                speak(f"{key} Terminated successfully.")
