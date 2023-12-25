from yahoo_bot import YahooBot
import json
from selenium import webdriver
import time
import os

# get current working directory
current_directory = os.path.dirname(__file__)
config_file_path = os.path.join(current_directory, 'config.json')
CONFIG = json.load(open(config_file_path, 'r'))


def main():
    '''
        Main Function that runs the program
    '''
    
    # Getting the driver type from the user
    driver_type = input('Enter the driver type(Web Browser of Choice): ')
    driver_type = driver_type.lower()
    
    email = input('Enter the email address: ')
    password = input('Enter the password: ')
    
    # Creating the driver
    match driver_type:
        case 'chrome':
            driver = webdriver.Chrome()
        case 'firefox':
            driver = webdriver.Firefox()
        case 'edge':
            driver = webdriver.Edge()
        case 'safari':
            driver = webdriver.Safari()
        case _:
            print('Invalid driver type')
    
    # Initializing the gmail_bot class
    bot = YahooBot(driver, CONFIG)
    
    # Going to the login page
    bot.goto_signin()
    
    # Wait for page to load
    time.sleep(5)
    
    # Entering the email address
    bot.enterEmail(email)

    # Wait for page to load
    time.sleep(5)
        
    # Entering the password
    bot.enterPassword(password)
    
    # Wait for page to load
    time.sleep(5)
    
    # Send OTP
    bot.sendOTP()
    
    # Wait for page to load
    time.sleep(5)
    
    # Enter OTP
    bot.enterOTP()
    
    
    
main()

