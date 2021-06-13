from  selenium import webdriver
from selenium.webdriver.common.keys import Keys #GIVES US ACCESS TO KEY
import time
#put the path of chromedriver
PATH= "/Users/jared/PycharmProjects/SeleniumTest/chromedriver"

#Select webdriver
driver=webdriver.Chrome(PATH)

#get the uri
driver.get("http://localhost:8000/")

#acceder a diferentes parametros por tipo, id, clase, nombre, classname
search=driver.find_element_by_id("servicios")
search.click()

titulo=driver.find_element_by_id("id_titulo")
titulo.send_keys("PRO")

boton=driver.find_element_by_name("filtrar")
boton.send_keys(Keys.ENTER)
#print(driver.page_source)
time.sleep(5)
driver.quit()
imprimirNumeros= lambda a,b: print(a+b)
imprimirNumeros(5,7)
