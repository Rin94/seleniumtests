import unittest
from selenium import webdriver
import os
from page import MainPage, SearchResultPage

class PythonOrgSeach(unittest.TestCase):
    """
    set up y teardown se ejecuta por cada test
    los test sin el nombre test no se ejecutan en la clase
    assert nos ayuda a validar nuestras pruebas
    Los errores en las pruebas nos dicen en que método fallo
    """
    def setUp(self) -> None:
        PATH=os.path.normpath(os.getcwd() + os.sep + os.pardir)+"/chromedriver"
        print(PATH)
        self.driver=webdriver.Chrome(PATH)
        self.driver.get("http://www.python.org")
    #TODO DEBE EMPEZAR EN TEST
    def test_example(self):
        print("Test")
        assert True

    def test_title(self):
        mainPage=MainPage(self.driver)
        assert mainPage.is_title_matches()

    def test_search_python(self):
        mainPage=MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element="zdkncsndsdsnjdssd"
        mainPage.click_go_button()
        search_result_page=SearchResultPage(self.driver)
        assert  search_result_page.is_results_found()
    def not_work(self):
        print("This wont print")

    def tearDown(self):
        self.driver.implicitly_wait(10)
        self.driver.close()



if __name__ == '__main__':
    unittest.main()