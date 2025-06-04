from pages.order_page import OrderPage
from data.urls import Urls
import allure
import pytest

class TestLogos:
    
    @allure.title("Проверка клика на логотип Яндекс")
    def test_click_yandex_logo(self, driver):
        logos_page = OrderPage(driver)
        logos_page.open_page()
        
        logos_page.click_yandex_logo()
        logos_page.switch_to_new_window()
        
        assert logos_page.wait_for_dzen_redirect()
        
    @allure.title("Проверка клика на логотип Самокат")
    def test_click_scooter_logo(self, driver):
        logos_page = OrderPage(driver)
        logos_page.open_page()
        logos_page.click_order_button_top()
        
        logos_page.click_scooter_logo()
        actual_url = logos_page.get_current_url()
        expected_url = Urls.BASE_URL
        
        assert actual_url == expected_url