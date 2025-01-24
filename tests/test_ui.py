from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from DataForTests import DataForTests
from time import sleep
from MainsPage import MainsPage
    
    
def test_result_search():
    main_page = MainsPage()
    main_page.go_to_main_page()
    name = "Происхождение жизни"
    main_page.send_keys_input(name)
    main_page.push_button_search()
    list_item = main_page.get_list_name_of_result_search()
    name_1 = list_item[0].text
    sleep(3)
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
    
def test_search_for_an_unknown_product():
    main_page = MainsPage()
    main_page.go_to_main_page()
    unknown_product = "kf,vfloll."
    main_page.send_keys_input(unknown_product)
    main_page.push_button_search_with_unknown_product()
    elem = main_page.get_elements_result_search_unknown_product()
    assert "Похоже, у нас такого нет" in elem

def test_add_items_in_cart():
    main_page = MainsPage()
    main_page.go_to_main_page()
    name = "Происхождение жизни"
    main_page.send_keys_input(name)
    sleep(3)
    main_page.push_button_search()
    sleep(3)
    main_page.browser.execute_script("window.scrollBy(0, 500);")
    elements = main_page.browser.find_elements(By.CSS_SELECTOR, ".button.action-button blue")
    #buy_buttons = [el for el in elements if el.text.strip() == "КУПИТЬ"]
    elements[0].click
    sleep(5)
    main_page.browser.execute_script("window.scrollBy(0, -500);")
    sleep(5)
    res = main_page.get_value_from_cart_icon()
    
    assert res == 1
        
    
  
