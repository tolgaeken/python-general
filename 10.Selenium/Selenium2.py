from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\Tolga\\AppData\\Local\\SeleniumBasic\\chromedriver.exe")
url = "http://github.com"
driver.get(url)
time.sleep(2)
driver.maximize_window() # Açılan tarayıcıyı tam ekran yapar
# driver.save_screenshot("github.com-homepage.png")
url = "http://github.com/tolgaeken"
driver.get(url)
print(driver.title)
if "tolgaeken" in driver.title:
    driver.save_screenshot("tolgae.png") # Ekran görüntüsü alır
time.sleep(2)
driver.back() # Bir önceki sayfaya gider
# driver.forward() # Bir sonraki sayfaya gider
time.sleep(2)
driver.close()