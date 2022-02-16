import allure
import pytest
from pages.welcome import WelcomePage

@allure.description('Test Welcome Page')
class TestWelcomePage:
        
    @allure.title('Test that Welcome Page is displayed on startup')
    def test_welcome_page_is_displayed(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.check_all_elements()
    
    @allure.title('Test that Start button on Welcome Page loads User Page')
    def test_welcome_start_page_loads_user_page(self):
        welcome_page = WelcomePage(self.driver)
        user_page = welcome_page.click_start()
        assert user_page.is_displayed()
