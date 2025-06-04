from selenium.webdriver.common.by import By

class MainPageLocators:
    
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    
    FAQ_MENU = (By.XPATH, "//div[contains(@class, 'Home_FourPart__1uthg')]")
    
    FAQ_MENU_Q1 = (By.ID, "accordion__heading-0")
    FAQ_MENU_A1 = (By.ID, "accordion__panel-0")
    FAQ_MENU_Q2 = (By.ID, "accordion__heading-1")
    FAQ_MENU_A2 = (By.ID, "accordion__panel-1")
    FAQ_MENU_Q3 = (By.ID, "accordion__heading-2")
    FAQ_MENU_A3 = (By.ID, "accordion__panel-2")
    FAQ_MENU_Q4 = (By.ID, "accordion__heading-3")
    FAQ_MENU_A4 = (By.ID, "accordion__panel-3")
    FAQ_MENU_Q5 = (By.ID, "accordion__heading-4")
    FAQ_MENU_A5 = (By.ID, "accordion__panel-4")
    FAQ_MENU_Q6 = (By.ID, "accordion__heading-5")
    FAQ_MENU_A6 = (By.ID, "accordion__panel-5")
    FAQ_MENU_Q7 = (By.ID, "accordion__heading-6")
    FAQ_MENU_A7 = (By.ID, "accordion__panel-6")
    FAQ_MENU_Q8 = (By.ID, "accordion__heading-7")
    FAQ_MENU_A8 = (By.ID, "accordion__panel-7")