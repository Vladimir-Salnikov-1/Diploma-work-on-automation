import requests
from DataForTests import DataForTests
import json
import allure
from requests.models import Response


class ApiClass:
    def __init__(self):
        self.headers = {
                "Authorization": DataForTests.access_token,
                "Content-Type": "application/json"
                }

    def get_all_items(self) -> dict:
        """Этот метод возвращает все товары"""
        with allure.step("Создать объект класса DataForTests"):
            data = DataForTests()
        with allure.step("Создать запрос на получение всех продуктов"):
            request = requests.get(
                data.base_url_for_api + "v2/products",
                headers=self.headers).content
            allure.attach(str(self.headers), "Передаваемые заголовки")
        return request

    def get_all_id_items_can_buy(self) -> list:
        """Этот метод возвращает список id всех товаров не в наличии"""
        with allure.step("Создать объект класса DataForTests"):
            data = DataForTests()
        with allure.step("Создать запрос на получение списка всех продуктов"):
            request = requests.get(
                data.base_url_for_api + "v2/products",
                headers=self.headers).content
            allure.attach(str(self.headers), "Передаваемые заголовки")
            data = json.loads(request)
        with allure.step("Отфильтровать список, получить ID\
                товаров которые готовы к покупке"):
            can_buy_ids = [item['id'] for item in data[
                'data'] if item['attributes']['status'] == 'canBuy']
        return can_buy_ids

    def get_all_id_items_unavailable(self) -> list:
        """Этот метод возвращает список id всех товаров в наличии"""
        with allure.step("Создать объект класса DataForTests"):
            data = DataForTests()
        with allure.step("Создать запрос на получение списка всех продуктов"):
            request = requests.get(
                data.base_url_for_api + "v2/products",
                headers=self.headers).content
            data = json.loads(request)
            allure.attach(str(self.headers), "Передаваемые заголовки")
        with allure.step("Отфильтровать список, получить ID товаров\
                которые не готовы к покупке"):
            can_buy_ids = [item['id'] for item in data[
                'data'] if item['attributes']['status'] == 'preOrder']
        return can_buy_ids

    def go_to_cart(self) -> json:
        """Этот метод для попадания в корзину,
        возвращает ответ от сервера в json"""
        with allure.step("Создать объект класса DataForTests"):
            data = DataForTests()
        with allure.step("Создать запрос на переход в корзину"):
            request = requests.get(
                data.base_url_for_api + "v1/cart", headers=self.headers).text
            data_request = json.loads(request)
            allure.attach(str(self.headers), "Передаваемые заголовки")
        return data_request

    def add_item_in_cart(self, id_item) -> Response:
        """Этот метод для добавления товара в корзину.
        Принимает на вход id товара"""
        with allure.step("Создать объект класса DataForTests"):
            data = DataForTests()
        with allure.step("Назначить тело запроса"):
            body = {
                    "id": id_item,
                    "adData": {
                        "item_list_name": "product-page"
                    }
                }
        with allure.step("Создать запрос для добавления товара в корзину"):
            request = requests.post(
                data.base_url_for_api + "v1/cart/product",
                headers=self.headers, json=body)
            allure.attach(str(id_item), "Передаваемый ID")
            allure.attach(str(body), "Тело запроса")
            allure.attach(str(self.headers), "Передаваемые заголовки")
        return request

    def delete_cart(self) -> Response:
        """Этот метод очищает корзину"""
        with allure.step("Создать объект класса DataForTests"):
            data = DataForTests()
        with allure.step("Создать запрос для очищения корзины"):
            request = requests.delete(
                data.base_url_for_api + "v1/cart", headers=self.headers)
            allure.attach(str(self.headers), "Передаваемые заголовки")
        return request

    def get_all_url_items_can_buy(self) -> list:
        """Этот метод возвращает список url всех товаров в наличии"""
        with allure.step("Создать объект класса DataForTests"):
            data = DataForTests()
        with allure.step("Создать запрос для получения всех товаров"):
            request = requests.get(
                data.base_url_for_api + "v2/products",
                headers=self.headers).content
            data = json.loads(request)
            allure.attach(str(self.headers), "Передаваемые заголовки")
        with allure.step("Отфильтровать все URL у товаров в наличии"):
            can_buy_urls = [item['attributes']['url'] for item in data[
                'data'] if item['attributes']['status'] == 'canBuy']
        with allure.step("Убрать префикс product/"):
            cleaned_urls = [url[len("product/"):] for url in can_buy_urls]
        return cleaned_urls

    def get_product_card(self, product_url) -> json:
        """Этот метод переходит к карточке товара.
        Принимает на вход url товара, возвращает тело ответа в json"""
        with allure.step("Создать объект класса DataForTests"):
            data = DataForTests()
        with allure.step("Создать запрос для получения карточки товара"):
            request = requests.get(
                data.base_url_for_api + "v1/products/slug/" + product_url,
                headers=self.headers).text
            data_resp = json.loads(request)
            allure.attach(product_url, "Передаваемый URL")
            allure.attach(str(self.headers), "Передаваемые заголовки")
        return data_resp

    def get_short_contents_of_cart(self) -> json:
        """Этот метод возвращает краткое содержание корзины"""
        with allure.step("Создать объект класса DataForTests"):
            data = DataForTests()
        with allure.step("Создать запрос для получения\
                краткого содержания корзины"):
            request = requests.get(
                data.base_url_for_api + "v1/cart/short",
                headers=self.headers).text
            allure.attach(str(self.headers), "Передаваемые заголовки")
        data_resp = json.loads(request)
        return data_resp
