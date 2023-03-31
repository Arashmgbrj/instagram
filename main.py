from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from tkinter import *
import requests
import re
import time
url = "https://www.instagram.com/"
class page1():
    def __init__(self,url):
        self.url = url
    def bot(self):
        print(self.i1.get())
        print(self.i2.get())
        a = str(requests.get(self.url))
        r_number = re.findall("[0-9]+",a)
        if int(r_number[0]) == 200 :
         self.driver = webdriver.Firefox(executable_path='geckodriver.exe')
         self.driver.maximize_window()
         self.driver.get(self.url)
         self.driver.implicitly_wait(10)
         self.input1 = self.driver.find_element(by=By.NAME , value="username")
         self.input1.send_keys(self.i1.get())
         self.input2 = self.driver.find_element(by=By.NAME,value="password")
         self.input2.send_keys(self.i2.get()+Keys().ENTER)
         self.driver.implicitly_wait(10)
         time.sleep(5)
         self.driver.get('https://www.instagram.com/perspolis/')
         self.driver.implicitly_wait(20)
         time.sleep(5)
         self.driver.find_element(By.CSS_SELECTOR,'#mount_0_0_eQ > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > div.x9f619.xnz67gz.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.xh8yej3.x1gryazu.x10o80wk.x14k21rp.x1porb0y.x17snn68.x6osk4m > section > main > div > header > section > div.x6s0dn4.x78zum5.x1q0g3np.xs83m0k.xeuugli.x1n2onr6 > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xmn8rco.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1i64zmx.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > button').click
        else:
            print("check_network")
    def gui(self):
       w = Tk()
       w.title("instagram_bot_fallow")
       w.config(background="gray")
       l1 = Label(w,text="bot_fallow",font=("mitra",100,"bold"),background="gray",foreground="red")
       l1.grid(row=0,column=0)
       l2 = Label(w,text="username",font=("mitra",20,"bold"),background="gray",foreground="red")
       l3 = Label(w,text="password",font=("mitra",20,"bold"),background="gray",foreground="red")
       self.i1 = Entry(w,width=50)
       self.i2 = Entry(w,width=50)
       self.i1.grid(row=2,column=0)
       self.i2.grid(row=4,column=0)
       l2.grid(row=2,column=4)
       l3.grid(row=4,column=4)
       btn = Button(w,text="click",background="red",foreground="gray",command=self.bot)
       btn.config(padx=100,pady=30,border=20,font=(50))
       btn.grid(row=6,column=0)

       input()
if __name__ == "__main__":
    x = page1(url)
    x.gui()



