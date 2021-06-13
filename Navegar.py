import time

from selenium import webdriver
from Selebi import Selebi
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

if __name__ == '__main__':
    PATH = os.path.abspath(os.getcwd()) + "/chromedriver"
    driver=webdriver.Chrome(PATH)
    driver.get("https://techwithtim.net/")
    try:
        link=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Start Programming!")))
        #link.clear() #clear input boxes
        link.click()
        link=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="panel-22-1-0-0"]/figure/a')))
        link.click()
        link=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="panel-146-0-0-0"]/figure/a')))
        link.click()
        link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sow-button-19310003")))
        link.click()
        time.sleep(10)
        driver.back()#regresar a anterior
        driver.back()
        driver.back()
        driver.back()
        time.sleep(15)
        driver.forward()
        driver.forward()

    except Exception as e:
        print(e)
    finally:
        time.sleep(15)
        driver.quit()