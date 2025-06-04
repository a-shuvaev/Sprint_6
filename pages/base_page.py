from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from data.urls import Urls
import allure

class BasePage:
    
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.URL_BASE = Urls.BASE_URL
        
    @allure.step("Открытие страницы")
    def open_page(self):
        self.driver.get(self.URL_BASE)
        return self
    
    @allure.step("Поиск элемента по локатору {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step("Поиск элементов по локатору {locator}")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    @allure.step("Проверка, что элемент видим {locator}")
    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
        
    @allure.step("Скроллинг к элементу {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Нажать на логотип Яндекс")
    def click_yandex_logo(self):
        self.find_element(MainPageLocators.LOGO_YANDEX).click()
        
    @allure.step('Ожидание и переключение на новое окно')
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 15).until(
            EC.number_of_windows_to_be(2)
        )
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

    @allure.step('Ожидание перехода на Дзен')
    def wait_for_dzen_redirect(self):
        WebDriverWait(self.driver, 5).until(
            EC.url_contains("dzen.ru")
        )
        return "dzen.ru" in self.driver.current_url




