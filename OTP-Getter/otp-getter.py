from selenium import webdriver

USERNAME_XPATH = "/html/body/div[1]/div/div/form/div[1]/input"
USERNAME = 'g001'
PW_XPATH = "/html/body/div[1]/div/div/form/div[2]/input"
PW = 'g1234'

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the URL
driver.get("http://acl-1.wi-ya.net/Login/")

# Get the username textbox
username = driver.find_element_by_xpath(USERNAME_XPATH)
username.send_keys(USERNAME)

# Get the password textbox
password = driver.find_element_by_xpath(PW_XPATH)
password.send_keys(PW)


