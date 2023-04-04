from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

import pandas as pd
import openpyxl
import os

query = "네이버 mou"
url_template = "https://www.google.com/search?q={}&tbm=nws&start={}"

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
# driver.maximize_window()

data = []
for page in range(0, 10):
    url = url_template.format(query, page)
    driver.get(url)
    time.sleep(5)  # 페이지 로딩을 위해 5초 대기
    articles = driver.find_elements(
        By.CLASS_NAME, 'mCBkyc.ynAwRc.MBeuO.nDgy9d')
    print(f'-------------{page}page---------------')
    for i in articles:
        print(i.text)
        data.append([i.text])  # 데이터 추가

driver.quit()

file_name = time.strftime("%Y%m%d_%H%M%S") + '.xlsx'  # 현재 시간 정보를 이용하여 파일 이름 생성
# path = os.path.join(r'C:\Users\seo\Desktop', file_name)  # 폴더 경로와 파일 이름 결합
path = os.path.join(r'C:\Users\PC\Desktop', file_name)  # 폴더 경로와 파일 이름 결합

try:
    df = pd.read_excel(path, sheet_name='sheet1')  # 기존 데이터 읽기
    df = pd.concat([df, pd.DataFrame(data, columns=['text'])],
                   ignore_index=True)  # 새로운 데이터 추가

except FileNotFoundError:
    df = pd.DataFrame(data, columns=['text'])  # 데이터프레임 생성
    with pd.ExcelWriter(path) as writer:
        df.to_excel(writer, sheet_name='sheet1', index=False)

with pd.ExcelWriter(path, engine='openpyxl', mode='a') as writer:
    df.to_excel(writer, sheet_name='sheet1', index=False,
                header=not writer.sheets['sheet1'])
