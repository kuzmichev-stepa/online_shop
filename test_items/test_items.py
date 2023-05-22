from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import time
import math
 
 link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket(browser):
    browser.implicitly_wait(10)
    browser.get(link)

    # Открываем поп-ап авторизации
    button = browser.find_element(By.ID, "ember33")
    button.click()
    
    #Находим элемент для ассерта
    modal_dialog = browser.find_element(By.ID, "ember84")
    
    # Код, который заполняет обязательные поля
    input1 = browser.find_element(By.ID, "id_login_email")
    input1.send_keys("kuzmichev.stepa@yandex.ru")
    input2 = browser.find_element(By.ID, "id_login_password")
    input2.send_keys("W)8fLZg5LP2bV2.")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # с помощью assert проверяем, что поп-ап закрылся
    assert EC.visibility_of_element_located(modal_dialog) != True, "smth broken"
            
if __name__ == "__main__":
    pytest.main()
