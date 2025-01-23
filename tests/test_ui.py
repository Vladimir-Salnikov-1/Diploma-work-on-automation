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
    main_page.send_keys_input("Происхождение жизни")
    main_page.push_button_search()
    list_item = main_page.get_list_name_of_result_search()
    name_1 = list_item[0].text
    sleep(3)
    assert "Происхождение жизни" in name_1
    main_page.browser.quit()

def test_dropdown_list_results_match_the_entered_value():
    main_page = MainsPage()
    main_page.go_to_main_page()
    main_page.send_keys_input("Происхождение жизни")
    res = main_page.get_elements_result_item()
    name_1 = res[0].text
    assert len(res) == 4
    assert "роисхождение жизни" in name_1
    
def test_search_for_an_unknown_product():
    main_page = MainsPage()
    main_page.go_to_main_page()
    unknown_product = "kf,vfloll."
    main_page.send_keys_input(unknown_product)
    main_page.push_button_search_with_unknown_product()
    elem = main_page.get_elements_result_search_unknown_product()
    assert "Похоже, у нас такого нет" in elem
