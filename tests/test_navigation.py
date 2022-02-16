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
        
        pass
