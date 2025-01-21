import requests
from classes.DataForTests import DataForTests
import json


class ApiClass:
    def __init__(self):
        pass

    def add_headers(self):
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
        """Этот метод возвращает список id всех товаров в наличии"""
        data = DataForTests
        api = ApiClass
        headers = api.add_headers(self)
        request = requests.get(data.base_url + "v2/products", headers=headers).content
        data = json.loads(request)
        # Получение списка ID товаров с статусом 'canBuy'
        can_buy_ids = [item['id'] for item in data['data'] if item['attributes']['status'] == 'canBuy']
        return can_buy_ids
    
    def go_to_cart(self):
        data = DataForTests
        api = ApiClass
        headers = api.add_headers(self)
        request = requests.get(data.base_url + "v1/cart", headers=headers)
        return request
        
    #def add_item_in_cart