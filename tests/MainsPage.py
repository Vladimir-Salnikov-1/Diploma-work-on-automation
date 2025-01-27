from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from DataForTests import DataForTests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import TimeoutException
import re


selector_element_input = ".header-search__input"
selector_elements_result_item = "[index]"
selector_element_cart = ".header-cart.sticky-header__controls-item"
selector_anim_load_spin_in_input = ".chg-app-loader"
selector_element_close_input = "[aria-label='Очистить']"
selector_element_search_button = ".header-search__button"
selector_messages_about_found_products = ".search-page__found-message"
selector_element_message_on_search = ".search-page__found-message"
selector_element_products_list = ".products-list"
selector_element_product_cart = "article"
selector_element_button_of_item = ".button.action-button.blue"
selector_element_title_product = ".product-title__head"
selector_container_empty_result = ".catalog-empty-result__container"
selector_header_empty_result = ".catalog-empty-result__header"
selector_counter_on_cart_icon = ".header-cart__badge"


class MainsPage:

    def __init__(self):
        pass
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        self.browser = browser

    def go_to_main_page(self):
        """Этот метод переходит на главную страницу сайта"""
        self.browser.get(DataForTests.base_url_for_ui)

    def send_keys_input(self, name: str):
        """Этот метод вводит в полле ввода поиска какое-то значение.
        На вход принимает название товара или автора"""
        elem_input = self.browser.find_element(
            By.CSS_SELECTOR, selector_element_input)
        elem_input.clear()
        elem_input.send_keys(name)
        try:
            WebDriverWait(self.browser, 10, 0.1).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, selector_anim_load_spin_in_input)))
        except TimeoutException:
            print("Спиннер загрузки не появился в течение указанного времени.")
        WebDriverWait(self.browser, 10, 0.1).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, selector_element_close_input)))

    def push_button_search(self):
        elem_button_search = self.browser.find_element(
            By.CSS_SELECTOR, selector_element_search_button)
        elem_button_search.click()
        WebDriverWait(self.browser, 10, 0.1).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, selector_element_title_product)))

    def get_elements_result_item(self):
        elems = self.browser.find_elements(
            By.CSS_SELECTOR, selector_elements_result_item)
        return elems

    def get_list_name_of_result_search(self):
        list_name = self.browser.find_elements(
            By.CSS_SELECTOR, selector_element_title_product)
        return list_name

    def push_button_search_with_unknown_product(self):
        elem_button_search = self.browser.find_element(
            By.CSS_SELECTOR, selector_element_search_button)
        elem_button_search.click()
        WebDriverWait(self.browser, 10, 0.1).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, selector_container_empty_result)))

    def get_elements_result_search_unknown_product(self):
        res = self.browser.find_element(
            By.CSS_SELECTOR, selector_header_empty_result)
        return res.text

    def get_value_from_cart_icon(self):
        res = self.browser.find_element(
            By. CSS_SELECTOR, selector_counter_on_cart_icon)
        return res.text

    def get_value_search_from_found_message(self):
        """Этот метод возвращает значение запроса
        из сообщения о найденных товарах"""
        res = self.browser.find_element(
            By. CSS_SELECTOR, selector_messages_about_found_products).text
        match = re.search(r"«(.*?)»", res)
        value_search_from_found_message = match.group(1)
        return value_search_from_found_message

    def get_buttons_buy(self):
        elements = self.browser.find_elements(
            By.CSS_SELECTOR, selector_element_button_of_item)
        buy_buttons = [el for el in elements if el.text.strip() == "КУПИТЬ"]
        return buy_buttons

    def get_product_carts(self) -> list:
        elements = self.browser.find_elements(
            By.CSS_SELECTOR, selector_element_product_cart)
        return elements

    def get_list_of_products(self) -> str:
        products_list_before = self.browser.find_element(
            By. CSS_SELECTOR, selector_element_products_list).text
        return products_list_before

    def get_message_on_the_search_results(self) -> str:
        message = self.browser.find_element(
            By. CSS_SELECTOR, selector_element_message_on_search).text
        return message
