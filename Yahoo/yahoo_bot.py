from anticaptchaofficial.recaptchav2proxyless import *
from anticaptchaofficial.imagecaptcha import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent



class YahooBot:
    
    def __init__(self, driver, config) -> None:
        '''
            Initializes the driver and opens the gmail login page
        '''
        options = Options()
        ua = UserAgent()
        user_agent = ua.random
        print(user_agent)

        options.add_argument(f'--user-agent={user_agent}')
        options.add_argument('--headless')
        
        # Class variables
        self.driver = driver
        self.url = "https://mail.yahoo.com/"
        self.page = driver.get(self.url)
        self.config = config['YAHOO']
        self.API_KEY = config['API']['AntiCaptcha']['API_KEY']


    def goto_signin(self):
        '''
            Clicks the Sign In button
        '''
        # Clicking the Sign In button
        signin_button = self.driver.find_element(By.XPATH, self.config['XPATHS']['Click_signin'])
        signin_button.click()

    def enterEmail(self, email):
        '''
            Enters the email address into the input field and clicks the Next button
        '''

        # Entering the email address
        email_input = self.driver.find_element(By.XPATH, self.config['XPATHS']['Email_input'])

        # Type text into the input field using send_keys()
        email_input.send_keys(email)


        # Clicking the Next button
        next_button = self.driver.find_element(By.XPATH, self.config['XPATHS']['Email_next'])
        next_button.click()


    def captchaCheck(self):
        '''
            Checks the type of captcha and returns the type
        '''
        print('Checking for captcha')
        try :
            self.driver.find_element(By.XPATH, self.config['XPATHS']['Recaptcha_sitekey'])
            return 'Recaptcha'
        except:
            try:
                self.driver.find_element(By.XPATH, self.config['XPATHS']['Image_Captcha_image'])
                return 'Image_Captcha'
            except:
                return 'No_Captcha'
            
        
    
    def recaptchaSolver(self):
        '''
            Get the sitekey from the page and solve the recaptcha
        '''
        sitekey = self.driver.find_element(By.XPATH, self.config['XPATHS']['Recaptcha_sitekey']).get_attribute('outerHTML')
        sitekey_clean = sitekey.split('data-site-key="')[1].split('"><div class="eEgeR">')[0]
        print(sitekey_clean)

        solver = recaptchaV2Proxyless()
        solver.set_verbose(1)
        solver.set_key(self.API_KEY)
        solver.set_website_url(self.url)
        solver.set_website_key(sitekey_clean)

        g_response = solver.solve_and_return_solution()

        if g_response!= 0:
            print("g_response"+g_response)
        else:
            print("task finished with error"+solver.error_code)

        test = 'test'
        self.driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')
        time.sleep(5)
        # token_box = self.driver.find_element(By.XPATH, '//*[@id="g-recaptcha-response"]')
        # token_box.send_keys(g_response)

        self.driver.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "'+g_response+'";')

        time.sleep(5)
        self.driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')

        time.sleep(5)

        self.driver.find_element(By.XPATH, self.config['XPATHS']['Recaptcha_next']).click()

    def imageCaptchaSolver(self):
        '''
            Gets the captcha image and solves it
        '''
        captcha_image = self.driver.find_element(By.XPATH, self.config['XPATHS']['Image_Captcha_image'])
        img = captcha_image.screenshot('captcha.png')

        solver = imagecaptcha()
        solver.set_verbose(1)
        solver.set_key(self.API_KEY)

        captcha_text = solver.solve_and_return_solution('captcha.png')
        if captcha_text != 0:
            print ("captcha text "+captcha_text)
        else:
            print ("task finished with error "+solver.error_code)

            
        textbox = self.driver.find_element(By.XPATH, self.config['XPATHS']['Image_Captcha_textbox'])
        textbox.send_keys(captcha_text)

        next_captcha = self.driver.find_element(By.XPATH, self.config['XPATHS']['Image_Captcha_next'])
        next_captcha.click()


    def enterPassword(self, password):
        '''
            Enters the password into the input field and clicks the Next button
        '''
        # Entering the password
        print('Entering the password')
        password_input = self.driver.find_element(By.XPATH, self.config['XPATHS']['Password_input'])
        password_input.send_keys(password)

        # Clicking the Next button
        next_button = self.driver.find_element(By.XPATH, self.config['XPATHS']['Password_next'])
        next_button.click()

        self.driver.quit()

