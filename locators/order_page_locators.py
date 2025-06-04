from selenium.webdriver.common.by import By

class OrderPageLocators:
    
    TITLE_ORDER = (By.CLASS_NAME, "Order_Header__BZXOb")
    
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    INPUT_SECOND_NAME = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    INPUT_ADDRESS = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    SELECT_METRO_STATION = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
    INPUT_PHONE_NUMBER = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')
    
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    
    INPUT_START_DATE = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')
    SELECT_RENT_REPIOD = (By.CLASS_NAME, "Dropdown-control")
    SELECT_RENTAL_PERIOD_OPTIONS = (By.CLASS_NAME, "Dropdown-option")
    CHECKBOX_COLOR_BLACK = (By.ID, 'black')
    CHECKBOX_COLOR_GREY = (By.ID, 'grey')
    INPUT_COMMENT = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')
    
    BUTTON_BACK = (By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i and contains(text(), "Назад")')
    BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[contains(@class, 'Button_Button') and contains(@class, 'Button_Middle') and not(contains(@class, 'Button_Inverted'))]")
    
    TITLE_CONFIRM_WINDOW = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    BUTTON_NO = (By.XPATH, "//button[text()='Нет']")
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    
    TITLE_STATUS = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    BUTTON_VIEW_STATUS = (By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM and contains(text(), "Посмотреть статус")')
    