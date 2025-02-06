import openpyxl
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import re, time



def web_search():

    # This function accesses the lottery's page and takes the result.
    options = Options()
    options.add_argument(f'user-agent={UserAgent().random}')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")

    # Input the round, clink the button and get the result.
    search = driver.find_element(By.CLASS_NAME, "gLFyf")
    search.send_keys("temperatura de são paulo")
    search.send_keys(Keys.ENTER)
    time.sleep(10)
    return "Ok"

print(web_search())