from classes.ApiClass import ApiClass


def test_positive_receiving_a_product_card():
    api = ApiClass()
    request = api.get_all_items()
    assert request is not None


def test_can_buy():
    api = ApiClass()
    id_cun_buy = api.get_all_id_items_can_buy()
    id_1_item = int(id_cun_buy[0])
    req = api.add_item_in_cart(id_1_item)
    cart = api.go_to_cart()
    deli = api.delete_cart()
    
    assert id_cun_buy is not None


# def test_positive_adding_item_to_cart():
# def test_positive_clear_basket():
# def test_positive_add_multiple_items_to_cart():
# def test_positive_summary_of_empty_cart():

# def test_negative_request_without_token():
# def test_negative_add_cart_list_of_products():
# def test_negative_add_unavailable_item_to_cart():