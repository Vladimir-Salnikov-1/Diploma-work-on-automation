from tests.class_for_tests.ApiClass import ApiClass
import requests
from DataForTests import DataForTests
import allure


@allure.epic("Тестирование API")
@allure.feature("Позитивные проверки")
@allure.title("Получить карточку товара")
@allure.description("В результате теста проверяется что обязательные поля\
    присутствуют в ответе от сервера в карточе товара")
@allure.severity("critical")
def test_positive_get_product_card():
    with allure.step("Создать объект класса ApiClass"):
        api = ApiClass()
    with allure.step("Получить список всех URL товаров в наличии"):
        all_url = api.get_all_url_items_can_buy()
    with allure.step("Перейти к карточке товара"):
        card = api.get_product_card(all_url[0])
    with allure.step("Назначить обязательные поля"):
        requared_fields = ["id", "category", "url"]
        allure.attach(str(requared_fields), "Обязательные поля")
    with allure.step("Проверить наличие обязательных полей в карточке товара"):
        for field in requared_fields:
            assert field in card["data"]


@allure.epic("Тестирование API")
@allure.feature("Позитивные проверки")
@allure.title("Добавить товар в корзину")
@allure.description("В результате теста проверяется добавление товара в\
    корзину путем проверки чтобы ID\
    добавленного товара и товара в корзине были равны")
@allure.severity("critical")
def test_psitive_add_item_in_cart():
    with allure.step("Создать объект класса ApiClass"):
        api = ApiClass()
    with allure.step("Очистить корзину"):
        api.delete_cart()
    with allure.step("Запросить список id всех товаров не в наличии"):
        list_id_items = api.get_all_id_items_can_buy()
    with allure.step("Выбрать id товара"):
        item_1 = int(list_id_items[0])
        allure.attach(str(item_1), "ID выбранного товара")
    with allure.step("Добавить товар в корзину"):
        api.add_item_in_cart(item_1)
    with allure.step("Перейти в корзину"):
        data_cart = api.go_to_cart()
        id_from_cart = data_cart["products"][0]["goodsId"]
        allure.attach(str(id_from_cart), "ID товара в корзине")
    with allure.step("Очистить корзину"):
        api.delete_cart()
    with allure.step("Проверить что ID совпадают"):
        assert item_1 == id_from_cart


@allure.epic("Тестирование API")
@allure.feature("Позитивные проверки")
@allure.title("Очистить корзину")
@allure.description("В результате теста проверяется что после очистки корзины,\
    при запросе ее содержимого возвращался пустой список")
@allure.severity("critical")
def test_positive_delete_cart():
    with allure.step("Создать объект класса ApiClass"):
        api = ApiClass()
    with allure.step("Очистить корзину"):
        api.delete_cart()
    with allure.step("Запросить список ID товаров в наличии"):
        list_id_items = api.get_all_id_items_can_buy()
    with allure.step("Добавить выбранный товар в корзину"):
        item_3 = int(list_id_items[2])
        api.add_item_in_cart(item_3)
        allure.attach(str(item_3), "ID выбранного товара")
    with allure.step("Запросить данные корзины"):
        data_cart_1 = api.go_to_cart()
        id_from_cart = data_cart_1["products"][0]["goodsId"]
        allure.attach(str(item_3), "ID товара в корзине")
    with allure.step("Проверить что ID товаров сходятся"):
        assert item_3 == id_from_cart
    with allure.step("Очистить корзину"):
        data_delete = api.delete_cart()
        allure.attach(str(data_delete.status_code), "Статус-код")
        allure.attach(str(data_delete.reason), "Контент")
    with allure.step("Проверить что статус-код верен"):
        assert data_delete.status_code == 204
    with allure.step("Проверить что контент ответа от сервера верен"):
        assert data_delete.reason == 'No Content'
    with allure.step("Запросить данные корзины"):
        data_cart_2 = api.go_to_cart()
    with allure.step("Проверить что возвращается пустой список продуктов"):
        assert data_cart_2["products"] == []


@allure.epic("Тестирование API")
@allure.feature("Позитивные проверки")
@allure.title("Добавить несколько товаров в корзину")
@allure.description("В результате теста проверяется что после добавления\
    в корзину нескольких товаров, только эти три товара\
        находятся в корзине")
@allure.severity("critical")
def test_positive_add_some_items_in_cart():
    with allure.step("Создать объект класса ApiClass"):
        api = ApiClass()
    with allure.step("Очистить корзину"):
        api.delete_cart()
    with allure.step("Запросить ID товаров в наличии"):
        list_id_items = api.get_all_id_items_can_buy()
    with allure.step("Добавить в корзину первый товар"):
        item_1 = int(list_id_items[2])
        api.add_item_in_cart(item_1)
    with allure.step("Добавить в корзину второй товар"):
        item_2 = int(list_id_items[5])
        api.add_item_in_cart(item_2)
    with allure.step("Добавить в корзину третий товар"):
        item_3 = int(list_id_items[10])
        api.add_item_in_cart(item_3)
    with allure.step("Запросить краткое содержание корзины"):
        cart = api.get_short_contents_of_cart()
    with allure.step("Проверить в корзине число товаров\
            соответствует добавленному"):
        assert cart['data']['quantity'] == 3
    with allure.step("проверить что ID добавленных товаров в корзине\
            соответствуют тому что находится в корзине"):
        list_added_items = [item_1, item_2, item_3]
        for item in list_added_items:
            assert item in cart['data']['items']
    with allure.step("Очистить корзину"):
        api.delete_cart()


@allure.epic("Тестирование API")
@allure.feature("Позитивные проверки")
@allure.title("Посмотреть краткое содержание корзины")
@allure.description("В результате теста проверяется в ответе на запрос\
    краткого содержания пустой корзины, приходит что число товаров 0\
        , а в списке товаров - возвращается пустой список")
@allure.severity("critical")
def test_positive_view_short_contents_of_empty_cart():
    with allure.step("Создать объект класса ApiClass"):
        api = ApiClass()
    with allure.step("Очистить корзину"):
        api.delete_cart()
    with allure.step("Запросить краткое содержание корзины"):
        empty_cart = api.get_short_contents_of_cart()
    with allure.step("Проверить что в количестве товаров приходит 0"):
        assert empty_cart['data']['quantity'] == 0
    with allure.step("Проверить что приходит пустой список товаров"):
        assert empty_cart['data']['items'] == []


@allure.epic("Тестирование API")
@allure.feature("Негативные проверки")
@allure.title("Добавить несколько товаров в корзину списком")
@allure.description("В результате теста проверяется при попытке добавить\
    несколько товаров списком приходит соответствующий статус-код\
        и операция не выполняется")
@allure.severity("critical")
def test_negative_add_some_items_in_cart_onetime():
    with allure.step("Создать объект класса ApiClass"):
        api = ApiClass()
    with allure.step("Запросить список ID товаров в наличии"):
        id_items = api.get_all_id_items_can_buy()
    with allure.step("Создать запрос на добавление в корзину\
            нескольких товаров списком"):
        list_add_items = [int(id_items[0]), int(id_items[2]), int(id_items[5])]
        request = api.add_item_in_cart(list_add_items)
    with allure.step("Проверить что статус-код ответа - 400"):
        assert request.status_code == 400


@allure.epic("Тестирование API")
@allure.feature("Негативные проверки")
@allure.title("Отправить запрос без токена")
@allure.description("В результате теста проверяется что при попытке\
    отправить запрос без токена запрос не отправляется")
def test_negative_respons_without_token():
    with allure.step("Создать запрос на переход на главную страницу сайта\
            без добавления токена"):
        data_cart = requests.get(DataForTests.base_url_for_api + "v1/cart")
        allure.attach(str(data_cart.status_code), "Статус-код ответа")
        allure.attach(str(data_cart.reason), "Сообщение ошибки")
    with allure.step("Проверить что статус код равен ожидаемому"):
        assert data_cart.status_code == 401
    with allure.step("Проверить что сообщение ошибки равно ожидаемому"):
        assert data_cart.reason == 'Unauthorized'


@allure.epic("Тестирование API")
@allure.feature("Негативные проверки")
@allure.title("Добавить в корзину недоступный товар")
@allure.description("В результате теста проверяется что при попытке\
    добавить недоступный товар в корзину запрос не выполняется")
def test_negative_add_in_cart_unavailable_item():
    with allure.step("Создать объект класса ApiClass"):
        api = ApiClass()
    with allure.step("Очистить корзину"):
        api.delete_cart()
    with allure.step("Создать запрос на добавление в корзину товара\
            недоступного к покупке"):
        request = api.add_item_in_cart(2389708)
        allure.attach("2389708", "ID недоступного к покупке товара")
        allure.attach(str(request.status_code), "Статус-код ответа")
    with allure.step("Проверить что статус-код ответа\
            соответствует ожидаемому"):
        assert request.status_code == 422
    with allure.step("Проверить что товар не добавился в корзину"):
        with allure.step("Запросить краткое содержание корзины"):
            cart = api.get_short_contents_of_cart()
            allure.attach(
                str(cart['data']['quantity']), "количество товаров в корзине")
        with allure.step("Проверить что товар не добавился в корзину"):
            assert cart['data']['quantity'] == 0
