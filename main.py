from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=options)
driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys('Alonzo')

# print(article_count.text)

# all_portals = driver.find_element(By.LINK_TEXT, 'All portals')
# all_portals.click()

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# # search_bar = driver.find_element(By.NAME, value='q')
# # print(search_bar.get_attribute('placeholder'))

# button = driver.find_element(By.CSS_SELECTOR, value='.a-price-whole')
# print(button.text)

# driver.quit()
