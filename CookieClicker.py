import os
import re
import locale
from enum import StrEnum
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from Saves.SaveGame import Load as LoadSave
from ChromeDriver.InstallChromeDriver import CHROME_DRIVER_OUTPUT_PATH

class Id(StrEnum):
    ENGLISH = "langSelect-EN"
    BIG_COOKIE = "bigCookie"
    NUM_COOKIES = "cookies"
    STORE = "storeTitle"
    OPTIONS_MENU = "menu"
    IMPORT_SAVE_PROMPT = "promptContentImportSave"

class Good:
    def __init__(self, name: str, price: str, element: WebElement):
        self.name = name
        self.price = price
        self.element = element
    def __repr__(self):
        return f'{self.name} {self.price}'
    def Buy(self):
        self.element.click()

class CookieClicker:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        options = Options()
        options.add_argument("--start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging']) # remove log spam
        self.driver = webdriver.Chrome(chrome_options = options, service=Service(CHROME_DRIVER_OUTPUT_PATH))
    def Launch(self):
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")
        self.__Wait_for(Id.ENGLISH)
        self.__Click(Id.ENGLISH)
        self.__Wait_for(Id.STORE)
        self.__Wait_for(Id.BIG_COOKIE)
    def Close(self):
        self.driver.close()
    def Load(self):
        save_data = LoadSave()
        self.driver.find_element(By.CSS_SELECTOR, "div.subButton").click() # open options menu
        self.__Wait_for(Id.OPTIONS_MENU)
        self.driver.find_element(By.CSS_SELECTOR, "a[onclick^='Game.Import'").click()
        self.__Wait_for(Id.IMPORT_SAVE_PROMPT)
        self.driver.find_element(By.ID, "textareaPrompt").send_keys(save_data)
        self.driver.find_element(By.ID, "promptOption0").click()
        self.__Wait_for(Id.BIG_COOKIE)
    def PatrolGoldenCookie(self):
        self.driver.execute_script("""
            for (let h in Game.shimmers) {
                if(Game.shimmers[h].type=="golden") {
                    Game.shimmers[h].pop();
                }
            }
        """)
    def SpamClick(self, num):
        self.__Click(Id.BIG_COOKIE, num)
    def GetProducts(self):
        products = self.driver.find_elements(By.CSS_SELECTOR, "button.product.unlocked.enabled")
        goods = map(lambda p: (
                Good(p.find_element(By.CSS_SELECTOR, ".productName").text, p.find_element(By.CSS_SELECTOR, ".price").text, p)
            ),
            products
        )
        return list(goods)
    def GetUpgrades(self):
        upgrades = self.driver.find_elements(By.CSS_SELECTOR, "button.crate.upgrade.enabled")
        goods = map(lambda p: (
                Good("unknown", "-1", p)
            ),
            upgrades
        )
        return list(goods)
    def GetNumCookies(self):
        label = self.driver.find_element(By.ID, Id.NUM_COOKIES).text
        return locale.atoi(re.search(r'\d+', label).group())
    def __Click(self, id, num = 1):
        self.driver.find_element(By.ID, id).click()
    def __Wait_for(self, id):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
        except:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
