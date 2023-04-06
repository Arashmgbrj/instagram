from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from tkinter import *
from pynput.mouse import Button, Controller
import requests
import re
import time
url = "https://www.instagram.com/accounts/login/"
class page1():
    def __init__(self,url):
        self.url = url
    def bot(self):
     a = str(requests.get(self.url))
     r_number = re.findall("[0-9]+",a)
     if int(r_number[0]) == 200 :
      self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
      self.driver.maximize_window()
      self.driver.get(self.url)
      self.driver.implicitly_wait(10)
      self.input1 = self.driver.find_element(by=By.NAME , value="username")
      self.input1.send_keys("marketingofweb")
      self.input2 = self.driver.find_element(by=By.NAME,value="password")
      self.input2.send_keys("arashmg1382"+Keys().ENTER)
      self.driver.implicitly_wait(10)
      time.sleep(10)
      for i in range(0,3):
       self.driver.get("https://www.instagram.com/explore/people/")
       time.sleep(12)
       print("yes")
     else:
      print("check_network")
if __name__ == "__main__":
    x = page1(url)
    x.bot()
