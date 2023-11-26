import gmail_bot
import json
from selenium import webdriver
import time

CONFIG = json.load(open('config.json', 'r'))


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
    gmailBot = gmail_bot.GMAIL(driver, CONFIG)
    
    gmailBot.enterEmail(email)

    # Wait for page to load
    time.sleep(5)

    
    # Checking the type of captcha and solving it  
    captcha_type =  gmailBot.captchaCheck()
    # captcha_type = 'Image_Captcha'
    print(captcha_type)
    while captcha_type != 'No_Captcha':
        if captcha_type == 'Recaptcha':
            gmailBot.recaptchaSolver()
        elif captcha_type == 'Image_Captcha':
            gmailBot.imageCaptchaSolver()
        
        
        # Wait for page to load
        print('sleeping')
        time.sleep(5)    
        captcha_type =  gmailBot.captchaCheck()
        break
        
        
    # Entering the password
    gmailBot.enterPassword(password)
    
    
    
main()

