from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def incializarDriver():
    PATH=os.path.abspath(os.getcwd())+"/chromedriver"
    driver=webdriver.Chrome(PATH)
    return driver

if __name__ == '__main__':
    driver=incializarDriver()
    driver.get("https://techwithtim.net")
    print(driver.title)
    search= driver.find_element_by_name("s")
    search.send_keys("Test")
    search.send_keys(Keys.RETURN)

    try:
        main= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"main")))
        articles=main.find_elements_by_tag_name("article")
        for articles in articles:
            header=articles.find_element_by_class_name("entry-summary")
            print(header.text)
        liga=driver.find_element_by_xpath('//*[@id="post-3707"]/header/div/span[1]/a/time[1]')
        liga.click()
        #liga=articles[0].find_elements_by_tag_name("a")

    except Exception as e:
        print(e)
    finally:
        time.sleep(120)
        driver.quit()