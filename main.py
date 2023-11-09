from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=options)
driver.get('https://www.amazon.com/Instant-Pot-Duo-Mini-Programmable/dp/B06Y1YD5W7/ref=sr_1_1?crid=3KMPX3FO5TROQ&keywords=instant%2Bpot&qid=1699949602&sprefix=instant%2Bpot%2Caps%2C116&sr=8-1&th=1')

price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
print(f"The price is {price_dollar.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, value='q')
print(search_bar.tag_name)

driver.quit()
