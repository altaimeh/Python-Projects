import random
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time 
from selenium.webdriver.common.by import By


CHROME_DRIVER_PATH = "/Users/taimeehassan/Documents/chromedriver2"
SIMILAR_ACCOUNT = "umich_photography"
USERNAME = "jujuonthebeat619"
PASSWORD = "12345qwerty"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(4)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        #followers = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a') 
        #followers = int(self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/header/div[2]/ul/li[2]/a/span").text) 
        #followers = self.driver.find_element_by_partial_link_text("followers")
        followers.click()

        time.sleep(2)
        #modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        modal = self.driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/div[2]') 
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            if button.text == 'Follow':
                time.sleep(1)
                button.click()
                rand_time = random.randint(2, 40)
                print(rand_time)
                time.sleep(rand_time)
            #try:
                #button.click()
                #time.sleep(1)
            #except ElementClickInterceptedException:
                #cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                #cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()