from giris_bilgileri import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class X:
    def __init__(self, username, password):
        self.browser = webdriver.Edge()
        self.username = username
        self.password = password
    
    def signIn(self):
            self.browser.get("https://x.com/i/flow/login")
            time.sleep(5)

            username_input = self.browser.find_element(By.NAME, 'text')
            username_input.send_keys(self.username)
            time.sleep(3)
            username_input.send_keys(Keys.RETURN)
            time.sleep(3)
            
            password_input = self.browser.find_element(By.NAME, "password")
            password_input.send_keys(self.password)
            time.sleep(3)
            password_input.send_keys(Keys.RETURN)  
            time.sleep(5)
#hastag arama
    def searchHashtag(self, hashtag):
            time.sleep(3)
            searchInput = self.browser.find_element(By.XPATH, '//input[@aria-label="Search query"]')
            searchInput.send_keys(f"#{hashtag}")
            time.sleep(2)
            searchInput.send_keys(Keys.RETURN)
            time.sleep(3)
            print(f"#{hashtag} etiketi arandı.")

while True:
    bot = X(username, password)
    bot.signIn()
    bot.searchHashtag("#Aramak istenen hashtag buraya yazın.")
    input("Kapatmak için Enter'a basınız:")
    bot.browser.quit()