from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

import pandas as pd
import openpyxl
import os


# driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
driver.get(f'http://www.d2startup.com/portfolio')
time.sleep(2)
elements = driver.find_elements(By.CLASS_NAME, "text_carddesc.eps")

# 텍스트 출력
for element in elements:
    print(element.text)

# driver.quit()
