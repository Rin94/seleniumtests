from selenium import webdriver
import os
import time
from selenium.webdriver.common.action_chains import ActionChains


def primerejemplo():
    PATH=os.path.abspath(os.getcwd()) + "/chromedriver"
    driver=webdriver.Chrome(PATH)
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    element=driver.find_element_by_id("bigCookie")
    n=0
    while(n<1100):
        element.click()
        n = n + 1
        time.sleep(0.1)

    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    PATH=os.path.abspath(os.getcwd()) + "/chromedriver"
    driver=webdriver.Chrome(PATH)
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    driver.implicitly_wait(5)#espera la siguiente linea hasta que haya pasado el tiempo
    cookie=driver.find_element_by_id("bigCookie")
    cookie_count=driver.find_element_by_id("cookies")
    #crear un arreglo al reve con los objetos de productos
    items=[driver.find_element_by_id("productPrice"+str(i)) for i in range(1,-1,-1)]
    print(items)

    actions=ActionChains(driver)
    actions.click(cookie)

    for i in range(5000):
        actions.perform()
        count=int(cookie_count.text.split(" ")[0])
        for item in items:
            value=int(item.text)

            if value<=count:
                upgrade_actions=ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()
                items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

    time.sleep(10)
    driver.quit()




