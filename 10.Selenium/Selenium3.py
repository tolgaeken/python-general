# GitHub Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\\Users\\Tolga\\AppData\\Local\\SeleniumBasic\\chromedriver.exe")
url = "http://github.com"
driver.get(url)
driver.maximize_window()

search = driver.find_element(By.NAME,"q")
# search = driver.find_element_by_name("q")
# search = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]")

time.sleep(1)
search.send_keys("python")
time.sleep(1)

# search.send_keys(Keys.RETURN)
search.send_keys(Keys.ENTER)

time.sleep(1)
# result = driver.page_source
result = driver.find_elements(By.CSS_SELECTOR,".repo-list-item .f4 a")

for element in result:
    print(element.text)

