import allure
from pages.welcome import WelcomePage
from pages.user import UserPage
from pages.confirmation import ConfirmationPage
from pages.my_plants import MyPlantsPage
from pages.plant import PlantPage
from pages.add_plant import AddPlantPage

@allure.description("Test Navigation")
class TestNavigation:
    
    @allure.title("Test navigation through all the screens the app")
    def test_navigation_through_the_app(self):
        welcome_page = WelcomePage(self.driver)
        user_page = UserPage(self.driver)
        confirmation_page = ConfirmationPage(self.driver)
        add_plant_page = AddPlantPage(self.driver)
        my_plants_page = MyPlantsPage(self.driver)
        plant_page = PlantPage(self.driver)
        
        
        welcome_page.check_all_elements()
        welcome_page.click_start()
        assert user_page.is_displayed()
        
        user_page.check_all_elements()
        user_page.enter_user_name("Ru Cindrea")
        user_page.click_confirm()
        assert confirmation_page.is_displayed()
        
        confirmation_page.check_all_elements()
        confirmation_page.confirm()
        assert add_plant_page.is_displayed()
        
        add_plant_page.check_all_elements()
        add_plant_page.click_my_plants_tab()
        assert my_plants_page.is_displayed()
        
        my_plants_page.check_all_elements()
        my_plants_page.click_add_plant_tab()
        assert add_plant_page.is_displayed()
        
        add_plant_page.select_plant_by_id(0)
        assert plant_page.is_displayed()
        
        plant_page.check_all_elements()
        plant_page.cancel_plant()
        assert add_plant_page.is_displayed()
        
        add_plant_page.select_plant_by_id(0)
        plant_page.save_plant()
        assert confirmation_page.is_displayed()
        
        confirmation_page.check_all_elements()
        confirmation_page.confirm()
        assert add_plant_page.is_displayed()
        