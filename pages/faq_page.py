from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class FAQPage(BasePage):
    
    @allure.step("Открыть страницу")
    def open_page(self):
        self.driver.get(self.URL_BASE)
        return self
    
    @allure.step("Скролл до меню FAQ")
    def scroll_to_faq_menu(self):
        self.scroll_to_element(MainPageLocators.FAQ_MENU)
        
    @allure.step("Нажать на вопрос FAQ {question_locator}")
    def get_faq_text(self, question_locator, answer_locator):
        question_text = self.find_element(question_locator).text
        self.find_element(question_locator).click()
        self.is_element_visible(answer_locator)
        answer_text = self.find_element(answer_locator).text
        
        return question_text, answer_text
    
    