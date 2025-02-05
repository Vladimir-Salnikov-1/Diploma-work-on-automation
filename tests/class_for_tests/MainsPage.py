from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from DataForTests import DataForTests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
import allure
from selenium.webdriver.remote.webelement import WebElement


class MainsPage:

    def __init__(self):
        self.browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        self.selector_element_input = ".header-search__input"
        self.selector_elements_result_item = "[index]"
        self.selector_element_cart = ".header-cart.sticky-header__controls-item"
        self.selector_anim_load_spin_in_input = ".chg-app-loader"
        self.selector_element_close_input = "[aria-label='Очистить']"
        self.selector_element_search_button = ".header-search__button"
        self.selector_element_message_on_search = ".search-page__found-message"
        self.selector_element_products_list = ".products-list"
        self.selector_element_product_cart = "article"
        self.selector_element_button_of_item = ".button.action-button.blue"
        self.selector_element_title_product = ".product-title__head"
        self.selector_container_empty_result = ".catalog-empty-result__container"
        self.selector_header_empty_result = ".catalog-empty-result__header"
        self.selector_counter_on_cart_icon = ".header-cart__badge"

    def go_to_main_page(self) -> None:
        """Этот метод переходит на главную страницу сайта"""
        self.browser.get(DataForTests.base_url_for_ui)
        allure.attach(DataForTests.base_url_for_ui, "Используемый URL")

    def send_keys_input(self, name: str):
        """Этот метод вводит в поле ввода поиска какое-то значение.
        На вход принимает название товара или автора"""
        with allure.step("Очистить поле ввода"):
            elem_input = self.browser.find_element(
                By.CSS_SELECTOR, self.selector_element_input)
            elem_input.clear()
        with allure.step("Ввести в поле ввода значение"):
            elem_input.send_keys(name)
            allure.attach(name, "Введенное значение")
        with allure.step("Подождать прогрузки необходимых элементов"):
            try:
                WebDriverWait(self.browser, 10, 0.1).until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, self.selector_anim_load_spin_in_input)))
            except TimeoutException:
                print("Спиннер загрузки не появился в течение указанного времени.")
            WebDriverWait(self.browser, 10, 0.1).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, self.selector_element_close_input)))

    def push_button_search(self) -> None:
        """Этот метод нажимает на кнопку поиска в поле ввода."""
        with allure.step("Нажать на кнопку поиска"):
            elem_button_search = self.browser.find_element(
                By.CSS_SELECTOR, self.selector_element_search_button)
            elem_button_search.click()
        with allure.step("Подождать прогрузки необходимых элементов"):
            WebDriverWait(self.browser, 10, 0.1).until(
                EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, self.selector_element_title_product)))

    def get_elements_result_item(self) -> list[WebElement]:
        """Этот метод получает список элементов результата поиска
        внизу, под полем ввода, еще до нажатия на значок поиска"""
        elems = self.browser.find_elements(
            By.CSS_SELECTOR, self.selector_elements_result_item)
        return elems

    def get_list_name_of_result_search(self) -> list[WebElement]:
        """Этот метод получает список элементов названий
        товаров под карточкой товара"""
        list_name = self.browser.find_elements(
            By.CSS_SELECTOR, self.selector_element_title_product)
        return list_name

    def push_button_search_with_unknown_product(self) -> None:
        """Этот метод нажимает на кнопку Найти, когда
        мы ищем заведомо неизвестный товар."""
        with allure.step("Нажать на кнопку поиска"):
            elem_button_search = self.browser.find_element(
                By.CSS_SELECTOR, self.selector_element_search_button)
            elem_button_search.click()
        with allure.step("Подождать прогрузки необходимых элементов"):
            WebDriverWait(self.browser, 10, 0.1).until(
                EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, self.selector_container_empty_result)))

    def get_elements_result_search_unknown_product(self) -> str:
        """Этот метод возвращает значение заголовка контейнера,
        который появляется когда товар не получилось найти"""
        res = self.browser.find_element(
            By.CSS_SELECTOR, self.selector_header_empty_result)
        return res.text

    def get_value_from_cart_icon(self) -> str:
        """Этот метод возвращает значение значка счетчика на значке
        корзины, когда товары присутствуют в ней"""
        res = self.browser.find_element(
            By. CSS_SELECTOR, self.selector_counter_on_cart_icon)
        return res.text

    def get_value_search_from_found_message(self) -> str:
        """Этот метод возвращает значение запроса
        из сообщения о найденных товарах"""
        with allure.step("Получить сообщение о результатах поиска"):
            res = self.browser.find_element(
                By. CSS_SELECTOR, self.selector_element_message_on_search).text
            allure.attach(res, "Полное сообщение")
        with allure.step("Вычленить из сообщения введенное значение в input"):
            match = re.search(r"«(.*?)»", res)
            value_search_from_found_message = match.group(1)
        return value_search_from_found_message

    def get_buttons_buy(self) -> list[WebElement]:
        """Этот метод возвращает все кнопки КУПИТЬ."""
        elements = self.browser.find_elements(
            By.CSS_SELECTOR, self.selector_element_button_of_item)
        buy_buttons = [el for el in elements if el.text.strip() == "КУПИТЬ"]
        return buy_buttons

    def get_product_carts(self) -> list:
        """Этот метод возвращает список карточек продуктов."""
        elements = self.browser.find_elements(
            By.CSS_SELECTOR, self.selector_element_product_cart)
        return elements

    def get_list_of_products(self) -> str:
        """Этот метод возвращает список продуктов."""
        products_list_before = self.browser.find_element(
            By. CSS_SELECTOR, self.selector_element_products_list).text
        return products_list_before

    def get_message_on_the_search_results(self) -> str:
        """Этот метод возвращает текст сообщения данных
        о результатах поиска."""
        message = self.browser.find_element(
            By. CSS_SELECTOR, self.selector_element_message_on_search).text
        return message
