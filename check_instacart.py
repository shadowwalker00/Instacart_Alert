import sys, os, re, requests, time
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
chromedriver = ROOT_DIR + "/AmazonFresh/chromedriver"

# instacart credentials
username = "fake@email"
password = "00000"

# hyper parameter
time_lapse = 2.0

def create_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
    return driver

def terminate(driver):
    driver.quit()

def sound_alert():
    while True:
        os.system('say "Instacart Find Slot GO GET IT"')

def display_time():    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def check_slots():
    print('Creating Chrome Driver ...')
    driver = create_driver()

    print('Logging into Instacart ...')
    driver.get('https://www.instacart.com/#')    
    
    time.sleep(time_lapse)

    driver.find_element_by_tag_name('button').click()
    time.sleep(time_lapse)

    email_field = driver.find_element_by_id('nextgen-authenticate.all.log_in_email')
    email_field.send_keys(username)
    passwd_field = driver.find_element_by_id('nextgen-authenticate.all.log_in_password')
    passwd_field.send_keys(password)        
    driver.find_elements_by_tag_name('button')[2].click()    
    time.sleep(time_lapse * 10)

    

    print('Redirecting to Ralphs ...')
    print('Step 1: Go to cart .....')

    driver.find_elements_by_tag_name('button')[0].click()   
    time.sleep(time_lapse*3)

    print('Step 2: Check out page .....')
    driver.get('https://www.instacart.com/store/checkout_v3')  
    time.sleep(time_lapse*3)
            
    print('Step 3: Collecting delivery availability .....')
    slots_available = False

    while not slots_available:
        no_delivery_image = "https://d2guulkeunn7d8.cloudfront.net/assets/modules/errors/heavy_load-9c583d42cc391f1ade7b077ef715e4c389741570579585b13ee7a27b169905b4.png"
        image_set = set()
        tmp_list = driver.find_elements_by_tag_name('img')
        for item in tmp_list:
            image_set.add(item.get_attribute('src'))

        if no_delivery_image not in image_set:
            slots_available = True          
        
        if slots_available == True:
            print('Slots Available!')
            sound_alert()
            break
        else:
            print('Cur time: {}, No slots available. Sleeping ...'.format(display_time()))
            time.sleep(60)
            driver.refresh()
    
    time.sleep(300)
    terminate(driver)

if __name__ == "__main__":
    print('------ Check  Instacart -------')
    check_slots()