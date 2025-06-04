from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure

class OrderPage(BasePage):
    
    @allure.step("Нажатие на кнопку 'Заказать' в заголовке страницы")
    def click_order_button_top(self):
        self.find_element(MainPageLocators.BUTTON_ORDER_HEADER).click()
    
    @allure.step("Нажатие на кнопку 'Заказать' внизу страницы")
    def click_order_button_bottom(self):
        self.scroll_to_element(MainPageLocators.BUTTON_ORDER_BOTTOM)
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.BUTTON_ORDER_BOTTOM)).click()
    
    @allure.step("Заполнить поле 'Имя'")
    def fill_first_name(self, first_name):
        self.find_element(OrderPageLocators.INPUT_FIRST_NAME).send_keys(first_name)

    @allure.step("Заполнить поле 'Фамилия'")
    def fill_second_name(self, second_name):
        self.find_element(OrderPageLocators.INPUT_SECOND_NAME).send_keys(second_name)
        
    @allure.step("Заполнить поле 'Адрес'")
    def fill_address(self, address):
        self.find_element(OrderPageLocators.INPUT_ADDRESS).send_keys(address)
    
    @allure.step("Выбрать станцию метро")
    def select_metro_station(self, metro_station):
        field_metro = self.find_element(OrderPageLocators.SELECT_METRO_STATION)
        field_metro.click()
        field_metro.send_keys(metro_station)
        self.find_element((By.XPATH, f"//div[@class='select-search__select']//div[text()='{metro_station}']")).click()
        
    @allure.step("Заполнить поле 'Телефон'")
    def fill_phone_number(self, phone_number):
        self.find_element(OrderPageLocators.INPUT_PHONE_NUMBER).send_keys(phone_number)
        
    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.find_element(OrderPageLocators.BUTTON_NEXT).click()
    
    @allure.step("Заполнить поле 'Дата начала аренды'")
    def fill_start_date(self, start_date):
        self.find_element(OrderPageLocators.INPUT_START_DATE).send_keys(start_date)
        self.find_element((By.XPATH, "//div[contains(@class, 'react-datepicker__day--selected')]")).click()
    
    @allure.step("Выбрать период аренды")
    def select_rent_period(self, rent_period):
        self.find_element(OrderPageLocators.SELECT_RENT_REPIOD).click()
        
        period_options = self.find_elements(OrderPageLocators.SELECT_RENTAL_PERIOD_OPTIONS)
        for option in period_options:
            if option.text == rent_period:
                option.click()
                break
        
    @allure.step("Выбрать цвет самоката: черный")
    def select_color_black(self):
        self.find_element(OrderPageLocators.CHECKBOX_COLOR_BLACK).click()
        
    @allure.step("Выбрать цвет самоката: серый")
    def select_color_grey(self):
        self.find_element(OrderPageLocators.CHECKBOX_COLOR_GREY).click()
    
    @allure.step("Заполнить поле 'Комментарий для курьера'")
    def fill_comment(self, comment):
        self.find_element(OrderPageLocators.INPUT_COMMENT).send_keys(comment)
        
    @allure.step("Нажать кнопку 'Назад'")
    def click_back_button(self):
        self.find_element(OrderPageLocators.BUTTON_BACK).click()
    
    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
        self.find_element(OrderPageLocators.BUTTON_ORDER).click()
    
    @allure.step("Нажать кнопку 'Нет' в окне подтверждения заказа")
    def click_no_button(self):
        self.find_element(OrderPageLocators.BUTTON_NO).click()
    
    @allure.step("Нажать кнопку 'Да' в окне подтверждения заказа")
    def click_yes_button(self):
        self.find_element(OrderPageLocators.BUTTON_YES).click()
        
    @allure.step('Получение текста сообщения об успешном заказе')
    def get_order_success_message(self):
        success_message = self.is_element_visible(OrderPageLocators.TITLE_STATUS)
        return success_message.text
        
    @allure.step("Нажать на логотип 'Самокат' в заголовке страницы")
    def click_scooter_logo(self):
        self.find_element(MainPageLocators.LOGO_SCOOTER).click()
    

