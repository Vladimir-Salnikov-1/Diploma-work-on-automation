from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from DataForTests import DataForTests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


selector_element_input = ".header-search__input"
selector_elements_result_item = "[index]"
selector_element_cart = ".header-cart.sticky-header__controls-item"


class MainsPage:
    
    def __init__(self):
        pass
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser = browser
        
    def go_to_main_page(self):
        """Этот метод переходит на главную страницу сайта"""
        self.browser.get(DataForTests.base_url_for_ui)
        
    def send_keys_input(self, name: str):
        """Этот метод вводит в полле ввода поиска какое-то значение.
        На вход принимает название товара или автора"""
        elem_input = self.browser.find_element(By.CSS_SELECTOR, selector_element_input)
        elem_input.clear()
        elem_input.send_keys(name)
        sleep(1)
        
        
    def push_button_search(self):
        elem_button_search = self.browser.find_element(By.CSS_SELECTOR, ".header-search__button")
        elem_button_search.click()
        WebDriverWait(self.browser, 10, 0.1).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".product-title__head")))
       
    
    def get_elements_result_item(self):
        elems = self.browser.find_elements(By.CSS_SELECTOR, selector_elements_result_item)
            
        return elems
    
    def get_list_name_of_result_search(self):
        list_name = self.browser.find_elements(By.CSS_SELECTOR, ".product-title__head")
        return list_name
    
    def push_button_search_with_unknown_product(self):
        elem_button_search = self.browser.find_element(By.CSS_SELECTOR, ".header-search__button")
        elem_button_search.click()
        WebDriverWait(self.browser, 10, 0.1).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".catalog-empty-result__container")))
        
    def get_elements_result_search_unknown_product(self):
        res = self.browser.find_element(By.CSS_SELECTOR, ".catalog-empty-result__header")
        return res.text
        
    
    
        
        
