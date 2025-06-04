from selenium.webdriver.common.by import By


class OrderPageLocators:
    
    TITLE_ORDER = (By.CLASS_NAME, "Order_Header__BZXOb")
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    
    BUTTON_ORDER_HEADER = (By.CSS_SELECTOR, "div.Header_Nav__AGCXC button.Button_Button__ra12g")
    BUTTON_ORDER_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[contains(@class, 'Button_Button')]")
    
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    INPUT_SECOND_NAME = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    INPUT_ADDRESS = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    SELECT_METRO_STATION = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
    INPUT_PHONE_NUMBER = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')
    
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    
    INPUT_START_DATE = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')
    SELECT_START_DATE = (By.XPATH, "//div[contains(@class, 'react-datepicker__day--selected')]")
    SELECT_RENT_REPIOD = (By.CLASS_NAME, "Dropdown-control")
    SELECT_RENTAL_PERIOD_OPTIONS = (By.CLASS_NAME, "Dropdown-option")
    INPUT_COMMENT = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')
    
    BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[contains(@class, 'Button_Button') and contains(@class, 'Button_Middle') and not(contains(@class, 'Button_Inverted'))]")
    
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    TITLE_STATUS = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    @staticmethod
    def select_metro_station_option(station_name):
        return (By.XPATH, f"//button[.='{station_name}']")

    @staticmethod
    def select_color_checkbox(color):
        return (By.ID, color.lower())

    @staticmethod
    def select_rental_period_option(period):
        return (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']")
