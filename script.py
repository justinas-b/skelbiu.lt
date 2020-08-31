#!/usr/bin/python

import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options, executable_path='chromedriver')

username = sys.argv[1]
password = sys.argv[2]

def renew():
    driver.get ('https://www.skelbiu.lt/users/renew')
    driver.find_element_by_id('nick').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login-button').click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="default_page_content"]/form/button').click()

renew()
