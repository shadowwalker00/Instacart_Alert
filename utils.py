import os, sys
from datetime import datetime
from selenium import webdriver
os_name = sys.platform

if 'win32' == sys.platform:
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    def sound_alert_windows(message):
        while True:
            speak.SPeak(message)

def sound_alert_macos(message):
    while True:
        os.system(message)

def display_time():    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def create_driver():
    chromedriver = "./chromedriver"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chromedriver, options=chrome_options)
    return driver

def terminate(driver):
    driver.quit()

def error_alert():
    while True:
        os.system('say "Whole Food ERROR"')


if __name__=='__main__':
    sound_alert_macos("say 'Instacart Ready to Checkout'")
    # print(sys.platform)

