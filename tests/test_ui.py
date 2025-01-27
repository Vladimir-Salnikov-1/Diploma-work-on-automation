from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from DataForTests import DataForTests
from time import sleep
from MainsPage import MainsPage

long_name_373 = "В целом, конечно, укрепление и развитие внутренней структуры говорит о возможностях новых принципов формирования материально-технической и кадровой базы. Разнообразный и богатый опыт говорит нам, что укрепление и развитие внутренней структуры создаёт необходимость включения в производственный план целого ряда внеочередных мероприятий с учётом комплекса новых предложений."


def test_result_search():
    main_page = MainsPage()
    main_page.go_to_main_page()
    name = "Происхождение жизни"
    main_page.send_keys_input(name)
    main_page.push_button_search()
    list_item = main_page.get_list_name_of_result_search()
    name_1 = list_item[0].text
    assert name.lower() in name_1.lower()
    main_page.browser.quit()


def test_dropdown_list_results_match_the_entered_value():
    main_page = MainsPage()
    main_page.go_to_main_page()
    name = "Происхождение жизни"
    main_page.send_keys_input(name)
    res = main_page.get_elements_result_item()
    name_1 = res[0].text
    assert len(res) == 4
    assert name.lower() in name_1.lower()
    main_page.browser.quit()


def test_search_for_an_unknown_product():
    main_page = MainsPage()
    main_page.go_to_main_page()
    unknown_product = "kf,vfloll."
    main_page.send_keys_input(unknown_product)
    main_page.push_button_search_with_unknown_product()
    elem = main_page.get_elements_result_search_unknown_product()
    assert "Похоже, у нас такого нет" in elem
    main_page.browser.quit()


def test_add_items_in_cart():
    main_page = MainsPage()
    main_page.go_to_main_page()
    name = "Происхождение жизни"
    main_page.send_keys_input(name)
    main_page.push_button_search()
    main_page.browser.execute_script("window.scrollBy(0, 500);")
    buy_buttons = main_page.get_buttons_buy()
    buy_buttons[0].click()
    main_page.browser.execute_script("window.scrollBy(0, -500);")
    WebDriverWait(main_page.browser, 10, 0.1).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".header-cart__badge")))
    res = main_page.get_value_from_cart_icon()
    assert int(res) == 1
    main_page.browser.quit()


def test_value_in_input_so_value_in_result():
    main_page = MainsPage()
    main_page.go_to_main_page()
    name = "апофения"
    main_page.send_keys_input(name)
    main_page.push_button_search()
    value = main_page.get_value_search_from_found_message()
    assert value == name
    main_page.browser.quit()


def test_negitive_very_long_value_in_input():
    main_page = MainsPage()
    main_page.go_to_main_page()
    main_page.send_keys_input(long_name_373)
    WebDriverWait(main_page.browser, 10, 0.1).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".result-item__mark")))
    elem = main_page.browser.find_element(
        By.CSS_SELECTOR, ".result-item__mark").text
    len_elem = len(elem)
    assert len_elem == 150, "длина текста не соответствует"
    main_page.browser.quit()


def test_negetive_some_click_on_button_search():
    main_page = MainsPage()
    main_page.go_to_main_page()
    name = "апофения"
    main_page.send_keys_input(name)
    main_page.push_button_search()
    message_before = main_page.get_message_on_the_search_results()
    len_item_before = len(main_page.get_product_carts())
    products_list_before = main_page.get_list_of_products()
    assert name in message_before
    
    for push in range(11):
        main_page.push_button_search()
    message_after = main_page.get_message_on_the_search_results()
    len_item_after = len(main_page.get_product_carts())
    products_list_after = main_page.get_list_of_products()
    assert message_before == message_after, "Сообщение о результате поиска поменялось"
    assert len_item_before == len_item_after, "Добавились новые товары"
    assert products_list_before == products_list_after
    main_page.browser.quit()
