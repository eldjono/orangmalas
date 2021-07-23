from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time

class MyBot:
    def __init__(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        PATH = "C:\webdriver\chromedriver.exe"
        self.driver = webdriver.Chrome(
            executable_path=PATH, 
            options=self.options)
        self.driver.get("http://192.168.2.1")
        namauser = self.driver.find_element_by_name("User")
        namauser.send_keys("user")
        paswot = self.driver.find_element_by_name("Passwd")
        paswot.send_keys("user123456")
        paswot.send_keys(Keys.RETURN)
        time.sleep(1)
        self.driver.get("http://192.168.2.1/management/reboot.asp")
        print(self.driver.title)
        element = WebDriverWait(self.driver,1).until(
            EC.presence_of_element_located((By.ID,"reboot_apply"))
        )
        element.click()
        alert = WebDriverWait(self.driver,1).until(
            EC.alert_is_present()
        )
        alert.accept()
        time.sleep(1)
    
MyBot()