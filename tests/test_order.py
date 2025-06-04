from pages.base_page import BasePage
from pages.order_page import OrderPage
from data.order import ORDER_DATA
import allure
import pytest

class TestOrder:
    
    @allure.title("Проверка возможности оформления заказа через кнопку 'Заказать' в заголовке страницы")
    @pytest.mark.parametrize('test_data', ORDER_DATA)
    def test_order_via_header_button(self, driver, test_data):
        order_page = OrderPage(driver)
        order_page.open_page()
        
        order_page.click_order_button_top()
        order_page.fill_first_name(test_data['first_name'])
        order_page.fill_second_name(test_data['second_name'])
        order_page.fill_address(test_data['address'])
        order_page.select_metro_station(test_data['metro_station'])
        order_page.fill_phone_number(test_data['phone_number'])
        
        order_page.click_next_button()
        
        order_page.fill_start_date(test_data['start_date'])
        order_page.select_rent_period(test_data['rent_period'])
        if test_data['color'] == 'black':
            order_page.select_color_black()
        elif test_data['color'] == 'grey':
            order_page.select_color_grey()
            
        order_page.fill_comment(test_data['comment'])
        
        order_page.click_order_button()
        order_page.click_yes_button()
        
        assert "Заказ оформлен" in order_page.get_order_success_message()
        
        
    @allure.title("Проверка возможности оформления заказа через кнопку 'Заказать' внизу страницы")
    @pytest.mark.parametrize('test_data', ORDER_DATA)
    def test_order_via_bottom_button(self, driver, test_data):
        order_page = OrderPage(driver)
        order_page.open_page()

        order_page.click_order_button_bottom()
        order_page.fill_first_name(test_data['first_name'])
        order_page.fill_second_name(test_data['second_name'])
        order_page.fill_address(test_data['address'])
        order_page.select_metro_station(test_data['metro_station'])
        order_page.fill_phone_number(test_data['phone_number'])

        order_page.click_next_button()

        order_page.fill_start_date(test_data['start_date'])
        order_page.select_rent_period(test_data['rent_period'])

        if test_data['color'] == 'black':
            order_page.select_color_black()
        elif test_data['color'] == 'grey':
            order_page.select_color_grey()

        order_page.fill_comment(test_data['comment'])

        order_page.click_order_button()
        order_page.click_yes_button()

        assert "Заказ оформлен" in order_page.get_order_success_message()