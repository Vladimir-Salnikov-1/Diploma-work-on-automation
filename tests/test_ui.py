from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from class_for_tests.MainsPage import MainsPage
import allure

long_name_373 = "В целом, конечно, укрепление и развитие внутренней структуры говорит о возможностях новых принципов формирования материально-технической и кадровой базы. Разнообразный и богатый опыт говорит нам, что укрепление и развитие внутренней структуры создаёт необходимость включения в производственный план целого ряда внеочередных мероприятий с учётом комплекса новых предложений."


@allure.epic("Тестирование UI")
@allure.feature("Позитивные проверки")
@allure.title("Найти товар по названию")
@allure.description("В результате теста проверяется что результат поиска\
    совпадает с введенным значением")
@allure.severity("critical")
def test_positive_result_search():
    with allure.step("Создать объект класса MainsPage"):
        main_page = MainsPage()
    with allure.step("Зайти на главную страницу"):
        main_page.go_to_main_page()
    with allure.step("Ввести в поле ввода название книги"):
        name = "Происхождение жизни"
        main_page.send_keys_input(name)
    with allure.step("Нажать на кнопку поиска"):
        main_page.push_button_search()
    with allure.step("Получить название первого товара"):
        list_item = main_page.get_list_name_of_result_search()
        name_1 = list_item[0].text
        allure.attach(name_1, "Название первого товара")
    with allure.step("Проверить что введенное значение есть в названии полученного товара"):
        assert name.lower() in name_1.lower()
    with allure.step("Закрыть браузер"):
        main_page.browser.quit()


@allure.epic("Тестирование UI")
@allure.feature("Позитивные проверки")
@allure.title("Веденное значение равнозначно выпадающим подсказкам")
@allure.description("В результате теста проверяется что при вводе\
    в поле какого-то значения, в выпадающем окне первая подсказка\
        равноценна введенному значению")
@allure.severity("critical")
def test_positive_dropdown_list_results_match_the_entered_value():
    with allure.step("Создать объект класса MainsPage"):
        main_page = MainsPage()
    with allure.step("Зайти на главную страницу"):
        main_page.go_to_main_page()
    with allure.step("Ввести в поле ввода название книги"):
        name = "Происхождение жизни"
        main_page.send_keys_input(name)
    with allure.step("Получить список подсказок из выпадающего списка"):
        res = main_page.get_elements_result_item()
        allure.attach(str(res), "список подсказок")
    with allure.step("Получить значение первой подсказки"):
        name_1 = res[0].text
        allure.attach(name_1, "Значение первой подсказки")
    with allure.step("Проверить что количество подсказок = 4"):
        assert len(res) == 4
    with allure.step("Проверить введенное значение присутствует в первой подсказке"):
        assert name.lower() in name_1.lower()
    with allure.step("Выйти из браузера"):
        main_page.browser.quit()


@allure.epic("Тестирование UI")
@allure.feature("Позитивные проверки")
@allure.title("Найти товар, который отсутствует в системе")
@allure.description("В результате теста проверяется что при поиске\
    несуществующего товара появляется окно с определенным текстом")
@allure.severity("critical")
def test_positive_search_for_an_unknown_product():
    with allure.step("Создать объект класса MainsPage"):
        main_page = MainsPage()
    with allure.step("Зайти на главную страницу"):
        main_page.go_to_main_page()
    with allure.step("Ввести в поле ввода очевидно непонятное значение"):
        unknown_product = "kf,vfloll."
        main_page.send_keys_input(unknown_product)
    with allure.step("Нажать на кнопку поиска"):
        main_page.push_button_search_with_unknown_product()
    with allure.step("Проверить наличие определенного текста"):
        elem = main_page.get_elements_result_search_unknown_product()
        assert "Похоже, у нас такого нет" in elem
    with allure.step("Выйти из браузера"):
        main_page.browser.quit()


@allure.epic("Тестирование UI")
@allure.feature("Позитивные проверки")
@allure.title("Добавить несколько товаров в корзину")
@allure.description("В результате теста проверяется что при добавлении\
    нескольких товаров в корзину, значение счетчика товаров, который\
        расположен на иконке корзины, соответствует количеству\
            добавленных товаров")
@allure.severity("critical")
def test_positive_add_items_in_cart():
    with allure.step("Создать объект класса MainsPage"):
        main_page = MainsPage()
    with allure.step("Зайти на главную страницу"):
        main_page.go_to_main_page()
    with allure.step("Ввести в поле ввода название книги"):
        name = "Происхождение жизни"
        main_page.send_keys_input(name)
    with allure.step("Нажать на кнопку поиска"):
        main_page.push_button_search()
    with allure.step("Нажать на первую кнопку КУПИТЬ"):
        main_page.browser.execute_script("window.scrollBy(0, 500);")
        buy_buttons = main_page.get_buttons_buy()
        buy_buttons[0].click()
        main_page.browser.execute_script("window.scrollBy(0, -500);")
        WebDriverWait(main_page.browser, 10, 0.1).until(
                EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, ".header-cart__badge")))
    with allure.step("Получить значение с счетчика товаров на корзине"):
        res = main_page.get_value_from_cart_icon()
        allure.attach(res, "Значение счетчика")
    with allure.step("Проверить что значение счетчика = 1"):
        assert int(res) == 1
    with allure.step("Выйти из браузера"):
        main_page.browser.quit()


@allure.epic("Тестирование UI")
@allure.feature("Позитивные проверки")
@allure.title("Совпадение искомого значения со значением из\
    сообщения о результатах поиска")
@allure.description("В результате теста проверяется что при поиске\
    определенного товара, введенное значение такое же\
        как значение из сообщения о результате поиска")
@allure.severity("major")
def test_positive_value_in_input_so_value_in_result():
    with allure.step("Создать объект класса MainsPage"):
        main_page = MainsPage()
    with allure.step("Зайти на главную страницу"):
        main_page.go_to_main_page()
    with allure.step("Ввести в поле ввода название книги"):
        name = "апофения"
        main_page.send_keys_input(name)
    with allure.step("Нажать на кнопку поиска"):
        main_page.push_button_search()
    with allure.step("Получить название из сообщения о результатах поиска"):
        value = main_page.get_value_search_from_found_message()
    with allure.step("Проверить что введенное значение = значение из сообщения"):
        assert value == name
    with allure.step("Выйти из браузера"):
        main_page.browser.quit()


@allure.epic("Тестирование UI")
@allure.feature("Негативные проверки")
@allure.title("Вставить в поле ввода очень длинное значение (373 символа)")
@allure.description("В результате теста проверяется что при вводе\
    в поле ввода слишком большого значения, в поле ввода остается\
        только 150 символов")
@allure.severity("minor")
def test_negitive_very_long_value_in_input():
    with allure.step("Создать объект класса MainsPage"):
        main_page = MainsPage()
    with allure.step("Зайти на главную страницу"):
        main_page.go_to_main_page()
    with allure.step("Ввести в поле ввода очень длинное значение (373)"):
        main_page.send_keys_input(long_name_373)
        WebDriverWait(main_page.browser, 10, 0.1).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".result-item__mark")))
    with allure.step("Получить значение подсказки из выпадающего списка"):
        elem = main_page.browser.find_element(
            By.CSS_SELECTOR, ".result-item__mark").text
        len_elem = len(elem)
        allure.attach(str(len(elem)), "Длина значения")
    with allure.step("Проверить что длина значения = 150"):
        assert len_elem == 150, "длина текста не соответствует"
    with allure.step("Выйти из браузера"):
        main_page.browser.quit()


@allure.epic("Тестирование UI")
@allure.feature("Негативные проверки")
@allure.title("Много раз подряд нажать на кнопку поиска")
@allure.description("В результате теста проверяется что при нажатии\
    несколько раз на кнопку поиска, новые товары не добавляются\
        и страница не изменяется")
@allure.severity("minor")
def test_negetive_some_click_on_button_search():
    with allure.step("Создать объект класса MainsPage"):
        main_page = MainsPage()
    with allure.step("Зайти на главную страницу"):
        main_page.go_to_main_page()
    with allure.step("Ввести в поле ввода название книги"):
        name = "апофения"
        main_page.send_keys_input(name)
    with allure.step("Нажать на кнопку поиска"):
        main_page.push_button_search()
    with allure.step("Получить сообщение о результате поиска ДО нескольких нажатий"):
        message_before = main_page.get_message_on_the_search_results()
        allure.attach(message_before, "Сообщение ДО нескольких нажатий")
    with allure.step("Получить число найденных карточек товаров на странице ДО"):
        len_item_before = len(main_page.get_product_carts())
        allure.attach(str(len_item_before), "Сообщение ДО нескольких нажатий")
    with allure.step("Получить список продуктов ДО нескольких нажатий"):
        products_list_before = main_page.get_list_of_products()
        allure.attach(products_list_before,
                      "Список продуктов ДО нескольких нажатий")
    with allure.step("Проверить что введенное значение есть в сообщении о результатах поиска"):
        assert name in message_before
    with allure.step("Нажать на кнопку поиска 10 раз подряд"):
        for push in range(11):
            main_page.push_button_search()
    with allure.step("Получить сообщение о результате поиска ПОСЛЕ нескольких нажатий"):
        message_after = main_page.get_message_on_the_search_results()
        allure.attach(message_after, "Сообщение ПОСЛЕ нескольких нажатий")
    with allure.step("Получить число найденных карточек товаров на странице ПОСЛЕ"):
        len_item_after = len(main_page.get_product_carts())
        allure.attach(str(len_item_after), "Сообщение ПОСЛЕ нескольких нажатий")
    with allure.step("Получить список продуктов ПОСЛЕ нескольких нажатий"):
        products_list_after = main_page.get_list_of_products()
        allure.attach(products_list_after,
                      "Список продуктов ПОСЛЕ нескольких нажатий")
    with allure.step("Проверить что сообщения ДО и ПОСЛЕ одинаковы"):
        assert message_before == message_after, \
            "Сообщение о результате поиска поменялось"
    with allure.step("Проверить что количество карточек ДО и ПОСЛЕ одинаковы"):
        assert len_item_before == len_item_after, "Добавились новые товары"
    with allure.step("Проверить что листы товаров ДО и ПОСЛЕ одинаковы"):
        assert products_list_before == products_list_after, \
            "Поменялся состав товаров"
    with allure.step("Выйти из браузера"):
        main_page.browser.quit()
