#program to obtain pineApple price for past one year

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time

driver = webdriver.Firefox()
driver.get('https://vazhakulampineapple.in/index.php')

date = datetime.date.today()-datetime.timedelta(days = 364)

for x in range(365):
    date += datetime.timedelta(days = 1)
    if date.weekday() == 0:
        pass
    fdate = date.strftime('%Y-%m-%d')

    a = driver.find_element_by_id('start')
    a.send_keys(fdate)
    b = driver.find_element_by_name('submit')
    b.click()
    time.sleep(5)
    b = driver.find_element_by_css_selector('form')
    fout = b.text.split('\n')

    try:
        dateOut = fout[1][6:]
        priceOut = fout[4][5:]
        valueOut = dateOut+', '+priceOut
        print(valueOut)
    except:
        pass
