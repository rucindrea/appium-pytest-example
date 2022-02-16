import allure
import pytest
from pages.welcome import WelcomePage
from pages.user import UserPage
from appium import webdriver

@allure.step('Go to User page')
@pytest.fixture(scope="class")
def go_to_user_page(driver):
    WelcomePage(driver).click_start()

@allure.step('Restart app and go to user page')
@pytest.fixture()
def restart_app_and_got_to_user_page(driver: webdriver):
    driver.reset()
    WelcomePage(driver).click_start()

@allure.description('Test User Page Basics')
@pytest.mark.usefixtures("go_to_user_page")
class TestUserPageBasics:
        
    @allure.title('Test that User Page is displayed')
    def test_user_page_is_displayed(self):
        user_page = UserPage(self.driver)
        user_page.check_all_elements()

    @allure.title('Test entering an empty user name')
    def test_enter_empty_user_name(self):
        user_page = UserPage(self.driver)
        user_page.enter_user_name('')
        assert user_page.get_user_name() == 'Enter your name'
    
    @allure.title('Test entering "John Doe" user name')
    def test_enter_user_name(self):
        user_page = UserPage(self.driver)
        user_page.enter_user_name('John Doe')
        assert user_page.get_user_name() == 'John Doe'

@allure.description('Test User Page Confirmation')
class TestUserPageConfirmation:
    
    @allure.title('Test that entering empty user name shows alert')
    def test_enter_empty_user_name_and_check_alert(self, restart_app_and_got_to_user_page):
        user_page = UserPage(self.driver)
        user_page.enter_user_name('')
        user_page.click_confirm()
        assert 'You have not entered your name' in user_page.check_alert_text()
    
    @allure.title('Test that you cannot save an empty user name')
    def test_enter_empty_user_name_and_accept_alert(self, restart_app_and_got_to_user_page):
        user_page = UserPage(self.driver)
        user_page.enter_user_name('')
        user_page.click_confirm()
        user_page.accept_alert()
        assert user_page.is_displayed()

    @allure.title('Test that you can save "John Doe" as user name')
    def test_enter_user_name(self, restart_app_and_got_to_user_page):
        user_page = UserPage(self.driver)
        user_page.enter_user_name('John Doe')
        confirmation_page = user_page.click_confirm()
        assert confirmation_page.is_displayed()