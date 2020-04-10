from win32com.client import Dispatch
import os

speak = Dispatch("SAPI.SpVoice")

def sound_alert_windows(message):
    while True:
        speak.SPeak(message)

def sound_alert_macos(message):
    while True:
        os.system(message)

if __name__=='__main__':
    sound_alert_windows("Instacart Ready to Checkout")

