import time
from selenium import webdriver
import os
from dataclasses import dataclass

#@dataclass
class Selebi:

    def inicializarSelenium(self,PATH):
        if PATH=="" or PATH==None:
            PATH = os.path.abspath(os.getcwd()) + "/chromedriver"
        return webdriver.Chrome(PATH)

    def __del__(self):
        print("deleted")

    def detenerSelenium(self,seconds,driver):
        time.sleep(seconds)
        driver.quit()

