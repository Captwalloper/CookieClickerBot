import shutil
import os
import sys
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path # this will get you the path variable (it actually does the downloading)

CHROME_DRIVER_OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "chromedriver.exe")
shutil.copy2(binary_path, CHROME_DRIVER_OUTPUT_PATH)

# Quick test
argParser = argparse.ArgumentParser()
argParser.add_argument("-t", "--test", action='store_true', help="Run quick test on chrome driver.")
args = argParser.parse_args()
if (args.test):
    service = Service(CHROME_DRIVER_OUTPUT_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    print("Success! ChromeDriver verified working!")
