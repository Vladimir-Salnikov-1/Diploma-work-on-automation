from classes.ApiClass import ApiClass

def test_positive_get_product_card():
    api = ApiClass()
    all_url = api.get_all_url_items_can_buy()
    card = api.get_product_card(all_url[0])
    requared_fields = ["id", "category", "url"]
    for field in requared_fields:
        assert field in card["data"]

def test_psitive_add_item_in_cart():
    api = ApiClass()
    api.delete_cart()
    list_id_items = api.get_all_id_items_can_buy()
    item_1 = int(list_id_items[0])
    api.add_item_in_cart(item_1)
    data_cart = api.go_to_cart()
    id_from_cart = data_cart["products"][0]["goodsId"]
    api.delete_cart()
    assert item_1 == id_from_cart

def test_positive_delete_cart():
    api = ApiClass()
    api.delete_cart()
    list_id_items = api.get_all_id_items_can_buy()
    item_3 = int(list_id_items[2])
    api.add_item_in_cart(item_3)
    data_cart_1 = api.go_to_cart()
    id_from_cart = data_cart_1["products"][0]["goodsId"]
    assert item_3 == id_from_cart
    data_delete = api.delete_cart()
    assert data_delete.status_code == 204
    assert data_delete.reason == 'No Content'
    data_cart_2 = api.go_to_cart()
    assert data_cart_2["products"] == []

def test_positive_add_some_items_in_cart():
    api = ApiClass()
    api.delete_cart()
    list_id_items = api.get_all_id_items_can_buy()
    item_1 = int(list_id_items[2])
    item_2 = int(list_id_items[5])
    item_3 = int(list_id_items[10])
    api.add_item_in_cart(item_1)
    api.add_item_in_cart(item_2)
    api.add_item_in_cart(item_3)
    cart = api.get_short_contents_of_cart()
    assert cart['data']['quantity'] == 3
    list_added_items = [item_1, item_2, item_3]
    for item in list_added_items:
        assert item in cart['data']['items']
    api.delete_cart()

def test_positive_view_short_contents_of_empty_cart():
    api = ApiClass()
    api.delete_cart()
    empty_cart = api.get_short_contents_of_cart()
    assert empty_cart['data']['quantity'] == 0
    assert empty_cart['data']['items'] == []
    



# def test_positive_adding_item_to_cart():
# def test_positive_clear_basket():
# def test_positive_add_multiple_items_to_cart():
# def test_positive_summary_of_empty_cart():

# def test_negative_request_without_token():
# def test_negative_add_cart_list_of_products():
# def test_negative_add_unavailable_item_to_cart():