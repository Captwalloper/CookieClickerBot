import shutil
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path # this will get you the path variable (it actually does the downloading)

CHROME_DRIVER_OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'chromedriver.exe')
shutil.copy2(binary_path, CHROME_DRIVER_OUTPUT_PATH)

# Quick test
service = Service(CHROME_DRIVER_OUTPUT_PATH)
driver = webdriver.Chrome(service=service)
driver.get("http://www.python.org")
assert "Python" in driver.title
print("Success! ChromeDriver verified working!")
