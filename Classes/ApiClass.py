import requests
from classes.DataForTests import DataForTests


class ApiClass:
    def __init__(self):
        pass
    data = DataForTests()
    
    def get_all_items(self):
        data = DataForTests
        headers = {
            "Authorization": data.access_token,
            "Content-Type": "application/json"
            }
        request = requests.get(data.base_url + "v2/products", headers=headers).json
        return request
        