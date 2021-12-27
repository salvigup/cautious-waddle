from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# driver.maximize_window()

url = "https://www.amazon.in/HP-23-8-Inch-Wireless-Keyboard-24-df1669in/dp/B09JZCL3R8"
home_url = "https://www.amazon.in"

driver.get(home_url)

search_box = driver.find_element(By.NAME, 'field-keywords')
search_box.send_keys('Asus Laptop', Keys.ENTER)
print(driver.title)
rows = driver.find_elements(By.XPATH, "//h2[@id='issreftag")

for item in rows:
    print(item.text)

# try:
#    ele = driver.find_element(By.TAG_NAME, 'h1')
#    print(ele.text)
# except Exception as e:
#    print(e)

driver.close()

