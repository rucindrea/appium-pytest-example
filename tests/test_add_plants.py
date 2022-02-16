import allure
import pytest
from pages.welcome import WelcomePage
from pages.add_plant import AddPlantPage

@pytest.fixture(scope="class", autouse=True)
def go_to_add_plant_page(request):
    welcome_page = WelcomePage(request.cls.driver)
    user_page = welcome_page.click_start()
    confirmation_page = user_page.enter_user_name("Ru").click_confirm()
    request.cls.add_plant_page = confirmation_page.confirm()

class TestAddPlants():
    
    add_plant_page: AddPlantPage
    
    @allure.title("Test that a saved plant is added to My Plants")
    def test_saved_plant_is_added_to_my_plants(self):
        self.add_plant_page.click_add_plant_tab()
        save_plant_page = self.add_plant_page.select_plant_by_id(0)
        plant_name = save_plant_page.get_plant_name()
        save_plant_page.save_plant().confirm()
        my_plants_page = self.add_plant_page.click_my_plants_tab()
        assert len(my_plants_page.plants()) > 0
        
    @allure.title("Test that a saved plant has correct name in My Plants")
    def test_saved_plant_has_correct_name_in_my_plants(self):
        self.add_plant_page.click_add_plant_tab()
        save_plant_page = self.add_plant_page.select_plant_by_name("Dumbcane")
        save_plant_page.save_plant().confirm()
        my_plants_page = self.add_plant_page.click_my_plants_tab()
        assert my_plants_page.get_plant_name_by_id(0) == "Dumbcane"