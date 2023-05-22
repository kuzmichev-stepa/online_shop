from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import time
 
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    
    #time.sleep(30)

    # Ищем кнопку добавления в корзину
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
  
    # с помощью assert проверяем, что кнопка добавленияв корзиину кликабельна
    assert len(button) >0, "===Page haven't Button for add to basket==="
            
if __name__ == "__main__":
   pytest.main()
