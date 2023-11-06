from selenium import webdriver

driver = webdriver.Chrome()

response = driver.get('https://www.amazon.com')

print(response)