# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 19:57:00 2022

@author: 18427
"""

#模拟键盘按键输入对在线钢琴 https://www.xiwnn.com/piano/ 的自动演奏
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
import time
from pykeyboard import PyKeyboard

#initialize the chrome driver and open the website
driver = webdriver.Chrome()

driver.get('https://www.xiwnn.com/piano/')
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/menu/a[3]').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/section/div[1]/div[2]/div[3]/div/div/div/div[1]/div/div[3]/button').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/menu/a[1]').click()

#lyrics file reading
ls = []
with open('.\\maple leaf-纯白无小键盘.txt', 'r') as f1:
    lyrics1 = f1.readlines()
for i in lyrics1:
    for j in i:
        ls.append(j)

#performance with win32 api and timer        
k = 0
kb = PyKeyboard()
while k <= 701:
    if ls[k] != ' ' and ls[k] != '\n' :
        kb.press_key(ls[k])
        if ls[k+1] == 'Q':
            time.sleep(0.25)
        elif ls[k+1] == 'B':
            time.sleep(0.5)
        elif ls[k+1] == 'O':
            time.sleep(1)
        elif ls[k+1] == 'T':
            time.sleep(2)
        else:
            pass
        kb.release_key(ls[k])
    elif ls[k] == ' ' and ls[k+1] == 'S':
        time.sleep(0.5)
    elif ls[k] == '\n' and ls[k+1] =='L':
        time.sleep(1)
    else:
        pass
    k+=2
