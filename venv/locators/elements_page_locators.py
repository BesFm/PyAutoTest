from selenium.webdriver.common.by import By



class TextBoxPageLocators:

    #INPUT
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    #OUTPUT
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

class CheckBoxPageLocators:
    EXPAND_ALL = (By.CSS_SELECTOR, "button[title='Expand all']")
    COLLAPSE_ALL = (By.CSS_SELECTOR, "button[title='Collapse all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")

    #Проверка
    CHECKED_ELEMENT = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ELEMENT = ".//ancestor::span[@class='rct-text']"
    OUTPUT_CHECKED = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_RADIO = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='yesRadio']")
    IMRESSIVE_RADIO = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='impressiveRadio']")
    NO_RADIO = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='noRadio']")

    #Проверка
    CHOOSEN_RADIO = (By.CSS_SELECTOR, "p span[class='text-success']")

