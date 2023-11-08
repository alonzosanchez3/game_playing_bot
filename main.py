from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=options)
driver.get('https://www.amazon.com')
