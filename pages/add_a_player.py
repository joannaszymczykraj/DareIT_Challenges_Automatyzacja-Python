import time
from pages.base_page import BasePage


class AddAPlayer(BasePage):
    expected_title_add_player = "Add player"
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name='surname']"
    age_field_xpath = "//input[@name='age']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    submit_button_xpath = "//button[contains(@class,'containedPrimary') and @type='submit']"



    def title_of_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title_add_player
        time.sleep(5)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, date):
        self.field_send_keys(self.age_field_xpath, date)

    def type_in_main_position(self, position):
        self.field_send_keys(self.main_position_field_xpath, position)

    def click_on_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    # def assert_add_player(self): #dodane
    #     assert self.assert_add_player(self.add_player_title_xpath) == self.add_player_text #dodane
