from  locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    #es de la clase locator
    locator="q"



class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

class MainPage(BasePage):
    #hide behevior

    search_text_element=SearchTextElement()
    def is_title_matches(self):
        return "Welcome to Python.org"== self.driver.title

    def click_go_button(self):
        #trabajar con tuplas *(1,2) los separa en dos argumentos
        element=self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source