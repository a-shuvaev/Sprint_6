from data.faq import FAQ_DATA
from pages.faq_page import FAQPage
import allure
import pytest

class TestFAQ:
    
    @allure.title("Проверка секции FAQ")
    @pytest.mark.parametrize('faq_data', FAQ_DATA)
    def test_faq_section(self, driver, faq_data):
        faq_page = FAQPage(driver)
        faq_page.open_page()
        faq_page.scroll_to_faq_menu()
    
        question_locator = faq_data['q_locator']
        answer_locator = faq_data['a_locator']
        qusestion_text = faq_data['q_text']
        answer_text = faq_data['a_text']
        
        actual_question_text, actual_answer_text = faq_page.get_faq_text(question_locator, answer_locator)

        assert actual_question_text == qusestion_text
        assert actual_answer_text == answer_text
