from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time
PATH = "C:\webdriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://192.168.2.1")
print(driver.title)

namauser = driver.find_element_by_name("User")
namauser.send_keys("admin")

paswot = driver.find_element_by_name("Passwd")
paswot.send_keys("Th3w33l123")
paswot.send_keys(Keys.RETURN)

time.sleep(1)

driver.get("http://192.168.2.1/management/reboot.asp")
print(driver.title)

try:
    element = WebDriverWait(driver,1).until(
        EC.presence_of_element_located((By.ID,"reboot_apply"))
    )
    element.click()
    alert = WebDriverWait(driver,1).until(
        EC.alert_is_present()
    )
    alert.accept()
    time.sleep(1)
    driver.quit()
    
except:
    #WebDriverWait(webdriver, 5).until(EC.alert_is_present())
    #webdriver.switch_to_alert.accept()
    driver.quit()