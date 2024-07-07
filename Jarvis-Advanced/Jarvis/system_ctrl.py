import os
import subprocess
import ctypes

def check_update():
    try:
        print("Checking for updates.......")
        subprocess.run(["powershell","Start-Process","-FilePath","ms-settings:windowsupdate-action","-Wait"])
    except:
        pass
    
def restart(time_delay):
    print("Restarting the system ........")
    os.system(f"shutdown /r /t {time_delay}")
    
def lock():
    ctypes.windll.user32.LockWorkStation()
    
