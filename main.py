from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
article_count.click()
print(article_count.text)

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# # search_bar = driver.find_element(By.NAME, value='q')
# # print(search_bar.get_attribute('placeholder'))

# button = driver.find_element(By.CSS_SELECTOR, value='.a-price-whole')
# print(button.text)

driver.quit()
