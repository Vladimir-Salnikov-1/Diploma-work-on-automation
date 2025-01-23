import requests
from tests.DataForTests import DataForTests
import json


class ApiClass:
    def __init__(self):
        pass

    def add_headers(self):
        """Этот метод добавляет заголовки: 'Authorization' и 'Content-Type'"""
        data = DataForTests
        headers = {
            "Authorization": data.access_token,
            "Content-Type": "application/json"
            }
        return headers
    
    def get_all_items(self) -> dict:
        """Этот метод возвращает все товары"""
        data = DataForTests
        api = ApiClass
        headers = api.add_headers(self)
        request = requests.get(data.base_url + "v2/products", headers=headers).content
        return request

    def get_all_id_items_can_buy(self) -> list:
        """Этот метод возвращает список id всех товаров не в наличии"""
        data = DataForTests
        api = ApiClass
        headers = api.add_headers(self)
        request = requests.get(data.base_url + "v2/products", headers=headers).content
        data = json.loads(request)
        # Получение списка ID товаров с статусом 'canBuy'
        can_buy_ids = [item['id'] for item in data['data'] if item['attributes']['status'] == 'canBuy']
        return can_buy_ids
    
    def get_all_id_items_unavailable(self) -> list:
        """Этот метод возвращает список id всех товаров в наличии"""
        data = DataForTests
        api = ApiClass
        headers = api.add_headers(self)
        request = requests.get(data.base_url + "v2/products", headers=headers).content
        data = json.loads(request)
        # Получение списка ID товаров с статусом 'canBuy'
        can_buy_ids = [item['id'] for item in data['data'] if item['attributes']['status'] == 'preOrder']
        return can_buy_ids
    
    def go_to_cart(self) -> json:
        """Этот метод для попадания в корзину"""
        data = DataForTests
        api = ApiClass
        headers = api.add_headers(self)
        request = requests.get(data.base_url + "v1/cart", headers=headers).text
        data_request = json.loads(request)
        return data_request
    
    def add_item_in_cart(self, id_item):
        """Этот метод для добавления товара в корзину.
        Принимает на вход id товара"""
        data = DataForTests
        api = ApiClass
        headers = api.add_headers(self)
        body = {
                "id": id_item,
                "adData": {
                    "item_list_name": "product-page"
                }
            }
        request = requests.post(data.base_url + "v1/cart/product", headers=headers, json=body)
        return request
    
    def delete_cart(self):
        """Этот метод очищает корзину"""
        data = DataForTests
        api = ApiClass
        headers = api.add_headers(self)
        request = requests.delete(data.base_url + "v1/cart", headers=headers)
        return request
    
    def get_all_url_items_can_buy(self) -> list:
        """Этот метод возвращает список url всех товаров в наличии"""
        data = DataForTests
        api = ApiClass
        headers = api.add_headers(self)
        request = requests.get(data.base_url + "v2/products", headers=headers).content
        data = json.loads(request)
        # Получение списка ID товаров с статусом 'canBuy'
        can_buy_urls = [item['attributes']['url'] for item in data['data'] if item['attributes']['status'] == 'canBuy']
        # Удаление префикса 'product/' из каждого URL
        cleaned_urls = [url[len("product/"):] for url in can_buy_urls]
        return cleaned_urls
    
    def get_product_card(self, product_url) -> json:
        """Этот метод переходит к карточке товара.
        Принимает на вход url товара, возвращает тело ответа в json"""
        data = DataForTests
        api = ApiClass
        headers = api.add_headers(self)
        request = requests.get(data.base_url + "v1/products/slug/" + product_url, headers=headers).text
        data_resp = json.loads(request)
        return data_resp
    
    def get_short_contents_of_cart(self) -> json:
        """Этот метод возвращает краткое содержание корзины"""
        data = DataForTests
        api = ApiClass
        headers = api.add_headers(self)
        request = requests.get(data.base_url + "v1/cart/short", headers=headers).text
        data_resp = json.loads(request)
        return data_resp
