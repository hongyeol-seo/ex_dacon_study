from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

import pandas as pd
import openpyxl
import os


driver = webdriver.Chrome()
driver.get(f'http://www.d2startup.com/portfolio')
elements = driver.find_elements(By.CSS_SELECTOR, ".text_carddesc.eps")

# 텍스트 출력
for element in elements:
    print(element.text)

driver.quit()
